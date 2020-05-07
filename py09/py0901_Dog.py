"""
创建Dog类，统一描述狗
属性：名字 年龄
动作：sit roll_over
"""


class Dog:
    """简单描述下小狗的行为。"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name.title()} is now sitting.')

    def roll_over(self):
        print(f'{self.name.title()} roll_over.')


if __name__ == '__main__':
    tom = Dog('Tom', 3)
    print(f'name: {tom.name}')
    print(f'age: {tom.age}')

    tom.sit()
    tom.roll_over()
