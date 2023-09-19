
from contain_capital import MustContainCapitalRequirement
from contain_number import MustContainNumberRequirement
from minimum_length import MustMeetMinimumLenghtRequirement
from contain_special_character import MustContainSpecialCharacterRequirement
from password_checker import PassWordChecker

import pytest

def test_contain_capital_exist():
    assert MustContainCapitalRequirement()

    
def test_contain_capital():
    result = MustContainCapitalRequirement()
    assert result.check('12Ab') == True


def test_not_contain_capital_empty_string():
    result = MustContainCapitalRequirement()
    assert result.check('') == False 


def test_not_contain_capital():
    result = MustContainCapitalRequirement()
    assert result.check('12dc') == False


def test_capital_message():
    result = MustContainCapitalRequirement()
    assert result.message() == 'The password must contain at least one capital.'


def test_contain_number_exist():
    assert MustContainNumberRequirement()


def test_contain_number():
    result = MustContainNumberRequirement()
    assert result.check('1bCd') == True


def test_not_contain_number_empty_string():
    result = MustContainNumberRequirement()
    assert result.check('') == False


def test_not_contain_number():
    result = MustContainNumberRequirement()
    assert result.check('Abcd') == False


def test_number_message():
    result = MustContainNumberRequirement()
    assert result.message() == 'The password must contain at least one number.'


def test_minimum_length_exist():
    assert MustMeetMinimumLenghtRequirement()


def test_minimum_length():
    result = MustMeetMinimumLenghtRequirement()
    assert result.check('1234Abcd') == True


def test_not_minimum_length():
    result = MustMeetMinimumLenghtRequirement()
    assert result.check('1234aBc') == False


def test_not_minimum_length_empty_string():
    result = MustMeetMinimumLenghtRequirement()
    assert result.check('') == False


def test_minimum_length_message():
    result = MustMeetMinimumLenghtRequirement()
    assert result.message() == 'The password must contain at least 8 characters.'


def test_special_character_exists():
    assert MustContainSpecialCharacterRequirement()


def test_special_character():
    result = MustContainSpecialCharacterRequirement()
    assert result.check('123?Abcd') == True


def test_not_contain_special_character_empty_string():
    result = MustContainSpecialCharacterRequirement()
    assert result.check('') == False


def test_not_contain_special_character():
    result = MustContainSpecialCharacterRequirement()
    assert result.check('1234Abcd') == False


def test_one_requirement():
    requirements = [MustMeetMinimumLenghtRequirement()]
    checker = PassWordChecker(requirements)
    checker.check('1234Abcd')
    assert checker.return_check()


def test_two_requirements():
    requirements = [MustContainNumberRequirement(),
                    MustContainCapitalRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('A7')
    assert checker.return_check()


def test_two_requirements_2():
    requirements = [MustContainNumberRequirement(),
                    MustMeetMinimumLenghtRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('1234Abcd')
    assert checker.return_check()


def test_two_requirements_fail():
    requirements = [MustContainNumberRequirement(),
                    MustContainCapitalRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('A')
    assert not checker.return_check()


def test_three_requirements():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('1234Abcd')
    assert checker.return_check() 


def test_three_requirements_fail():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('1234abcd')
    assert not checker.return_check()


def test_four_requirements():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('12?4Abcd')
    assert checker.return_check()


def test_four_requirements_fail():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('12?4abcd')
    assert not checker.return_check()


def test_return_one_message_capital():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('123>abcd')
    assert checker.message() == ['The password must contain at least one capital.']
    

def test_return_two_messages_capital_and_number():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('asdfa?cd')
    assert checker.message() == ['The password must contain at least one capital.',
                                 'The password must contain at least one number.'
                                 ]


def test_return_three_messages():
    requirements = [MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustMeetMinimumLenghtRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('asdf?bc')
    assert checker.message() == ['The password must contain at least one capital.',
                                 'The password must contain at least one number.',
                                 'The password must contain at least 8 characters.',
                                 ]


def test_return_all_messages():
    requirements = [MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustMeetMinimumLenghtRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)
    checker.check('asdfabc')
    assert checker.message() == ['The password must contain at least one capital.',
                                 'The password must contain at least one number.',
                                 'The password must contain at least 8 characters.',
                                 'The password must contain at least one special character.',
                                 ]
