import requests
import json
from bs4 import BeautifulSoup

def download_data(url):
    response = requests.get(url)
    data = response.json()
    return data

def extract_data(data):
    show_info = {}
    show_info['id'] = data['id']
    show_info['url'] = data['url']
    show_info['name'] = data['name']
    show_info['season'] = data['_embedded']['episodes'][-1]['season']
    show_info['number'] = data['_embedded']['episodes'][-1]['number']
    show_info['type'] = data['type']
    show_info['airdate'] = data['_embedded']['episodes'][-1]['airdate']
    show_info['airtime'] = data['_embedded']['episodes'][-1]['airtime']
    show_info['runtime'] = data['runtime']
    show_info['average_rating'] = data['rating']['average']
    
    # Extract and format the summary without HTML tags
    summary_html = data['summary']
    summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
    show_info['summary'] = summary_text.strip()
    
    show_info['medium_image'] = data['image']['medium']
    show_info['original_image'] = data['image']['original']
    
    return show_info

url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
data = download_data(url)

show_data = extract_data(data)

# Save the extracted data to a JSON file
filename = "show_data.json"
with open(filename, 'w') as file:
    json.dump(show_data, file, indent=4)

print(f"The extracted data has been saved to the file '{filename}'.")
