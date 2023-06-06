import requests
import csv
import json
from datetime import datetime

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def convert_to_csv(data, filename):
    headers = ['name', 'id', 'nametype', 'recclass', 'mass', 'year', 'reclat', 'reclong']

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        for entry in data:
            name = entry['name']
            id = entry['id']
            nametype = entry['nametype']
            recclass = entry['recclass']
            mass = float(entry['mass']) if 'mass' in entry else None
            year = datetime.strptime(entry['year'], '%Y-%m-%dT%H:%M:%S.%f').year if 'year' in entry else None
            reclat = float(entry['reclat']) if 'reclat' in entry else None
            reclong = float(entry['reclong']) if 'reclong' in entry else None

            writer.writerow({'name': name, 'id': id, 'nametype': nametype, 'recclass': recclass,
                             'mass': mass, 'year': year, 'reclat': reclat, 'reclong': reclong})

    print(f"CSV file '{filename}' has been created successfully.")

url = "https://data.nasa.gov/resource/y77d-th95.json"
data = download_data(url)

filename = "meteorite_data.csv"
convert_to_csv(data, filename)
