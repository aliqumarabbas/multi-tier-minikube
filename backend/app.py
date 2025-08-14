from flask import Flask, jsonify
import os
import mysql.connector

app = Flask(__name__)

db_host = os.getenv("DB_HOST", "mysql")
db_pass = os.getenv("DB_PASSWORD", "root123")

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user='root',
            password=db_pass
        )
        return jsonify({"message": "Backend connected to MySQL!"})
    except:
        return jsonify({"message": "Backend cannot connect to MySQL!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)