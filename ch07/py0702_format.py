if __name__ == '__main__':
    a = 'ab%s%d%f' % ('c', 6, 9)
    b = 'ab{}{}{}'.format('c', 6, 9)

    c = 'abc'
    d = f'b{c}b'

    print(d)
    # print(a)
    # print(b)
