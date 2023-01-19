from random import randint
import sys


# created function for testing

def guesser(guess, answer):
    if 0 < guess < 10:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
       

# statement for running only testing part
if __name__ == '__main__':
    # generate a number 1~10
    answer = randint(1, 3)

    # input from user?
    # check that input is a number 1~10
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if guesser(guess, answer):
                break
        except ValueError:
            print('please enter a number')
        continue
