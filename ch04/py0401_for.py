"""
range(start=0, end, step=1)
"""

if __name__ == '__main__':
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(magician)

    for magician in magicians:
        print(magician.title() + 'is a great trick!')
        print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print("Thank you, everyone. That are a great magic show!")

    for value in range(5):
        print(value)

    numbers = list(range(5))
    print(numbers)

    even_numbers = range(2, 11, 2)
    print(list(even_numbers))

    digits = range(10)
    print(min(digits))
    print(max(digits))
    print(sum(digits))

    squares = [value ** 2 for value in range(11)]
    print(squares)




