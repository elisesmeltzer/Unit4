import pymysql

USERNAME = 'admin'
PASSWORD = 'is3600_rds'
ENDPOINT = "is3600-41.cbw1bfhckbag.us-west-2.rds.amazonaws.com"
PORT = 3306
REGION = "us-west-2"
DBNAME = "unit41"
SSL_CA = "ssl/rds-combined-ca-bundle.pem"
CURSORCLASS = pymysql.cursors.DictCursor

