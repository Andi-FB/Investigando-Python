import random

random_number = random.randint(0, 10)


def play():
    number_of_tries = 0
    while number_of_tries < 3:
        user_in = int(input('Try a number from 0 to 10'))
        if random_number == user_in:
            print('That´s correct you won!')
            number_of_tries = 3
        elif random_number < user_in:
            print('Lower!')
            number_of_tries += 1
        elif user_in == -1:
            print('CHEAT ENABLED: THE NUMBER IS {}'.format(random_number))
        elif abs(user_in - random_number) == 1:
            print('1 unit close!')
            number_of_tries += 1
        else:
            print('Higher!')
            number_of_tries += 1


play()
print('The number was {0}'.format(random_number))
wantsToPlayAgain = input('Want to play again? Y/N')
while wantsToPlayAgain.upper() == 'Y':
    play()
    wantsToPlayAgain = input('Want to play again? Y/N')
print('Game over :(')
