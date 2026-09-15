import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)

CORS(app)

API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route('/weather/<city>')
def get_weather(city):
    if not API_KEY:
        return jsonify({"error": "OPENWEATHER_API_KEY is not configured"}), 500

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
