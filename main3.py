#setting values
score = 0
a2 = "red"
b2 = "blue"
c2 = "white"
list1 = [a2, "a"]
list2 = [b2, "b", c2, "c"]
#getting persons name
print("Hello Random Person")
name = input("what is your name? ")
#introducing them to the quiz
print ("Welcome", name, "to the Flag Quiz")
#first question
answer1 = input("What country has veritcal red, white and blue stripes on its flag? ")
#check the answer
if("france" in answer1.lower()):
    print("You answered correctly!")
    score += 1
else:
    print("You are incorrect, the answer was France.")
#other questions
answer2 = input("What country has the only flag that isn't rectangular? ")
#check the answer
if("nepal" in answer2.lower()):
    print("You answered correctly!")
    score += 1
elif(answer2 == ""):
    print("That is not a answer to the question. The answer was Nepal")
else:
    print("You are incorrect, the answer was Nepal.")
answer3 = input("What is the most common colour on flags?\nA. {}\nB. {}\nC. {}\n".format(a2, b2, c2))
#check the answer
if(answer3.lower() in list1):
    print("You answered correctly!")
    score += 1
elif(answer3.lower() in list2):
    print("You answered incorrectly. The answer was red")
else:
    print("Your input is not in the question")
#finish the quiz
if(score == 3):
    print("Congrats {} you got {} out of 3 correct on the flag quiz".format(name, score))
elif(score == 2):
    print("Nice try {} you got {} out of 3 correct on the flag quiz".format(name, score))
else:
    print("Nice try {} you got {} out of 3 correct on the flag quiz".format(name, score))
print("Thanks for playing the Flag Quiz")

