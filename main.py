import pandas as pd
import requests
import folium
from datetime import datetime
from flask import Flask, render_template, request

### MINE ###
def flightsPage():
    url = "https://travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com/v2/prices/nearest-places-matrix"

    querystring = {"origin":"KUL","destination":"SIN","flexibility":"0","currency":"SGD","show_to_affiliates":"true","limit":"1","distance":"100"}

    headers = {
	   "X-Access-Token": "a4513a2499b8fe893b280f163f979420",
	   "X-RapidAPI-Host": "travelpayouts-travelpayouts-flight-data-v1.p.rapidapi.com",
	   "X-RapidAPI-Key": "db6e55f4f3mshf88108bb0ec0e42p16c681jsn401df87f50ed"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response)

    data = response.json()
    #print(data)
    print(data['prices'])
    data = data['prices']



    return(data)

flightsData = flightsPage()


app = Flask(__name__)

@app.route('/') ##landing page
def home():
    return render_template("attractions.html")

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("floatingInput")
        print(email)


    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/attractions')
def attractions():
    return render_template("attractions.html")

@app.route('/flights')
def flights():
    flight_class = ["Economy", "Business", "First Class"]
    no_travellers = ["Travellers:",1,2,3,4,5,6,7,8,9,10]
    return render_template("flights.html", flight_class = flight_class, no_travellers = no_travellers, result = flightsData)

@app.route('/flightsResult')
def flightsResult():
    return render_template("flightsResult.html", result = flightsData)

@app.route('/hotels')
def hotels():
    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    return render_template("hotels.html", numbers=numbers)

@app.route('/hotelsResult')
def hotelsResult():
    return render_template("hotelsResult.html")

@app.route('/transport')
def transport():
    transportMode = ["Mode of Transport:", "driving", "walking", "bicycling", "transit", "flying"]
    return render_template("transport.html", transportMode=transportMode)

@app.route('/account')
def account():
    return render_template("account.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
