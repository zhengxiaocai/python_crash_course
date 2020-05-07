"""
就地永久性排序
sort(list, reverse=False)
临时性排序
sorted(list, reverse=False)
"""

if __name__ == '__main__':
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()
    print(cars)

    cars.sort(reverse=True)
    print(cars)

    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars = sorted(cars)
    print(cars)

    # 倒序
    print(list(reversed(cars)))

    # len(list)
    print(len(cars))
