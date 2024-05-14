def playagain():
    if start == -1:
        return True
    while True:
        playagain3 = input("Would you like to play again? ")
        if playagain3.lower() == "yes":
            return True
        elif playagain3.lower() == "no":
            print("Thank you for playing the Flag Quiz")
            return False
        else:
            print("Please answer with Yes or No")
start = 0
playagain()
print(playagain())