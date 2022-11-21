import requests
import config
from flask import Flask
#Sources
##How to hide API Key: https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
##VirusTotal API docs: https://developers.virustotal.com/reference/ip-info

app = Flask(__name__)
app.config.from_object(__name__)

url = "https://www.virustotal.com/api/v3/ip_addresses/18.4.56.78"

headers = {
    "accept": "application/json",

    #If you wish to use your own API key replace below line with" "x-apikey": "yourfullapikeyfromVT"
    "x-apikey": config.api_key
}

response = requests.get(url, headers=headers)

@app.route('/')
def test():
    return response.text