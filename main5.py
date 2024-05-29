import random
def playagain():
    global keepplaying
    while True:
        playagain3 = input("Would you like to play again? ")
        if playagain3.lower() == "yes":
            keepplaying = True
            return
        elif playagain3.lower() == "no":
            print("Thank you for playing the Flag Quiz")
            keepplaying = False
            return 
        else:
            print("Please answer with Yes or No")


keepplaying = True
a2 = "red"
b2 = "blue"
c2 = "white"
d2 = "purple"
list1 = [a2, "a"]
list2 = [b2, "b", c2, "c", d2, "d"]
QTRIES = ["1", "2", "3", "4"]
QFORMAT = "{}\n A. {} B. {} C. {} D. {} "
QUESTIONS = ["What country has veritcal red, white and blue stripes on its flag? ",
                "What country has the only flag that isn't rectangular? ",
                    "What is the most common colour on flags?"]
GOOD_COMMENTS = ["Nice job", "Going strong", "Keep up the good work"]
BAD_COMMENTS = ["Nice try", "Keep trying", "Better luck next time"]
ANSWERS = ["france","nepal","red"]
SHORTOPTIONS = ["b","c","a"]
OPTIONS = [["Netherlands", "France", "Germany", "USA"],["Cameroon", "France", "Nepal", "Luxembourg"],["red","blue","white","purple"]]

#getting persons name
print("Hello Random Person")
name = input("what is your name? ")
#introducing them to the quiz
print ("Welcome", name, "to the Flag Quiz")
while keepplaying == True:
    #setting values
    score = 0
    #first question
    for x in range(len(QUESTIONS)):
        while True:
            q1tries = input("How many times do you want to try again if you get it wrong? 1-4 ")
            if q1tries in QTRIES:
                q1tries = int(q1tries)
                break
            print("That is not a number 1-4 please input a valid input.")
        while q1tries > 0:
            answer = input(QFORMAT.format(QUESTIONS[x], OPTIONS[x][0], OPTIONS[x][1], OPTIONS[x][2], OPTIONS[x][3]))
            #check the answer
            if(ANSWERS[x] in answer.lower() or answer.lower() == SHORTOPTIONS[x]):
                print(random.choice(GOOD_COMMENTS))
                print("You answered correctly!")
                score += 1
                q1tries -= 4
            else:
                q1tries -= 1
                print("That answer was incorrect. You have {} tries left".format(q1tries))
                print(random.choice(BAD_COMMENTS))
                if q1tries == 0:
                    print("The answer was {}.".format(OPTIONS[x][ANSWERS[x]]))
    #finish the quiz
    if(score == 3):
        print("Congrats {} you got {} out of 3 correct on the flag quiz".format(name, score))
    elif(score == 2):
        print("Nice try {} you got {} out of 3 correct on the flag quiz".format(name, score))
    else:
        print("Better luck next time {}. You got {} out of 3 correct on the flag quiz".format(name, score))
    playagain()


