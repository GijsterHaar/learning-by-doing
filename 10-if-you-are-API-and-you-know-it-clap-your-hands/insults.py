
import requests

language = 'en'
datatype = 'json'
arguments = {'lang': language, 'type': datatype}

for i in range(5):
    url = "https://evilinsult.com/generate_insult.php"
    r = requests.get(url, arguments)
    obj = r.json()
    print(obj['insult'])