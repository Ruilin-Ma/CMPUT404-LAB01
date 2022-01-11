import requests
print("request version is: ", requests.__version__)
print("###################")
response = requests.get("https://www.google.com")
print ("response status code is: ", response.status_code)
print ("response content is: ", response.content)
singleRequest = requests.get('https://raw.githubusercontent.com/Ruilin-Ma/CMPUT404-LAB01/main/requestVersion.py')
print ("source code is: ", singleRequest.text)