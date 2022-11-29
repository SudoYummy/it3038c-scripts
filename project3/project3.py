import requests
import config
from flask import Flask, render_template, request
import ipaddress
#Sources
##How to hide API Key: https://medium.com/black-tech-diva/hide-your-api-keys-7635e181a06c
##VirusTotal API docs: https://developers.virustotal.com/reference/ip-info
##How to use ipaddess module: https://docs.python.org/3/library/ipaddress.html

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def home():
    return render_template("index.html")
    
@app.route('/results', methods=['POST'])
def results():
    #This makes the request to VirusTotal. The entered ipaddress is used for the URL
    #ipvalue holds the entered IP address
    ipvalue=request.form['data']
    #making sure value entered was an IP address
    def ipv4(string):
        try:
            ipaddress.IPv4Network(string)
            return True
        except ValueError:
            return False
    if ipv4(ipvalue) == False:
        return "This is not a valid IP address please return to home page"

    #Below code will run only if the IP is valid
    url = "https://www.virustotal.com/api/v3/ip_addresses/%s" % (ipvalue)
    headers = {
        "accept": "application/json",
        #If you wish to use your own API key replace below line with" "x-apikey": "yourfullapikeyfromVT"
        "x-apikey": config.api_key
    }
    response = requests.get(url, headers=headers)
    #jsondata holds the response from VT
    ##'tags' attribute determines whether or not it is private
    jsondata = response.json()
    #Determine if the IP address is private/public
    try:
        if jsondata['data']['attributes']['tags'][0] == 'private':
            return "This is a private IP address. This cannot be searched with VirusTotal. Please return to homepage and enter a public IP."
    except:
        #These are values sent to the html page
        ipaddressvalue = jsondata['data']['id']
        malicious = jsondata['data']['attributes']['last_analysis_stats']['malicious']
        harmless = jsondata['data']['attributes']['last_analysis_stats']['harmless']
        suspicious = jsondata['data']['attributes']['last_analysis_stats']['suspicious']
        undetected = jsondata['data']['attributes']['last_analysis_stats']['undetected']
        total = int(malicious) + int(harmless) + int(suspicious) + int(undetected)
        return render_template("results.html", webip=ipaddressvalue, webmal=malicious, webharm=harmless, websus=suspicious, webund=undetected, webtotal = total)