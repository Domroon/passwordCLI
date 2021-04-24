import time

GERMAN = {
            "welcome" : "\nHerzlich Willkommen!\n",
            "requirements" : "\nFolgende Anforderungen sollte das Passwort haben:\n"
                             "- Mindestens 8 Zeichen\n"
                             "- Mindestens ein Großbuchstabe\n"
                             "- Mindestens ein Kleinbuchstabe\n"
                             "- Mindestens eine Zahl\n"
                             "- Mindestens eine Sonderzeichen\n",
            "main_menu" : "\n1 - Passwort Überprüfer\n"
                          "2 - Passwort Generator\n"
                          "q - Programm beenden\n"
         }

ENGLISH = {
            "welcome" : "\nwelcome!\n",
            "requirements" : "\nThe password should have the following requirements:\n"
                             "- At least 8 characters\n"
                             "- At least one capital letter\n"
                             "- At least one lowercase letter\n"
                             "- At least one number\n"
                             "- At least one special character\n",
            "main_menu" : "\n1 - Password checker\n"
                          "2 - Password generator\n"
                          "q - Exit program\n"
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

def password_verification():
    pass

def password_generation():
    pass

def main():
    user_input = None
    sentences = None
    while user_input != "q":
        while True:
            try:
                if language_selection() == '1':
                    sentences = ENGLISH.copy()
                else:
                    sentences = GERMAN.copy()
                break
            except InputError:
                print('\nPlease enter a valid Input\n')
                time.sleep(1)

        print(sentences["welcome"])
        time.sleep(1)

        print(sentences["main_menu"])

        user_input = input('input: ')


if __name__ == '__main__':
    main()