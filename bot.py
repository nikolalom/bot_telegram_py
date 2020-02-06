import requests

url = "https://api.telegram.org/bot1061254538:AAEO8julHGjZC22l2hies4A1-q7N315cU9U/"


def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]