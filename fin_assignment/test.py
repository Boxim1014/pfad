import httpx
from pyquery import PyQuery

url = 'https://www.buyiju.com/bgsm/'
data = {
    'year': 1980,
    'month': 1,
    'day': 18,
    'hour': 6
}
response = httpx.post(url, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'})

doc = PyQuery(response.text)
print(doc('.content>p').text())