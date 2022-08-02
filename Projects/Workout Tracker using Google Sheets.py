import os
import requests
from datetime import datetime

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = "177"
AGE = "22"

TRACK_API = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API = os.environ["SHEET_ENDPOINT"]


# Creating the natural language query for the Nutritionix API
exercise_question = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_question,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(TRACK_API, json=parameters, headers=headers)
result = response.json()

# Creating the info and the connection to the Sheety API to edit rows in our spreadsheet
bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}
today = datetime.today()

for exercise in result["exercises"]:
    workout_info = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    print(workout_info)
    sheet_response = requests.post(SHEETY_API, json=workout_info, headers=bearer_headers)
    print(sheet_response.text)
