if __name__ == '__main__':
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())

    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')

    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')

    age = 19
    if age >= 18:
        print('You are old enough to vote!')
    else:
        print('Sorry, you are too young to vote!')

    if age < 4:
        print('0')
    elif age < 18:
        print('5')
    elif age < 65:
        print('10')
    else:
        print('5')


