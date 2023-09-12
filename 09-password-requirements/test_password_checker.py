
from contain_capital import MustContainCapital

def test_contain_capital_exist():
    result = MustContainCapital(1234).password
    assert result == 1234

def test_contain_capital():
    result = MustContainCapital('abCd')
    assert result.check() == True

def test_capital_message():
    result = MustContainCapital('aBcd')
    assert result.__str__() == 'The password must contain at least one capital.'