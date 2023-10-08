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
def main():
    # I give previous_free_bikes a string as startvalue, because a False (or True) would mess
    # with my code when previous_free_bikes == 0
    previous_free_bikes = "welcome-message"

    url = "http://api.citybik.es/v2/networks/"
    r = requests.get(url)
    network_id = get_network_id(r.json())

    while True: #   create an infinite loop
        sleep(10)               # set iterations to 10 seconds per iteration

        url = f"http://api.citybik.es/v2/networks/{network_id[0]}"
        r = requests.get(url)
        free_bikes = get_free_bikes(r.json())
        
        free_bikes_message = print_free_bikes(free_bikes, previous_free_bikes)
        print(free_bikes_message)
        previous_free_bikes = free_bikes


def get_network_id(obj):
        network_id = [d['id'] for d in obj["networks"] if d['location']['city'] == 'London']
        return network_id

def get_free_bikes(obj):
        free_bikes = obj['network']['stations'][0]['free_bikes']
        return free_bikes

def print_free_bikes(free_bikes, previous_free_bikes):
        bike = 'bike' if free_bikes == 1 else 'bikes'
        if previous_free_bikes != 'welcome-message':
            if free_bikes < previous_free_bikes:
                difference = (previous_free_bikes - free_bikes)
                difbike = 'bike' if difference == 1 else 'bikes'
                return f"we rented out {difference} {difbike}. We have {free_bikes} {bike} left"
            elif free_bikes > previous_free_bikes:
                difference = (free_bikes - previous_free_bikes)
                difbike = 'bike' if difference == 1 else 'bikes'
                return f"we had {difference} {difbike} returned. We have {free_bikes} {bike} left"
            else:
                return f"Nothing happened in the last 10 seconds, we still have {free_bikes} {bike} left"
        else:
            return f"Welcome, we have {free_bikes} {bike} for rent"
        

    

if __name__ == '__main__':
    main()