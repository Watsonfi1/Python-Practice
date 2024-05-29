import math

def pythagoras(num1,num2):
    num3 = num1**2 + num2**2
    num3 = math.sqrt(num3)
    return num3

print("Enter the number next to what you want to do. \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division", 
      "\n 5. To the Power \n 6. Square Root \n 7. Pythagoras Thereom")
type = input()

if type == "5":
    num1 = input("What number do you want to be squared?")
    num2 = input("What number would you like it to be to the power of?")