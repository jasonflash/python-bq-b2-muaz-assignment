import random
# import is used to borrow anything from library or module 
def guess_the_number():
    #it is used to create a special set of instructions we will use at the last line of this program.
    secret_number = random.randint(1, 100)
    # = operator is used to give special name then RANDOM.RANDINT IS BASICALLY TELLING THE COMPUTER TO PICK A RANDOM NUMBER
    
    attempts = 0 #on this line it show how many times a person has attempted.
    max_attempts = 5 #here it shows how many times a person can attempt.

    print("Welcome to Guess the Number Game!")# print string
    print("I've picked a number between 1 and 100. Can you guess it?")#print string

    while attempts < max_attempts:
        #now the while loop starts, if attempts are less than total maximum attempts it stops, since it's not less, 
        #it will proceed until it meets the requirement.
        
        guess = int(input("Enter your guess: "))#we use int input to change the submitted input from string to integer.

        if guess == secret_number:
            #if the guess is equal to secret/random number then print the line written below and stop the code.
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            #f string is used to put a string inside an expression
            break #if the above condition is met the code stops.
        elif guess < secret_number:
            #if the guessed number/input number is less secret/random number print the line below.
            print("Too low! Try again.")
        else:
            #else print the line below
            print("Too high! Try again.")
        attempts += 1 # this is used to know how many times we've guessed/attempted.

    
    if attempts == max_attempts: #if attempts/guessed number is equal to maximum attempts, print the line below.
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

guess_the_number() # right here we're using the set of instrutions that we gave above on line 3