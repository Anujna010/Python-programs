import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#gives the user a total of 6 chances to guess the right number
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('your guess is too high!')
    elif guess < secretNumber:
        print('your guess too low!')
    else: 
        break

if guess == secretNumber:
    print('good job! you guessed my number in '+str(guessesTaken)+' guesses!!')
else:
    print('Nope, the number I was thinking is '+str(secretNumber))