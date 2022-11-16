import requests
import config
url = "https://www.virustotal.com/api/v3/ip_addresses/18.4.56.78"

headers = {
    "accept": "application/json",
    "x-apikey": config.api_key
}

response = requests.get(url, headers=headers)

print(response.text)