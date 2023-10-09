from advice import check_valid_input, get_advice_by_id, get_id_list_by_search_query

def test_valid_input():
    result = check_valid_input('1')
    assert result == '1'

def test_invalid_input():
    result = check_valid_input('4')
    assert result == "Ow no, that's not a valid input"

def test_get_by_id():
    result = get_advice_by_id("11")
    assert result == "Avoid mixing Ginger Nuts with other biscuits, they contaminate. Keep separated."

def test_get_by_id_not_found():
    result = get_advice_by_id("22")
    assert result == 'Advice slip not found.'

def test_get_id_list_search_query_exists():
    result = get_id_list_by_search_query("man")
    assert result == "List of al advice ID's containing your query\n[46, 95, 125, 161]"

def test_get_id_list_search_query_not_exists():
    result = get_id_list_by_search_query("morning")
    assert result == "No advice slips found matching that search term."