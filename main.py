from flask import Flask, jsonify, request
from config import get_connection
from models import User

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({ "message": "Api Flask con python" })

@app.route("/users", methods=["GET"])
def get_user():
    try:
        connect = get_connection()
        with connect.cursor() as cursor:
            cursor.execute("SELECT * FROM USERS;")
            user = cursor.fetchall()
        return jsonify({ "data": user }), 200
    except Exception as e:
        return jsonify({ "Error": str(e) }), 500
    finally:
        connect.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)