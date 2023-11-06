import requests

def getAirport(iata):
    url = "https://airport-info.p.rapidapi.com/airport"

    querystring = {"iata":str(iata)}

    headers = {
        "X-RapidAPI-Key": "5ef4ff6610msh94da71473b98d63p14ac16jsn994619dd7994",
        "X-RapidAPI-Host": "airport-info.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    airports = {}
    
    airports[data["iata"]] = {
        #"iata": data["name"],
        "name": data["name"],
        "location": data["location"],
        "city": data["city"],
        "country": data["country"],
        "website": data["website"],
        "phone": data["phone"],
        
    }


    airports["flightOperators"].append({
        "name": "Operator1",
        "planes": 10
    })

    return airports