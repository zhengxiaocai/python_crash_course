"""
形参 实参
"""


def greet_user(username):
    print(f'Hello {username if username else "Jack"}!')


def describe_pet(pet_name, animal_type='Cat'):
    """ 显示宠物信息 """
    print('\nI have a {}.'.format(animal_type))
    print(f"My {animal_type}'s name is {pet_name.title()}.")


if __name__ == '__main__':
    greet_user('')
    describe_pet('dog', 'harry')
    describe_pet(animal_type='Cat', pet_name='Tom')
    describe_pet('Ruby')
    describe_pet('doo', 'dog')
