from infra.DBConnection import DBConnection
import pandas as pd
import requests
import urllib.parse

from datetime import datetime, date, timedelta

class CustomerService:

    def __init__(self):
        self.conn = DBConnection.getConnection()

    def get_cluste_locale(self):
        self.conn.execute("""
            SELECT 
                CONCAT(country, " ", state, " ", city, " ", postcode) as address 
            FROM 
                `wp_wc_customer_lookup`
            HAVING address != "";
        """)

        addresses = pd.DataFrame(self.conn.fetchall())
        addresses = list(addresses['address'])

        locales = []
        for address in addresses:
            url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
            response = requests.get(url).json()
            if(response != []):
                locales.append(dict({
                    'lat': response[0]["lat"],
                    'lon': response[0]["lon"],
                }))

        return locales

