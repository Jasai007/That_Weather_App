from flask import Flask, render_template, request 
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('API_KEY')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(BASE_URL, params=params)
        weather_data = response.json() if response.status_code == 200 else None
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
