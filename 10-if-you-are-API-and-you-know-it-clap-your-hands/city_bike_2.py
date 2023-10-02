import requests
from time import sleep

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

previous_free_bikes = False

url = "http://api.citybik.es/v2/networks/"
r = requests.get(url)
obj = r.json()
network_id = [d['id'] for d in obj["networks"] if d['location']['city'] == 'London']

while True: #   create an infinite loop
    sleep(10)               # set iterations to 10 seconds per iteration

    url = f"http://api.citybik.es/v2/networks/{network_id[0]}"
    r = requests.get(url)
    obj = r.json()
    free_bikes = ((obj['network']['stations'][0]['free_bikes']))
    bike = 'bike' if free_bikes == 1 else 'bikes'

    if previous_free_bikes != False:
        if free_bikes < previous_free_bikes:
            difference = (previous_free_bikes - free_bikes)
            difbike = 'bike' if difference == 1 else 'bikes'
            print(f"we rented out {difference} {difbike}. We have {free_bikes} {bike} left")
        elif free_bikes > previous_free_bikes:
            difference = (free_bikes - previous_free_bikes)
            difbike = 'bike' if difference == 1 else 'bikes'
            print(f"we had {difference} {difbike} returned. We have {free_bikes} {bike} left")
        else:
            print(f"Nothing happened in the last 10 seconds, we still have {free_bikes} {bike} left")
    else:
        print(f"Welcome, we have {free_bikes} {bike} for rent")
    
    previous_free_bikes = free_bikes
