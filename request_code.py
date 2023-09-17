import requests

url = "http://localhost:3000/"
params = {"country": "Philippines", "season": "Summer","season":"Rainy"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed with status code:", response.status_code)
