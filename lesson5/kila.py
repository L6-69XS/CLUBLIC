import random
play = True
number = str(random.randint(0,9)) 
while play:
    guess = input("guess the number \n")
    if number == guess:
        print("you win")
        print("the number was",number)
        break
    else:
        print("try again \n")
