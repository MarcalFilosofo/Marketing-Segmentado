import mariadb
import os
import sys

class DBConnection:
    @staticmethod
    def getConnection():
        # load_dotenv(override=True)
        try:
            conn = mariadb.connect(
                user='app_kpi',
                password='app_kpi',
                host='127.0.0.1',
                port=int(3306),
                database='wordpress'

                # HOST_CONNECT=""
                # DATABASE_PORT=3306
                # DATABASE_NAME="wordpress"
                # DATABASE_USERNAME="app_kpi"
                # DATABASE_PASSWORD="app_kpi"

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
            
        return conn.cursor(dictionary=True)

# conn = DBConnection.getConnection()