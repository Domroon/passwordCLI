import string
from random import choice
import json

SENTENCES = {
    'English': {
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
    },
    'German' : {
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
    },
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


def load_languages():
    with open('languages.json', 'r') as file:
        data = json.load(file)
    
    # convert data to right dictionary-structure
    selected_languages = ["English", "German"]
    for language in selected_languages:
        languages = dict.fromkeys([language], data[language])
        
    return languages


def select_language():
    languages = list(SENTENCES)
    while True:
        print("Choose you language: ")
        for index, language in enumerate(languages, 1):
            print(f"{index} - {language}")
        user_input = input()
        try:
            index = int(user_input) - 1
            if 0 <= index < len(languages):
                break
        except ValueError:
            pass
    return SENTENCES[languages[index]]


def verify_password(password):
    password = set(password)
    return [
        message_key
        for test_result, message_key in [
            (len(password) >= 8, "wrong_length"),
            *(
                (password.intersection(characters), message_key)
                for characters, message_key in [
                    (string.ascii_uppercase + "ÄÖÜ", "no_uppercase"),
                    (string.ascii_lowercase + "äöüß", "no_lowercase"),
                    (string.digits, "no_digit"),
                    (string.punctuation, "no_special"),
                ]
            ) 
        ]
        if not test_result
    ]


def password_generation(length, sentences):
    if length < 8 or length > 20:
        raise InputError(length, ' is not a valid Input')

    password = ""
    while True:
        for i in range(length):
            all_signs = string.ascii_uppercase
            all_signs += string.ascii_lowercase
            all_signs += string.digits
            all_signs += string.punctuation

            password = password + choice(all_signs)
        
        if verify_password(password) == []:
            break
    
    print("\n" + password + "\n")


def main():
    load_languages()
    user_input = None
    sentences = None

    # Language Menu
    sentences = select_language()

    print(sentences["welcome"])

    # Main Menu
    print(sentences["main_menu"])

    while True:
        user_input = input('input: ')

        if user_input == '1':
            message_list = verify_password(input(sentences["password_input"]))
            for message in message_list:
                print(sentences[message])

            if message_list == []:
                print(sentences["success"])

            print(sentences["main_menu"])

        elif user_input == '2':
            while True:
                try:
                    length = int(input(sentences["length"]))
                    password_generation(length, sentences)
                    break
                except InputError:
                    print(sentences["wrong_input"])

            print(sentences["main_menu"])
        elif user_input == 'q':
            break
        else:
            print(sentences["wrong_input"])

        if user_input == "q":
            break


if __name__ == '__main__':
    main()