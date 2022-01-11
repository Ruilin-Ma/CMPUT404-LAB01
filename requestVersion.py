import requests
print("request version is: ", requests.__version__)
print("###################")
response = requests.get("https://www.google.com")
print ("response status code is: ", response.status_code)
print ("response content is: ", response.content)