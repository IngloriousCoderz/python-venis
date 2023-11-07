import requests

response = requests.get("https://swapi.dev/api/people/1/")
print(response.status_code)
print(response.headers)
print(response.json())

response = requests.post(
    "https://swapi.dev/api/people/", json={'name': 'Antony'})
print(response.status_code)
print(response.headers)
print(response.json())

response = requests.patch(
    "https://swapi.dev/api/people/1/", json={'name': 'Antony'})
print(response.status_code)
print(response.headers)
print(response.json())

response = requests.delete(
    "https://swapi.dev/api/people/1/")
print(response.status_code)
print(response.headers)
print(response.json())
