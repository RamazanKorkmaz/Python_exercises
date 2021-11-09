num = 10
print("Let's play the guessing game")
while True:
    guess = int(input("enter a number: "))
    if guess > num:
        print("enter lower number")
    elif num > guess:
        print("enter higher number")
    else:
        print("Are you a MINDREADER")
        break