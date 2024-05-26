import random

def intro():
    global name
    name = input("What is your name? ")
    print("Welcome {} to the number guessing game".format(name))
def numguess():
    global number
    while True:
        amount = input("How many numbers would you like to guess between? ")
        try:
            amount = abs(int(amount))
            if amount == 0:
                print("Enter a number higher than 0")
            else:
                print("You are guessing for a number between 1 - {}".format(amount))
                break
        except:
            print("Thats not a number")
    number = random.randint(1, amount)
    while True:
        highorlow = input("Would you like higher or lower? Yes or No. ")
        if highorlow.lower() == "yes" or highorlow.lower() == "no":
            if highorlow.lower() == "yes":
                return True
            else:
                return False
        else:
            print("Answer with yes or no please")
def guessing():
    global freedom
    global number
    global highorlow
    while True:
        guess = input("What would you like to guess? ")
        try:
            guess = int(guess)
            break
        except:
            print("Try an actual number.")
    if guess == number:
        print("Congrats you guessed the right number.\n You are now free!")
        freedom = True
    else:
        if highorlow == True:
            if guess > number:
                print("Number is lower try again")
            else:
                print("Number is higher try again")
freedom = False
intro()
highorlow = numguess()
while freedom == False:
    guessing()

