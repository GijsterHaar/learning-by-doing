
import requests
import subprocess

url = "https://coffee.alexflipnote.dev/random.json"
r = requests.get(url)
obj = r.json()
print(obj['file'])


subprocess.run(['firefox', obj['file']])

