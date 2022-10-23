# first get a random number
# second get a number from user
# compare user input with computer guess
# then take a decision according to the result of compare

from random import randint

MIN_RAGNE = 1
MAX_RANGE = 100
computer_guess = randint(MIN_RAGNE, MAX_RANGE)

for i in range(5):
    user_input = 0
    while user_input == 0 :
        try:
            user_input = int(input("please enter a number between 1 to 100 :"))
        except:
            print("please enter valid number")
    
    if user_input == computer_guess :
        print("hoora!!")
        break
    elif user_input > computer_guess:
        print("Your number is bigger than actual number")
    else:
        print("Your number is smaller than actual number")
        
    print("you still have {} try".format(4-i))

else:
    print("you lose the game")
    print("the actual number was ", computer_guess)