# coding: utf-8
import os
from flask import *
from flask_cors import CORS

from functools import update_wrapper
from datetime import timedelta

from service.OrderService import OrderService
from service.CustomerService import CustomerService
from service.ProductService import ProductService

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')


def converter_em_dict(var, label):
    return dict({label: var})


orderService = OrderService()
customerService = CustomerService()
productService = ProductService()

@app.route('/products-kpis', methods=["GET"])
def return_products_kpis():
    return productService.get_products_kpis()

@app.route('/report', methods=['GET'])
def get_report():
    report = dict({
        'ticket_medio': orderService.get_ticket_medio(),
        'mrr': orderService.get_mrr(),
        'mau': orderService.get_mau(),
        'churn_liquido': orderService.get_churn_liquido(),
        'churn': orderService.get_churn_mensal(),
        "receita_liquida": orderService.get_receita_liquida(),
        "ltv": orderService.get_ltv(),
        "nps": orderService.get_nps(),
        "cac": orderService.get_cac(),
    })

    return report


@app.route('/historico_ticket_medio', methods=["GET"])
def return_historico_ticket_medio():
    return orderService.get_historico_ticket_medio()


@app.route('/groupping_hours', methods=["GET"])
def return_groupping_hours():
    return orderService.get_grouping_shopping_hours()


@app.route('/groupping_categories', methods=["GET"])
def return_groupping_categories():
    return orderService.get_groupping_categories()


@app.route('/cluster-locale', methods=["GET"])
def return_cluster_locale():
    return customerService.get_cluste_locale()


@app.route("/ticket-medio", methods=["GET"])
def return_ticket_medio():
    ticket_medio = orderService.get_ticket_medio()
    return converter_em_dict(ticket_medio, "ticket_medio")


@app.route("/get-mrr", methods=["GET"])
def return_mrr():
    mrr = orderService.get_mrr()
    return converter_em_dict(mrr, "mrr")


@app.route('/mau', methods=["GET"])
def return_mau():
    mau = orderService.get_mau()
    return converter_em_dict(mau, "mau")


@app.route("/churn-liquido", methods=["GET"])
def return_churn_liquido():
    churn = orderService.get_churn_liquido()
    return converter_em_dict(churn, "churn_liquido")


@app.route("/receita-liquida", methods=["GET"])
def return_receita_liquida():
    receita_liquida = orderService.get_receita_liquida()
    return converter_em_dict(receita_liquida, "receita_liquida")


@app.route("/ltv", methods=["GET"])
def return_ltv():
    ltv = orderService.get_ltv()
    return converter_em_dict(ltv, "ltv")


@app.route("/clv", methods=["GET"])
def return_clv():
    clv = orderService.get_clv()
    return converter_em_dict(clv, "clv")


@app.route("/nps", methods=["GET"])
def return_nps():
    nps = orderService.get_nps()
    return converter_em_dict(nps, "nps")


@app.route("/cac", methods=["GET"])
def return_cac():
    nps = orderService.get_cac()
    return converter_em_dict(nps, "cac")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
