import json
import requests

#The API is stored in the node folder and uses port 3000
#Making A request to the API

r = requests.get("http://localhost:3000")
data=r.json()

counter = 0
for widget in data:
    print(data[counter]["name"] + " is " + data[counter]["color"])
    counter += 1