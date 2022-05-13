import requests
import pandas as pd
from geopy.geocoders import Nominatim
from threading import Timer
from bs4 import BeautifulSoup
def give_locname(lat,log):
    geolocator = Nominatim(user_agent="geoapiExercises")  
  
    # Latitude & Longitude input
    Latitude = lat
    
    Longitude = log
    para = Latitude+","+Longitude
    print(para)
    location = geolocator.reverse(para)
    
    address = location.raw['address']
      
    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    code = address.get('country_code')
    zipcode = address.get('postcode')
    print('City : ', city)
    print('State : ', state)
    print('Country : ', country)
    print('Zip Code : ', zipcode)
    print("")

def getlocation():
    
    source = requests.get('http://api.open-notify.org/iss-now.json').json()
    longitude=source['iss_position']['longitude']
    latitude=source['iss_position']['latitude']
    give_locname(latitude,longitude)
    Timer(0.5,getlocation).start()
getlocation()

