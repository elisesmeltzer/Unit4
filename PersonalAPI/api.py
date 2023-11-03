import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Create some test data for our catalog in the form of a list of dictionaries.
drivers = [
        {'id': 0,
            'name': 'Lewis Hamilton',
            'born': '1985',
            'team': 'Mercedes AMG Petronas',
            'points': '180'},
        {'id': 1,
            'name': 'Max Verstappen',
            'born': '1997',
            'team': 'Red Bull Racing',
            'points': '366'},
        {'id': 2,
            'name': 'Lando Norris',
            'born': '1999',
            'team': 'McLaren',
            'points': '101'}
        ]
@app.route('/', methods=['GET'])
def home():
    return '<h1>F1 Driver Info</h1><p>A prototype API for Formula 1 Driver information</p>'
    # A route to return all of the available entries in our catalog.
    @app.route('/api/v1/resources/f1/all', methods=['GET'])
    def api_all():
        return jsonify(drivers)

@app.route('/api/v1/resources/f1', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    # Create an empty list for our results
    results = []
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for driver in drivers:
        if driver['id'] == id:
            results.append(driver)
            # Use the jsonify function from Flask to convert our list of
            # Python dictionaries to the JSON format.
            return jsonify(results)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

import flask
from flask import request, jsonify
from config import *
import pymysql.cursors

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/api/v1/resources/songs', methods=['GET'])

def song_year():
    if 'year' in request.args:
        year = int(request.args['year'])
    else:
        return "Error: No year provided. Please specify a year."
    # Initiate RDS connection
    connection = start_rds_connection()
    with connection.cursor() as cursor:
        sql = f"SELECT * FROM top10s WHERE year = {year}"
        cursor.execute(sql)
        result = cursor.fetchall() # Retrieve all rows
        #connection.commit()
        return jsonify(result)
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


