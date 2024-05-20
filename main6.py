#--------Functions--------------
def password():
    attempts = 3
    while attempts > 0:
        password = input("What is the four digit password? ")
        try:
            password = int(password)
        except:
            attempts -= 1
            print("Those are not numbers. You have {} attempts left".format(attempts))
        if password == 3874:
            return True
    return False
def intro():
    name = input("What is your name? ")
    print("Welcome {} to the quiz".format(name))
def questions(question,correctanswer):
    global livesvar
    answer = input(question)
    if answer == correctanswer:
        print("Correct answer")
    else: 
        print("Incorrect answer")
        print("You have {} lives left.".format(livesvar))
def lives():
    global livesvar
    NUMBERS = [1,2,3,4]
    while True:
        livesvar = input("How many lives would you like? 4 max ")
        try:
            livesvar = int(livesvar)
            if NUMBERS in livesvar:
                return
        except:
            print("Thats not a valid amount of lives")





#Main Code
passwordstate = password()
if passwordstate == True:
    intro()
    
    questions()