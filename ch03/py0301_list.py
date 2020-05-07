

if __name__ == '__main__':
    # 访问，查 list[index]
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles)
    print(bicycles[0])
    print(bicycles[0].title())
    print(bicycles[-1])

    message = 'My first bicycle was a ' + bicycles[0].title() + '.'
    print(message)

    # 改 list[index] = value
    motorcycle = ['honda', 'yamaha', 'suzuki']
    motorcycle[0] = 'ducati'
    print(motorcycle)

    # 增 list.append(value)  list.insert(index, value)
    motorcycle.append('moto')
    print(motorcycle)

    motorcycle.insert(0, 'first_moto')
    print(motorcycle)

    # 删
    # list.pop()   自动弹出最后一个
    # list.pop(index)  弹出任意元素
    # del list[index]   还是按照index去del
    # list.remove(value)    只按照value去删除，如果多次出现，只删除第一个。
    values = ['a', 'b', 'c', 'a']
    del values[3]
    print(values)
    values = ['a', 'b', 'c', 'a']
    values.remove('a')
    print(values)

    print(values.pop(0))
    


