def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = '{} {} {}'.format(first_name, middle_name, last_name)
    else:
        full_name = '{} {}'.format(first_name, last_name)
    return full_name.title()


def build_person(first_name, last_name, age=''):
    """返回一个字典，一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


def greet_users(names):
    """向每个人发出问候"""
    for name in names:
        msg = 'Hello, {}!'.format(name)
        print(msg)


if __name__ == '__main__':
    musician = get_formatted_name('jimi', 'lee', 'hendrix')
    lee = get_formatted_name('jimi', 'hendrix')
    print(musician)
    print(lee)

    music = build_person('jimi', 'hendrix', 18)
    print(music)

    usernames = ['hannah', 'ty', 'margot']
    greet_users(usernames)
