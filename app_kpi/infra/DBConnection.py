import mariadb
from dotenv import load_dotenv
import os
import sys

class DBConnection:
    @staticmethod
    def getConnection():
        load_dotenv(override=True)
        try:
            conn = mariadb.connect(
                user=os.environ['DATABASE_USERNAME'],
                password=os.environ['DATABASE_PASSWORD'],
                host=os.environ['HOST_CONNECT'],
                port=int(os.environ['DATABASE_PORT']),
                database=os.environ['DATABASE_NAME']

            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
            
        return conn.cursor(dictionary=True)

# conn = DBConnection.getConnection()