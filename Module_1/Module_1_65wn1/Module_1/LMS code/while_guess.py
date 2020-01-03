attempts = 0
while 1:
    val = int(input("Guess the value between 0 to 10: "))
    attempts += 1
    if val == 9:
        print("you guessed it right")
        break
    else:
        print("Wrong guess")
    if attempts == 3:
        print("no more attempts left")
        break
