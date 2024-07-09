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
    print("Received request:", request.method)  # Debug: print request method
    if request.method == 'POST':
        city = request.form['city']
        print("City:", city)  # Debug: print city input
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        print("Request params:", params)  # Debug: print request params
        response = requests.get(BASE_URL, params=params)
        print("Response status code:", response.status_code)  # Debug: print response status code
        if response.status_code == 200:
            weather_data = response.json()
            print("Weather data:", weather_data)  # Debug: print weather data
        else:
            print("Error:", response.text)  # Debug: print error message
    return render_template('index.html', weather=weather_data, city=city, appid=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)