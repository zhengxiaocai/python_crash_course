if __name__ == '__main__':
    filename = 'alice.txt'

    try:
        with open(filename, 'r') as f:
            f.read()
    except FileNotFoundError as e:
        print('File Not Found.', e)

    alice = 'programming.txt'
    try:
        with open(alice, 'r') as f:
            contents = f.read()
    except FileNotFoundError as e:
        print('File Not Found.')
    else:
        contents = contents.split()
        print(f'Len is {len(contents)}')
