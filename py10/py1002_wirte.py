if __name__ == '__main__':
    file_name = 'programming.txt'
    with open(file_name, 'w') as f:
        f.write('I love programming!\n')
        f.write('I love creating new game.\n')

    with open(file_name, 'a') as f:
        f.write('I also love finding meaning in large datasets.\n')
        f.write('I love creating apps that can run in a browser.\n')
