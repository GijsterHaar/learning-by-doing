import requests

def main():
    action = input('What action would you like to perform,\
                \n - press 1 for random advice\
                \n - press 2 for search by id\
                \n - press 3 for keyword search: ')
    action = check_valid_input(action)
    if action == "1":
        message = get_random_advice()
    elif action == "2":
        search_id = input("Please enter an id: ")
        message = get_advice_by_id(search_id),
    elif action == "3":
        search_query = input("Please enter your search query here: ")
        message = get_id_list_by_search_query(search_query)
    else: message = action
    print(message)
   

def check_valid_input(action):
    if action not in ('1', '2', '3'):
        return "Ow no, that's not a valid input"
    return action

def get_random_advice():
        url = "https://api.adviceslip.com/advice"
        r = requests.get(url)
        obj = r.json()
        return obj['slip']['advice']

def get_advice_by_id(search_id):
    url = f"https://api.adviceslip.com/advice/{search_id}"
    r = requests.get(url)
    obj = r.json()
    if 'message' in obj:
        return obj['message']['text']
    else:
        return obj['slip']['advice']

def get_id_list_by_search_query(search_query):
    url = f"https://api.adviceslip.com/advice/search/{search_query}"
    r = requests.get(url)
    obj = r.json()
    if 'message' in obj:
        return obj['message']['text']
    else:
        return (f"List of al advice ID's containing your query\n{[d['id'] for d in obj['slips']]}")


if __name__ == "__main__":
    main()
