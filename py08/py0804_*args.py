def make_pizza(size, *toppings):
    """打印所有客户的佐料"""
    print("\nMaking a {}-inch pizza with the following toppings:".format(size))
    for topping in toppings:
        print('-{}'.format(topping))


def build_profile(first, last, **user_info):
    """创建一个字典，有用户所有想知道的东西。"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


if __name__ == '__main__':
    make_pizza(16, 'pepperoni')
    make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

    user_profile = build_profile('albert', 'einstein', location='princeton',
                                 field='physics')
    print(user_profile)
