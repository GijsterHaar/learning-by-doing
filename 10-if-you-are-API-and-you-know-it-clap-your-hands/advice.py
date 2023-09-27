import requests

action = input('What action would you like to perform,\
               \npress 1 for random advice\
               \npress 2 for search by id\
               \npress 3 for keyword search: ')

if not isinstance(action, str) or action == '':
    print("Ow no, that's not a valid input")

if action == '1':
    url = "https://api.adviceslip.com/advice"
    r = requests.get(url)
    obj = r.json()
    print(obj['slip']['advice'])

elif action == '2':
    search_id = input("Please enter an id: ")
    url = f"https://api.adviceslip.com/advice/{search_id}"
    r = requests.get(url)
    obj = r.json()
    print(obj['slip']['advice'])

elif action == '3':
    search_query = input("Please enter your search query here: ")
    url = f"https://api.adviceslip.com/advice/search/{search_query}"
    r = requests.get(url)
    obj = r.json()
    id_list = [d['id'] for d in obj['slips']]
    print(f"Here's a list of al advice ID's containing your query\n{id_list}")
