import requests

response = requests.get("http://localhost:5000/project/")
print(response.text)
