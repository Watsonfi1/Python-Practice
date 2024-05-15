def playagain():
    while True:
        playagain3 = input("Would you like to play again? ")
        if playagain3.lower() == "yes":
            return True
        elif playagain3.lower() == "no":
            print("Thank you for playing the Flag Quiz")
            return False
        else:
            print("Please answer with Yes or No")
keepplaying = True
a2 = "red"
b2 = "blue"
c2 = "white"
list1 = [a2, "a"]
list2 = [b2, "b", c2, "c"]
QTRIES = ["1", "2", "3", "4"]
#getting persons name
print("Hello Random Person")
name = input("what is your name? ")
#introducing them to the quiz
print ("Welcome", name, "to the Flag Quiz")
while keepplaying == True:
    #setting values
    score = 0
    #first question
    while True:
        q1tries = input("How many times do you want to try again if you get it wrong? 1-4 ")
        if q1tries in QTRIES:
            q1tries = int(q1tries)
            break
        print("That is not a number 1-4 please input a valid input.")
    while q1tries > 0:
        answer1 = input("What country has veritcal red, white and blue stripes on its flag? ")
        #check the answer
        if("france" in answer1.lower()):
            print("You answered correctly!")
            score += 1
            q1tries -= 4
        else:
            q1tries -= 1
            print("That answer was incorrect. You have {} tries left".format(q1tries))
            if q1tries == 0:
                print("The answer was France.")


    while True:
        q2tries = input("How many times do you want to try again if you get it wrong? 1-4 ")
        if q2tries in QTRIES:
            q2tries = int(q2tries)
            break
        print("That is not a number 1-4 please input a valid input.")
    while q2tries > 0:
        answer2 = input("What country has the only flag that isn't rectangular? ")
        #check the answer
        if("nepal" in answer2.lower()):
            print("You answered correctly!")
            score += 1
            q2tries -= 4
        else:
            q2tries -= 1
            print("That answer was incorrect. You have {} tries left".format(q2tries))
            if q2tries == 0:
                print("The answer was Nepal.")


    while True:
        q3tries = input("How many times do you want to try again if you get it wrong? 1-4 ")
        if q3tries in QTRIES:
            q3tries = int(q3tries)
            break
        print("That is not a number 1-4 please input a valid input.")
    while q3tries > 0:
        answer3 = input("What is the most common colour on flags?\nA. {}\nB. {}\nC. {}\n".format(a2, b2, c2))
        #check the answer
        if(answer3.lower() in list1):
            print("You answered correctly!")
            score += 1
            q3tries -= 4
        else:
            q3tries -= 1
            print("That answer was incorrect. You have {} tries left".format(q3tries))
            if q3tries == 0:
                print("The answer was Red.")


    #finish the quiz
    if(score == 3):
        print("Congrats {} you got {} out of 3 correct on the flag quiz".format(name, score))
    elif(score == 2):
        print("Nice try {} you got {} out of 3 correct on the flag quiz".format(name, score))
    else:
        print("Better luck next time {}. You got {} out of 3 correct on the flag quiz".format(name, score))
    keepplaying = playagain()


