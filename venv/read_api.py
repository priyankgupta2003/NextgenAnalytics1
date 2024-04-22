import requests
import mysql.connector as mc


cnx = mc.connect(user='scott', password='password', host='127.0.0.1', database='API_LIST')

api_url = "https://api.apis.guru/v2/list.json"

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    for 
else:
    print("Error: ", response.status_code)
