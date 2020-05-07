if __name__ == '__main__':
    filename = 'alice.txt'

    try:
        with open(filename, 'r') as f:
            f.read()
    except FileNotFoundError as e:
        print('File Not Found.')
