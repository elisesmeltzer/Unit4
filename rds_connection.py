import pymysql.cursors
from config import *

# Define function to establish RDS connection
def start_rds_connection():
    try:
        connection = pymysql.connect(host=ENDPOINT,
                port=PORT,
                user=USERNAME,
                passwd=PASSWORD,
                db=DBNAME,
                cursorclass=CURSORCLASS,
                ssl_ca=SSL_CA)
        print('[+] RDS Connection Successful')
    except Exception as e:
        print(f'[+] RDS Connection Failed: {e}')
        connection = None
        return connection
    # Initiate RDS connection
    connection = start_rds_connection()
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM top10s"
        cursor.execute(sql)
        result = cursor.fetchall() # Retrieve all rows
        print(result)
        connection.commit()
