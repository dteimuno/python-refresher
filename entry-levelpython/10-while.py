#while loop can also be used with else and probabl elif too
secret_number = 3
guess = int(input("Guess a number:"))
while guess != secret_number:
    print("Wrong guess, try again!")
    guess = int(input("Guess a number:"))
    else:
    print("Congratulations, You guessed it right!")