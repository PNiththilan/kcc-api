from flask import Flask, jsonify
import mysql.connector
from flask_cors import CORS

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'kmmv',
}

app = Flask(__name__)
if app.debug:
   if app.debug:
        CORS(app)

@app.route('/api/data',methods = ['GET'])
def fetch_all_data():
    try:
        with mysql.connector.connect(**db_config) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM canteen")
                results = cursor.fetchall()

                # Convert the results to a list of dictionaries
                data_list = [{'id': result['id'], 'items': result['items'], 'price': result['price']} for result in results]

                return jsonify(data_list)

    except mysql.connector.Error as e:
        return jsonify({'error': f'MySQL Error: {str(e)}'}), 500
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
   
    
