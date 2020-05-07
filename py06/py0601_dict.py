if __name__ == '__main__':
    alien_0 = {'color': 'green', 'point': 5}
    print(alien_0['color'], alien_0['point'])

    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
    alien_2 = {'color': 'red', 'points': 15}
    aliens = [alien_0, alien_1, alien_2]

    for alien in aliens:
        print(alien)
