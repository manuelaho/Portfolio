# -*- coding: utf-8 -*-

import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

def fetch_data(name):
    
    url = f"{BASE_URL}/{name}"
    #params = {"contentType" : "json"}
    
    data = requests.get(url)
    
    return data.json()

