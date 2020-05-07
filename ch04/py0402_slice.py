if __name__ == '__main__':
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])
    print(players[1:4])
    print(players[0:4])
    print(players[2:])
    print(players[-3:])

    print("Here are the first three players on my team:")
    for player in players[:3]:
        print('\t', player)

    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:]
    print('my_foods:', my_foods)
    print('friend_foods:', friend_foods)

    my_foods.append('cannoli')
    friend_foods.append('ice cream')
    print(id(my_foods), my_foods)
    print(id(friend_foods), friend_foods)
