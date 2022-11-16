import requests

url = "https://www.virustotal.com/api/v3/ip_addresses/ip"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)