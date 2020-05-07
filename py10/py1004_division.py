"""
用户输入两个数，打印相除的结果
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
            print('answer:', answer)
        except ZeroDivisionError as e:
            print('Second number can not be 0:', e)
        except ValueError as e:
            print('Please enter number:', e)
