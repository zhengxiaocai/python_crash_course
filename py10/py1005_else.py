"""
思考一个问题：一段可能发生异常的代码放在try里，依赖这段代码后边的处理放哪里？
1.放到try-except之后
    这个指定不行，如果出现异常，后续流程会有问题。
2.放到try里
    只有那些可能发生异常的代码才丢在这里。
3.放到else里
    应该放到这里。
"""

if __name__ == '__main__':
    print('Please input two numbers, I will divide them.')
    print("Enter 'q' to quit.")

    while True:
        first_number = input('Please enter first number:')
        if first_number == 'q':
            break
        second_number = input('Please enter second number:')
        if second_number == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError as e:
            print('Second number can not be 0:', e)
        except ValueError as e:
            print('Please enter number:', e)
        else:
            print('answer:', answer)
