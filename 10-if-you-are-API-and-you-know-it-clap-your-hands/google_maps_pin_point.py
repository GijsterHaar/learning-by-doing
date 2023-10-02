import requests
import webbrowser

"""
find the location of the only Dutch citybike shop and open it in google maps
"""

url = "http://api.citybik.es/v2/networks?fields=location"
r = requests.get(url)
obj = r.json()

location = [i['location'] for i in obj['networks'] if i['location']['country'] == 'NL']


latitude, longitude = location[0]['latitude'], location[0]['longitude']

webbrowser.open(f'https://google.com/maps/@{latitude},{longitude},18z')