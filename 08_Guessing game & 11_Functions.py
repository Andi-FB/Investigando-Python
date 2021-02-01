import random

random_number = random.randint(0, 10)


def validate_in():
    input_ok = False
    while not input_ok:
        user_in = input("Try a number from 0 to 10")
        if user_in.isnumeric():
            return user_in


def play():
    number_of_tries = 0
    while number_of_tries < 3:
        user_in = validate_in()
        if random_number == user_in:
            print('That´s correct you won!')
            return
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


# This is not really recommended in python because of def keyword
# def welcome: print("Welcome")
# the name of the resulting function object is specifically 'welcome' instead of the generic '<lambda>'
# But lambda functions are quite practical e.g. to define a sorting function
welcome = lambda: print('Welcome!')

welcome()
wantsToPlayAgain = 'Y'
while wantsToPlayAgain.upper() == 'Y':
    play()
    wantsToPlayAgain = input('Want to play again? Y/N')
print('Game over :(')
