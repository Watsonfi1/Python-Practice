#setting values
score = 0
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
    score = score + 1
else:
    print("You are incorrect, the answer was France.")
#other questions
answer2 = input("What country has the only flag that isn't square? ? ")
#check the answer
if("nepal" in answer2.lower()):
    print("You answered correctly!")
    score = score + 1
else:
    print("You are incorrect, the answer was Nepal.")
answer3 = input("What is the most common colour on flags? ")
#check the answer
if("red" in answer3.lower()):
    print("You answered correctly!")
    score = score + 1
else:
    print("You are incorrect, the answer was France.")
#finish the quiz
print("You got", score,"out of 3 correct on the flag quiz")
print("Thanks for playing the Flag Quiz")

