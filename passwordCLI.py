import string
from random import choices
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
    password_length = len(password)
    password = set(password)
    return [
        message_key
        for test_result, message_key in [
            (password_length >= 8, "wrong_length"),
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


def password_generation(length):
    ALL_SIGNS = (string.ascii_uppercase
        + string.ascii_lowercase
        + string.digits
        + string.punctuation
    )

    if not 8 <= length <= 20:
        raise InputError(length, ' is not a valid Input')

    while True:
        password = "".join(choices(ALL_SIGNS, k=length))
        if verify_password(password) == []:
            break
            
    print(f"\n{password}\n")


def select_main_menu(sentences):
    print(sentences["main_menu"])
    while True:
        user_input = input('input: ')
        if user_input in ["1", "2", "q"]:
            break
        print(sentences["wrong_input"])
    return user_input


def check_password(sentences):
    password = input(sentences["password_input"])
    messages = verify_password(password)
    if not messages:
        print(sentences["success"])
    else:
        for message in messages:
            print(sentences[message])


def generate_password(sentences):
    while True:
        try:
            length = int(input(sentences["length"]))
            password_generation(length)
            break
        except (InputError, ValueError):
            print(sentences["wrong_input"])


def main():
    # Language Menu
    sentences = select_language()
    print(sentences["welcome"])

    # Main Menu
    while True:
        user_input = select_main_menu(sentences)
        if user_input == '1':
            check_password(sentences)
        elif user_input == '2':
            generate_password(sentences)
        elif user_input == 'q':
            break
        else:
            assert False, "not possible"


if __name__ == '__main__':
    main()