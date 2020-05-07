"""
repr(str)  str.__repr__()
打印异常信息，重命名 as 一下，print(e)
"""
if __name__ == '__main__':
    age = input('How old are you: ')
    print(f'Your age is {type(age)}!')
    print(repr(age))

    try:
        if int(age) >= 18:
            print('adult')
        else:
            print('teenager')
    except TypeError as e:
        print(e)


