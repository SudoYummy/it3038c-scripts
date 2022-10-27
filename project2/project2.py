import numpy as np
import re

##Define IP address regex
##Source: https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/
ip = re.compile('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

##Take in a file

with open("./ip.log") as log:
  lines = log.read()
  
  ##Extract all IP addresses using REGEX
  result = (ip.findall(lines))
  log.close()

##Output data on list: Number of Uniq, Total Number of IP addresses
uniqueip = len(np.unique(result))
totalip = len(result)

print("Total number of IPs: %s\nNumber of unique IPs: %s" % (totalip, uniqueip))
