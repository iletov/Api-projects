import requests
from datetime import datetime



current_date = datetime.now()

APP_ID = "app id"
API_KEY = "key"
TOKEN = "token"
EXERCISE_INPUT = input("What exercise did you do today? ")
DATE = current_date.strftime("%d/%m/%Y")
NOW_TIME = current_date.strftime("%X")


nutri_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/8ae95db65aafb4fb02cdbeef79537035/workoutTracking/workouts"



exercise_params = {
    "query": EXERCISE_INPUT,
    "gender": "male",
    "weight_kg": 95,
    "height_cm": 85,
    "age": 34
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

token_header = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.post(url=nutri_endpoint,
                         json=exercise_params,
                         headers=header)
result = response.json()

for exercise in result["exercises"]:
    nestet_sheet = {
        "workout": {
            "date": DATE,
            "time": NOW_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint,
                               json=nestet_sheet,
                               headers=token_header)
print(sheet_response.text)


