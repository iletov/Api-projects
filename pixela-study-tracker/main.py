import requests
from datetime import datetime


pixela_endpoint = 'https://pixe.la/v1/users'

today = datetime.now()

USERNAME = "username"
TOKEN = "random token"
GRAPH_ID = "graph id"
DATE = today.strftime("%Y%m%d")
QUANTITY = input("How many hours you spent learning? ")


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    "id": GRAPH_ID,
    "name": "Study graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers )
# print(response.text)

single_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_params = {
    "date": DATE,
    "quantity": QUANTITY,
}

response = requests.post(url=single_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

update_params = {
    "quantity": QUANTITY
}

# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)