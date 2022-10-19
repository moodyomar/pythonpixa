import requests

api = {
    "key": "17357236-aeda27ac71ed0d74e165db2a8",
    "baseurl": "https://pixabay.com/api",
    "q": ""
    }

def apiReq(query='thailand'):
    api["q"] = query
    url = f"{api['baseurl']}/?key={api['key']}&q={api['q']}"
    data = requests.get(url)
    return data.json()['hits']
print(apiReq("cat")[0]['webformatURL'])