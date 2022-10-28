# Project 2: Counting number of IPv4 Addresses in a file

This project will count the total number and number of unique of IPv4 Addresses in a specified file.

It uses the ```re``` and ```numpy``` modules to search for the IPv4 address pattern and output statistics on the resulting array

# Prerequisites

```
pip install numpy
```

* Note: You do not have to install the ```re``` module

# Usage

The file that will be parsed is currently hardcoded into the program. The provided file "ip.log" is stored in the same directory for ease of use.

To parse your own file change the following line of code and put the file path of the file.

```python
with open("./ip.log") as log:
```

Then simply execute the file:

```
python ./project2.py
```
