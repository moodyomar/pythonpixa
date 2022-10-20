import requests
from bs4 import BeautifulSoup

api = {
    "key": "17357236-aeda27ac71ed0d74e165db2a8",
    "baseurl": "https://pixabay.com/api",
    "query": "thailand beach"
    }

url = "http://localhost:3000"

def apiReq(query):
    print(f'utils query is: {query}')
    print(f"utils api[q] is: {api['query']}")
    url = f"{api['baseurl']}/?key={api['key']}&q={api['query']}"
    data = requests.get(url)
    return data.json()['hits']


def is_url_up(url):
    try:
        r = requests.head(url)
    except Exception:
        return False
    return r.status_code == 200


def is_website_running(url):
    try:
        r = requests.get(url)
        title = BeautifulSoup(r.text, 'html.parser')
    except Exception:
        return False
    return title.find("title").get_text()