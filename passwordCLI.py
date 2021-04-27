import string
from random import choice
import json


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
    with open('languages.json', 'rb') as file:
        return json.load(file)


def select_language():
    sentences = load_languages()
    languages = list(sentences)
    
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
    return sentences[languages[index]]


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
        else:
            password = ""
    
    print("\n" + password + "\n")


def main():
    print(type(load_languages()))
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