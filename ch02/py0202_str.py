"""
str.title()  字符串中的每个单词的首字母都是大写。
str.upper()  字符串中的每个字母都是大写
str.lower()  字符串中的每个字母都是小些
str.capitalize()  字符串的首字母大写，其余小写。
str.strip() str.rstrip() str.lstrip()
"""

if __name__ == '__main__':
    name = 'ada Lovelace'
    print(name.title())
    print(name.upper())
    print(name.lower())
    print(name.capitalize())

    # 字符串拼接。
    first_name = 'ada'
    last_name = 'lovelace'
    full_name = first_name + ' ' + last_name
    print(full_name)
    message = 'Hello, ' + full_name.title() + '!'
    print(message)

    # 使用制表符和换行符
    print('Python')
    print('\tPython')
    print('language:\n\tPython\n\tC\n\tJavaScript')

    # 删除空白 str.strip()
    favorite_language = ' Python '
    print(favorite_language.strip().__repr__())

    # 引号要好好用，单双岔开用
    msg = "One of Python's strengths is its diverse community."
    print(msg)

