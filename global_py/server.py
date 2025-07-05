from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Настройки подключения к MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="18112004Imkr",  # Укажи пароль, если есть
    database="global_db"
)

cursor = db.cursor()

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    services = data.get('services', [])

    if not name or not email:
        return jsonify({'message': 'Имя и Email обязательны'}), 400

    services_str = ', '.join(services)

    try:
        cursor.execute("INSERT INTO requests (name, email, services) VALUES (%s, %s, %s)", (name, email, services_str))
        db.commit()
    except Exception as e:
        print("Ошибка при вставке в БД:", e)
        return jsonify({'message': 'Ошибка при сохранении'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
