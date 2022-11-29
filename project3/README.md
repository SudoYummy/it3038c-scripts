# Project 3: Checking Reputation of an IP Address

This program creates a "website" that runs on port 3000. A user inputs an IP address into the form and basic results are pulled from VirusTotal's API for quick access.

# Prerequisites

```
pip install requests
pip install flask
```
* If you want to use your own API Key see the following lines of code:

```python
headers = {
    "accept": "application/json",
    #If you wish to use your own API key replace below line with" "x-apikey": "yourfullapikeyfromVT"
    "x-apikey": config.api_key
}
```

# Usage

To execute the file run ``` python ./web.py``` in the directory

Then navigate to ```http://localhost:3000/``` to have access to the form. Here is where you input the IP.

