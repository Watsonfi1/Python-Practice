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
    global name
    name = input("What is your name? ")
    print("Welcome {} to the quiz".format(name))

def questions(question,correctanswer):
    global livesvar
    global score
    if livesvar > 0:
        answer = input(question)
        if answer.lower() == correctanswer:
            print("Correct answer")
            score += 1
        else: 
            print("Incorrect answer")
            livesvar -= 1
            print("You have {} lives left.".format(livesvar))

def lives():
    global livesvar
    NUMBERS = [1,2,3,4]
    while True:
        livesvar = input("How many lives would you like? 4 max ")
        try:
            livesvar = int(livesvar)
            if livesvar in NUMBERS:
                return
        except:
            print("Thats not a valid amount of lives")

def playagain():
    global play
    global score
    global name
    print("You got {} out of 3 {} well done!!!".format(score,name))
    while True:
        playagain3 = input("Would you like to play again? ")
        if playagain3.lower() == "yes":
            play = True
            return
        elif playagain3.lower() == "no":
            print("Thank you for playing the Flag Quiz")
            play = False
            return 
        else:
            print("Please answer with Yes or No")
#-------------Values-----------
QUESTIONS = ["What country has veritcal red, white and blue stripes on its flag? ",
                "What country has the only flag that isn't rectangular? ",
                    "What is the most common colour on flags?"]
play = True



#-----------Main Code---------
passwordstate = password()
if passwordstate == True:
    intro()
    while play == True:
        score = 0
        lives()
        questions(QUESTIONS[0],"france")
        questions(QUESTIONS[1],"nepal")
        questions(QUESTIONS[2],"red")
        playagain()