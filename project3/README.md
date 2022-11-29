# Project 3: Checking Reputation of an IP Address

This program creates a "website" that runs on port 3000. A user inputs an IP address into the form and basic results are pulled from VirusTotal's API for quick access. This tool is useful for a variety of reasons. The first is automation. While this use case uses a GUI interface, that can easily be removed so the tool can automatically injest IP addresses and report them. The other is a just a quick lookup tool for SOC analyst. Time is key for a SOC and having quick efficient processes allows for a more secure business.

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

