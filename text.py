
def add(x, y):
    print(x + y)


if __name__ == '__main__':
    s = "add(3, 5)"
    a = "print('test')"
    exec(a)
    exec(s)
