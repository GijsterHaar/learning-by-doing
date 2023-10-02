import requests
from time import sleep
import itertools

"""
find any bike shop and use time/sleep to repeat available bikes
every 10 seconds and the difference with 10 seconds ago

1. find a citybike shop in London using the  http://api.citybik.es/v2/networks obj to find London in obj['networks']['location']['city']

2. get the 'id' from that obj

2. use that network_id to find the shop:
"http://api.citybik.es/v2/networks/{network_id}" and create an obj from that

3. in the 'stations' field find 'free_bikes'

4. get info every 10 seconds with time.sleep()

5. calculate the difference in 'free_bikes' with the previous info 'free_bikes"
and print
"""

compare_free_bikes = []
start = True
for i in itertools.count(): #   create an infinite loop
    sleep(10)               # set iterations to 10 seconds per iteration

    url = "http://api.citybik.es/v2/networks/"
    r = requests.get(url)
    obj = r.json()
    network_id = [d['id'] for d in obj["networks"] if d['location']['city'] == 'London']


    url = f"http://api.citybik.es/v2/networks/{network_id[0]}"
    r = requests.get(url)
    obj = r.json()

    compare_free_bikes.append((obj['network']['stations'][0]['free_bikes']))

    bike = 'bike' if obj['network']['stations'][0]['free_bikes'] == 1 else 'bikes'
    
    if start == True:
        print(f"Welcome, we have {compare_free_bikes[-1]} {bike} for rent")
        sleep(10)

    if compare_free_bikes[i] < compare_free_bikes[i-1]:
        difference = compare_free_bikes[i-1] - compare_free_bikes[i]
        difbike = 'bike' if difference == 1 else 'bikes'
        print(f'we rented out {difference} {difbike}, we have {compare_free_bikes[i]} {bike} left')
    elif compare_free_bikes[i] > compare_free_bikes[i-1]:
        difference = compare_free_bikes[i] - compare_free_bikes[i-1]
        difbike = 'bike' if difference == 1 else 'bikes'
        print(f'{difference} {difbike} got returned, we have {compare_free_bikes[i]} {bike} left')
    else:
        print(f"Nothing happened in the last 10 seconds, we still have {compare_free_bikes[i]} {bike} left")
    
    start = False
