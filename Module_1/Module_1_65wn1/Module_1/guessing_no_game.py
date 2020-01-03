
# guessing a number game
winner = 10

while True:
    number = int(input("enter a number: "))
    if number == winner:
        print("You guessed it right!!", number)
        break
    elif number > winner:
        print("Entered number is large")
    else:
        print("Entered number is less than the correct number")

print("This line of code is outside the loop")


