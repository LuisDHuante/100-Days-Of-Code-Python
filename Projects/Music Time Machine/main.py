import base64
import json
import datetime
from bs4 import BeautifulSoup
import requests


#Validate date format
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


#Ask for user input and validate
date = input("From which year do you want to create the playlist? Type the date in this format YYYY-MM-DD: ")
validate(date)


#Web scrape the top 100 songs
response = requests.get(
    f"https://www.billboard.com/charts/hot-100/{date}")
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
songs = soup.select(selector="li #title-of-a-story")


#Add song titles to a list
top_100_songs = [song.getText().strip() for song in songs]
print(top_100_songs)


#Connection to Spotify API
URL = "https://accounts.spotify.com/api/token"
CLIENT_ID = ""
CLIENT_SECRET = ""
headers = {}
data = {}


# Encode as Base64
message = f"{CLIENT_ID}:{CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')
headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"
r = requests.post(URL, headers=headers, data=data)
token = r.json()['access_token']


#Create Spotify Playlist
playlistUrl = f"hhttps://api.spotify.com/v1/users/{CLIENT_ID}/playlists"
headers = {
    "Authorization": "Bearer " + token,
    "name": f"Billboard Top 100: {date}",
    "description": "New playlist description",
    "public": False,
    "collaborative": False,
}
res = requests.post(url=playlistUrl, headers=headers)
print(json.dumps(res.json(), indent=2))

#Get URI's of all tracks

#Pass list of URI's to new playlist
