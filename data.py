import requests

parameter = {
    "amount": 10,
    "category": 31,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameter)
data = response.json()
question_data = data['results']

