"""
合并成一个程序，先尝试读取。
"""
import json

if __name__ == '__main__':
    filename = 'username.json'
    try:
        with open(filename, 'r') as f_out:
            username = json.load(f_out)
    except FileNotFoundError as e:
        username = input("What's your name?")
        with open(filename, 'w') as f_in:
            json.dump(username, f_in)
            print(f"We'll remember you when you come back, {username}.")
    else:
        print(f"Welcome back, {username}.")
