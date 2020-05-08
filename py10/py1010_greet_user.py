import json

if __name__ == '__main__':
    filename = 'username.json'

    with open(filename, 'r') as f_out:
        username = json.load(f_out)
        print(f"Welcome back {username}.")
