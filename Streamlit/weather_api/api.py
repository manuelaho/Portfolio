# Bibliothek für API-requests
import requests                           

# Basiszugriff auf URL und key in Variable speichern 
BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

key = "xxx"


# Klassen für Fehler bauen
class MaximumRequestsDone(Exception):
    pass

class UndefinedLocation(Exception):
    pass

class WrongAPIKey(Exception):
    pass

class WrongDatum(Exception):
    pass


# Funktion für Anfrage an API(Rückgabe als jason)

def fetch_data_for_city(city, start, end):
    
    try:
        
        url = f"{BASE_URL}/{city}/{start}/{end}"
        
        # Parameter, die wir brauchen(gibt auch noch andere)
        params = {"key" : key, "unitGroup" : "metric", "contentType" : "json"}   
        
        # in Variable speichern die Ausgabe mit url und Parameter
        res = requests.get(url, params)
    
        return res.json()
    
    except ValueError as e:
        print(res.text)
        
        if "maximum number" in res.text:
            raise MaximumRequestsDone
            
        elif "Invalid location found" in res.text:
            raise UndefinedLocation
        
        elif "API key" in res.text:
            raise WrongAPIKey
            
        elif "cannot be before" in res.text:
            raise WrongDatum
            
        
            
        
