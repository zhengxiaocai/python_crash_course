"""
这样才能打印异常的具体信息。直接打印Exception只能得到class
except Exception as e:
    print(e)
"""


if __name__ == '__main__':
    dimemsions = (200, 50)
    print(dimemsions[0])
    print(dimemsions[1])

    try:
        dimemsions[0] = 250
    except TypeError as e:
        print(e)


