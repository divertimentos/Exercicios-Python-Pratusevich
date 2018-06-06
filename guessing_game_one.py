'''
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extra 1: Keep the game going until the user types “exit”
Extra 2: Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint

rand = randint(1, 9)
counter = 0

while True:
    user = (input("Guess a number (type 'exit' do leave): \n"))
    if user == "exit":
        print(f"Guesses: {counter}")
        break
    else:
        user = int(user)  
        counter += 1       
        if user < rand:
            print(f"{user} is too low.")
        elif user > rand:
            print(f"{user} is too high.")
        elif user == rand:
            print(f"{user} is exactly right!")
