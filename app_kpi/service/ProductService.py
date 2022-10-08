from ast import If
from re import X
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from infra.DBConnection import DBConnection


class ProductService(object):
    def __init__(self):
        self.conn = DBConnection.getConnection()

    def get_qt_orders(self, product_id):
        self.conn.execute("""
            SELECT COUNT(*) qt FROM `wp_wc_order_product_lookup`
            WHERE product_id  = %s
        """, [product_id])

        pedidos = pd.DataFrame(self.conn.fetchall())

        sum_compras = np.sum(list(pedidos['qt']))

        return sum_compras

    def get_index_recompra(self, product_id):
        self.conn.execute("""
            SELECT COUNT(*) qt, customer_id, product_id FROM `wp_wc_order_product_lookup`
            WHERE product_id  = %s
            GROUP BY customer_id, product_id
        """, [product_id])

        pedidos = pd.DataFrame(self.conn.fetchall())

        try:
            sum_compras = np.sum(list(pedidos['qt']))

            filter = pedidos['qt'] > 1

            recompras = pedidos.where(filter)
            sum_recompras = np.sum(list(recompras['qt'].fillna(0)))

            if (sum_compras == 0):
                return 0

            num_recompra = round(sum_recompras / sum_compras * 100, 2)
            return num_recompra
        except KeyError:
            return 0

    def get_products_kpis(self):
        self.conn.execute("""
            SELECT 
                wp_posts.ID,
                wp_posts.post_title,
                Round(Avg(DISTINCT(wp_commentmeta.meta_value)), 1) AS nps,
                -- COUNT(DISTINCT(wp_wc_order_product_lookup.product_id)) as qt_orders,
                COUNT(DISTINCT(wp_commentmeta.meta_id)) as rating_count,
                Round(wp_wc_product_meta_lookup.max_price, 2) as current_price,
                wp_wc_product_meta_lookup.stock_quantity,
                CASE 
                    WHEN wp_wc_product_meta_lookup.stock_status = "instock" THEN 1
                    ELSE 0
                END as stock_status
            FROM   wp_posts
                LEFT JOIN wp_comments
                        ON wp_posts.id = wp_comments.comment_post_id
                LEFT JOIN wp_commentmeta
                        ON wp_comments.comment_id = wp_commentmeta.comment_id
                -- LEFT JOIN wp_wc_order_product_lookup
                --        ON wp_posts.ID = wp_wc_order_product_lookup.product_id
                LEFT JOIN wp_wc_product_meta_lookup
                        ON wp_posts.ID = wp_wc_product_meta_lookup.product_id
            WHERE 
            (wp_commentmeta.meta_key = 'rating' OR wp_commentmeta.meta_key is null)
            AND wp_posts.post_type = "product"
            GROUP BY wp_posts.post_title  
        """)

        products_kpis_1 = pd.DataFrame(self.conn.fetchall())

        products_kpis_list = []

        for index, row in products_kpis_1.iterrows():
            index_recompra = self.get_index_recompra(row['ID'])
            qt_orders = self.get_qt_orders(row['ID'])

            new_row = dict({
                "id": row['ID'],
                "post_title": row['post_title'],
                "current_price": row['current_price'],
                "nps": row['nps'],
                "stock_quantity": row['stock_quantity'],
                "stock_status": row['stock_status'],
                "qt_orders": qt_orders,
                # "rating_count": row['rating_count'],
                "repurchase": index_recompra,
            })
            products_kpis_list.append(new_row)

        products_kpi = pd.DataFrame(products_kpis_list)
        
        products_kpi['nps'] = products_kpi['nps'].fillna(0)
        products_kpi['stock_quantity'] = products_kpi['stock_quantity'].fillna(99999)

        scaler = StandardScaler()

        products_kpi_2 = products_kpi
        scaled_data = scaler.fit_transform(products_kpi_2.drop(['current_price', 'post_title', 'id'], axis=1))

        scaled_orders = pd.DataFrame(scaled_data)

        ratings = []

        for sd in scaled_data:
            ratings.append(np.mean(sd))
            
        min = float(np.min(ratings))
        max = float(np.max(ratings))

        new_ratings = list(
            map(
                lambda x: self.get_rating(min, max, x)
                , ratings
            )
        )

        X = np.array(products_kpi.drop(['post_title', 'id', 'current_price'], axis=1))
        
        kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

        classes = list(map(self.padronizar_classe, kmeans.labels_))
        products_kpi['K_classes'] = classes
        products_kpi['rating'] = new_ratings

        products_kpi = products_kpi.sort_values(by='rating', ascending=False)
        return products_kpi.to_dict('records')

    def get_rating(self, min, max, rating):
        if(min < 0):
            new_min = 0
            new_max = max + (min * -1)
            rating = rating + (min * -1)

        if(min > 0):
            new_min = 0
            new_max = max - min
            rating = rating - min


        fator_scaler = 10 / new_max

        new_rating = fator_scaler * rating

        return round(new_rating, 2)


    def padronizar_classe(self, k_class):
        if(k_class == 1):
            return "C"
        
        if(k_class == 0):
            return "B"

        if(k_class == 2):
            return "A"
