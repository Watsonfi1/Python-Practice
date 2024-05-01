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
else:
    print("You are incorrect, the answer was France.")
#finish the quiz
print("Thanks for playing the Flag Quiz")