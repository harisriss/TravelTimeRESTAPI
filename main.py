"""
5b3ce3597851110001cf624821e44c6c9a554cdfaa1190672abbd9f1
"""
from flask import Flask, request
import openrouteservice
from openrouteservice.directions import directions

app = Flask(__name__)


@app.route('/')
def createRoute():
    #format coordonne : (longitude, latitude)
    coords = ((5.917781,45.564601),(4.835659,45.764043))
    client = openrouteservice.Client(
        key='5b3ce3597851110001cf624821e44c6c9a554cdfaa1190672abbd9f1')  # Specify your personal API key
    routes = directions(client, coords)  # Now it shows you all arguments for .directions

    return routes


if __name__ == "__main__":
    app.run()
