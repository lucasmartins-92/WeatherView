import csv
import datetime
import pytz
import requests
import urllib
import uuid
import googlemaps

from flask import redirect, render_template, request, session
from functools import wraps

gmaps = googlemaps.Client(key='') # User should provide their own Google Maps API key.

weathercode = {
    0:"Clear sky",
    1:"Mainly clear",
    2:"partly cloudy",
    3:"overcast",
    45:"Fog",
    48:"depositing rime fog",
    51:"light drizzle",
    53:"moderate drizzle",
    55:"intense drizzle",
    56:"light freezing drizzle",
    57:"intense freezing drizzle",
    61:"Slight rain",
    63:"moderate rain",
    65:"heavy rain",
    66:"light freezing rain",
    67:"heavy freezing rain",
    71:"light snowfall",
    73:"moderate snowfall",
    75:"heavy snowfall",
    77:"snow grains",
    80:"slight rain showers",
    81:"moderate rain showers",
    82:"violent rain showers",
    85:"slight snow showers",
    86:"heavy snow showers",
    95:"thunderstorm",
    96:"thunderstorm w/ slight hail",
    99:"thunderstorm w/ heavy hail"
    }

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


def geocode(place):
    api_response = gmaps.geocode(place)
    lat, lng, formattedaddress = lat, lng, formattedaddress = api_response[0]['geometry']['location']['lat'], api_response[0]["geometry"]["location"]["lng"], api_response[0]['formatted_address']
    return lat, lng, formattedaddress


def weather(lat,lng):
    payload = {
            'latitude': lat,
            'longitude': lng,
            "current": ["temperature_2m", "weather_code"],
            "daily": ["temperature_2m_max", "temperature_2m_min"],
            "forecast_days": 1
    }
    api = requests.get(
        'https://api.open-meteo.com/v1/forecast', params=payload
    ).json()
    code = api['current']['weather_code']
    return weathercode[code], api['current']['temperature_2m'], api['daily']['temperature_2m_max'][0], api['daily']['temperature_2m_min'][0]

    