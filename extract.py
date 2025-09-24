import requests
import pandas as pd

def extract_data():
    # Construct the API with star and end dates provided by Data Factory, formatted for geojson output.
    url = f"https://rickandmortyapi.com/api/character/1,10"

    # Make the GET request to fetch data
    response = requests.get(url)

    #Check if the request was successful
    if response.status_code == 200:
        #Get the JSON response
        data = response.json()

    else:
        print("Failed to fetch) data. Status code: ", response.status_code)
    return pd.DataFrame(data)