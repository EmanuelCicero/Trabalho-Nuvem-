from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)


def users():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',  
        'port': '3306',
        'database': 'projeto'
    }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT username, email FROM users')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


@app.route('/')
def index():
    return jsonify({'Resultado': users()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
