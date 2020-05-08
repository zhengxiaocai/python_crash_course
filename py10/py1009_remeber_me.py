"""
把用户输入的名字储存起来
"""
import json

if __name__ == '__main__':
    username = input("What's your name?")

    file = 'username.json'
    with open(file, 'w') as fin:
        json.dump(username, fin)
        print(f"We'll remember you when you come back, {username}.")
