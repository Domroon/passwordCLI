import random


class InputError(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


def language_selection():
    print(f'Choose your language: ')
    print(f'1 - English')
    print(f'2 - German')
    user_input = input()
    if (user_input != '1') and (user_input != '2'):
        raise InputError(user_input, ' is not a valid Input')
    
    return user_input
    

def main():
    user_input = None
    while user_input != "q":
        while True:
            try:
                language_selection()
                break
            except InputError:
                print('Please enter a valid Input')
        user_input = input('Input: ')


if __name__ == '__main__':
    main()