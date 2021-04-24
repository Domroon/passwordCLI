import time
import string
import random

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
                          "q - Programm beenden\n",
            "wrong_input" : "\nBitte gib einen gültigen Wert ein\n",
            "password_input" : "\nBitte geben Sie ein Passwort ein: ",
            "success" : "\nDas Passwort ist OK!",
            "wrong_length" : "- Zu Kurz",
            "no_uppercase" : "- Kein Großbuchstabe enthalten",
            "no_lowercase" : "- Kein Kleinbuchstabe enthalten",
            "no_digit" : "- Keine Zahl enthalten",
            "no_special" : "- Kein Sonderzeichen enthalten",
            "length" : "Passwortlänge(8-20): "
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
                          "q - Exit program\n",
            "wrong_input": "\nPlease enter a valid value\n",
            "password_input": "\nPlease enter a password: ",
            "success": "\nThe password is OK!",
            "wrong_length": "- Too short",
            "no_uppercase": "- No capital letter",
            "no_lowercase": "- Contains no lower case letter",
            "no_digit": "- Does not contain a number",
            "no_special": "- No special characters included",
            "length" : "Password length (8-20): "
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


def password_verification(password, sentences, give_return=False):
    length = False
    uppercase_letter = False
    lowercase_letter = False
    digit = False
    special_char = False

    if len(password) >= 8:
        length = True

    for letter in password:
        if letter in string.ascii_uppercase + "ÄÖÜ":
            uppercase_letter = True

        if letter in string.ascii_lowercase + "äöüß":
            lowercase_letter = True

        if letter in string.digits:
            digit = True

        if letter in string.punctuation:
            special_char = True

    if not give_return:
        if not length:
            print(sentences["wrong_length"])

        if not uppercase_letter:
            print(sentences["no_uppercase"])

        if not lowercase_letter:
            print(sentences["no_lowercase"])

        if not digit:
            print(sentences["no_digit"])

        if not special_char:
            print(sentences["no_special"])

    if length and uppercase_letter and lowercase_letter and digit and special_char:
        if give_return:
            return True
        print(sentences["success"])
        time.sleep(1)

    if give_return:
        return False


def password_generation(length):
    password=""
    for i in range(length):
        random_char_type = random.randint(0, 3)
        char_types = {
                        0 : string.ascii_uppercase[random.randint(0, len(string.ascii_uppercase)-1)],
                        1 : string.ascii_lowercase[random.randint(0, len(string.ascii_lowercase)-1)],
                        2 : string.digits[random.randint(0, len(string.digits)-1)],
                        3 : string.punctuation[random.randint(0, len(string.punctuation)-1)]
                     }
        password = password + char_types[random_char_type]
    
    print("\n" + password + "\n")


def main():
    user_input = None
    sentences = None

    # Language Menu
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

        # Main Menu
        print(sentences["main_menu"])

        while True:
            user_input = input('input: ')
            if user_input == '1':
                password_verification(input(sentences["password_input"]), sentences)
                time.sleep(1)
                print(sentences["main_menu"])
            elif user_input == '2':
                length = int(input(sentences["length"]))
                password_generation(length)
                print(sentences["main_menu"])
            elif user_input == 'q':
                break
            else:
                print(sentences["wrong_input"])
                time.sleep(1)


if __name__ == '__main__':
    main()