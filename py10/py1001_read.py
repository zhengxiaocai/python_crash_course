if __name__ == '__main__':
    with open('pi.txt', 'r') as f:
        contents = f.read()
        print(contents.rstrip())

    with open('dir/test.txt', 'r') as f:
        contents = f.read()
        print('contents_type:', type(contents))

    # 绝对路径
    file_path = '/Users/hanxing/PycharmProjects/python_crash_course/py10/pi.txt'
    with open(file_path, 'r') as f:
        contents = f.read()
        print(contents)

    # 逐行
    file_name = 'pi.txt'
    with open(file_name) as file_object:
        for line in file_object:
            print(line.rstrip())

    # 储存在列表中，后续处理
    with open(file_name) as f:
        lines = f.readlines()
        print('lines_type:', type(lines))

    for line in lines:
        print('line:', line.rstrip())

    # 使用文件内容
    with open(file_name) as f:
        lines = f.readlines()

    pi_str = ''
    for line in lines:
        pi_str += line.strip()
    print(f'pi_str: {pi_str}')
    print(len(pi_str))
