def is_str_close(a):
    for i in a:
        a = a.replace('()', '')
        a = a.replace('{}', '')
        a = a.replace('[]', '')
        if not a:
            break
    return False if a else True


if __name__ == '__main__':
    b = '{[{()}]()}'
    c = '{[{()}]([)]}'
    print(is_str_close(b))
    print(is_str_close(c))
