"""
最后的完美状态，拆分成三个函数。
"""
import json


def get_stored_username():
    try:
        filename = 'username.json'
        with open(filename, 'r') as f_out:
            username = json.load(f_out)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name?")

    filename = 'username.json'
    with open(filename, 'w') as f_in:
        json.dump(username, f_in)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}.")


if __name__ == '__main__':
    greet_user()
