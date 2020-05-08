def count_words(filename):
    """读取文件单词个数"""

    try:
        with open(filename, 'r') as f:
            contents = f.read()
    except FileNotFoundError as e:
        print('File Not Found.', e)
    else:
        words = contents.split()
        nums_words = len(words)
        print(f'Len({filename}) is {nums_words}.')


if __name__ == '__main__':
    file = 'programming.txt'
    count_words(file)

    # 或者可以循环调用
    files = ['pi.txt', 'alice.txt', 'programming.txt']
    for file in files:
        count_words(file)
