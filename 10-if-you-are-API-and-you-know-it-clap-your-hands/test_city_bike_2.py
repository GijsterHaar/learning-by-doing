from city_bike_2 import get_network_id, get_free_bikes, print_free_bikes

# create test data the way the function we want to test on expects it
NETWORKS = {'networks': 
            [{'company': ['3AO «СитиБайк»'], 'href': '/v2/networks/velobike-moscow', 'id': 'velobike-moscow', 'location': {'city': 'Moscow', 'country': 'RU', 'latitude': 55.75, 'longitude': 37.616667}, 'name': 'Velobike'},
             {'company': ['Urban Infrastructure Partner'], 'href': '/v2/networks/baerum-bysykkel', 'id': 'baerum-bysykkel', 'location': {'city': 'Bærum', 'country': 'NO', 'latitude': 59.89455, 'longitude': 10.546343}, 'name': 'Bysykkel'},
             {'company': ['PBSC', 'Serco Group plc'], 'href': '/v2/networks/santander-cycles', 'id': 'santander-cycles', 'location': {'city': 'London', 'country': 'GB', 'latitude': 51.51121389999999, 'longitude': -0.1198244}, 'name': 'Santander Cycles'}]}


def test_get_network_id():
    result = get_network_id(NETWORKS)
    assert result == ['santander-cycles']

def test_get_free_bikes():
    # create testdata with a path of keys leading to the final key/value we expect
    testdata = {'network': {'stations': [{'free_bikes': 11}]}} 
    result = get_free_bikes(testdata)
    assert result == 11

def test_get_free_bikes_fail():
    # create testdata with a path of keys leading to the final key/value we expect
    testdata = {'network': {'stations': [{'free_bikes': 11}]}} 
    result = get_free_bikes(testdata)
    assert result != 10

def test_print_free_bikes_start_message():
    result = print_free_bikes (11, 'welcome-message')
    assert result == "Welcome, we have 11 bikes for rent"

def test_print_free_bikes_same():
    result = print_free_bikes (11, 11)
    assert result == "Nothing happened in the last 10 seconds, we still have 11 bikes left"

def test_print_free_bikes_less_one():
    result = print_free_bikes (10, 11)
    assert result == "we rented out 1 bike. We have 10 bikes left"

def test_print_free_bikes_less_more_than_one():
    result = print_free_bikes (8, 11)
    assert result == "we rented out 3 bikes. We have 8 bikes left"

def test_print_free_bikes_less_more_than_one_and_just_one_left():
    result = print_free_bikes (1, 11)
    assert result == "we rented out 10 bikes. We have 1 bike left"

def test_print_free_bikes_plus_one():
    result = print_free_bikes (11, 10)
    assert result == "we had 1 bike returned. We have 11 bikes left"

def test_print_free_bikes_plus_more_than_one():
    result = print_free_bikes (11, 8)
    assert result == "we had 3 bikes returned. We have 11 bikes left"

def test_print_free_bikes_plus_one_start_with_zero():
    result = print_free_bikes (1, 0)
    assert result == "we had 1 bike returned. We have 1 bike left"
