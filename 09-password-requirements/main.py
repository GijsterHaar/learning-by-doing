from contain_capital import MustContainCapitalRequirement
from contain_number import MustContainNumberRequirement
from minimum_length import MustMeetMinimumLenghtRequirement
from contain_special_character import MustContainSpecialCharacterRequirement
from password_checker import PassWordChecker


def main():
    requirements = [MustMeetMinimumLenghtRequirement(),
                    MustContainCapitalRequirement(),
                    MustContainNumberRequirement(),
                    MustContainSpecialCharacterRequirement(),
                    ]
    checker = PassWordChecker(requirements)

    password = input("Please enter your password: ")
    checker.check(password)
    message = checker.message()
    print(message)





if __name__ == "__main__":
    main()