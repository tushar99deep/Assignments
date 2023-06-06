import requests
import csv
from bs4 import BeautifulSoup

# Function to download data from the API link
def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to extract the desired attributes from the episode data
def extract_episode_data(episode):
    episode_info = {
        'id': episode['id'],
        'url': episode['url'],
        'name': episode['name'],
        'season': episode['season'],
        'number': episode['number'],
        'airdate': episode['airdate'],
        'airtime': episode['airtime'],
        'runtime': episode['runtime'],
        'average_rating': episode['rating']['average']
    }

    # Extract and format the summary without HTML tags
    summary_html = episode['summary']
    summary_text = BeautifulSoup(summary_html, 'html.parser').get_text()
    episode_info['summary'] = summary_text.strip()

    return episode_info

# API link for the Westworld show
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"

# Download the data from the API
data = download_data(url)

if data is not None:
    # Extract the show information
    show_info = {
        'id': data['id'],
        'url': data['url'],
        'name': data['name'],
        'type': data['type'],
        'runtime': data['runtime'],
        'average_rating': data['rating']['average']
    }

    # Extract episode information
    episodes = data['_embedded']['episodes']
    episode_data = []
    for episode in episodes:
        episode_info = extract_episode_data(episode)
        episode_data.append(episode_info)

    # Define the CSV file name
    filename = "show_data.csv"

    # Write the show and episode data to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = list(show_info.keys())
        fieldnames.extend(list(episode_data[0].keys()))
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(show_info)
        writer.writerows(episode_data)

    print(f"The data has been saved to the file '{filename}'.")
else:
    print("Failed to retrieve data from the API.")
