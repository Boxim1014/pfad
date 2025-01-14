
import requests

url = 'https://www.dearmoney.com.tw/eightwords'

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to retrieve content: {response.status_code}")