import requests
from datetime import datetime


# Variables used to generate the graph
USERNAME = "luisd3"
TOKEN = "ladehigo3202"
pixela_endppoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

graph_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}


# Post
pixel_endpoint = f"{pixela_endppoint}/{USERNAME}/graphs/graph1"
today = datetime(year=2022, month=7, day=10)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("For how many minutes did you code today?"),
}
response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)


# Update
update_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
pixel_new_info = {
    "quantity": "",
}

# Comment out to update
#response = requests.put(url=update_endpoint, json=pixel_new_info, headers=headers)
# print(response.text)


# Delete
delete_endpoint = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"
pixel_new_info = {
    "quantity": "",
}

# Comment out to delete
#response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
