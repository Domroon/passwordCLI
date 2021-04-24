import random

GERMAN = {
            "welcome" : "\nHerzlich Willkommen!\n"
         }

ENGLISH = {
            "welcome" : "\nwelcome!\n"
          }

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
    language = None
    while user_input != "q":
        while True:
            try:
                if language_selection() == '1':
                    language = ENGLISH.copy()
                else:
                    language = GERMAN.copy()
                break
            except InputError:
                print('\n Please enter a valid Input \n')

        print(language["welcome"])

        

        user_input = input('input: ')

if __name__ == '__main__':
    main()