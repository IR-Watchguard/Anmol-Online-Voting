import os
from random import randint
# Generating a random number on our end
target = randint(1,100)

#Explaining the rules to the player
print("\n\nWelcome to PEHECHAAN SAKO TOH PEHECHAAN LO\n\n")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")

#Taking user's consent for the game
ask = input("Are you ready to proceed to the game? y or n\nYour response:")
if ask == 'y':
    os.system('cls')
    guess_counter = 1
    prev = 0
    while True:
        if guess_counter > 20:
            print(f'YOU LOST!!! The number was {target}')
        
        user_guess = int(input('Guess a number between 1 to 100: '))

        if user_guess < 1 or user_guess > 100:
            print("OUT OF BOUNDS!! Guess again: ")
            guess_counter += 1
            continue

        #If the user input matches the target we end the loop and break from the loop
        if target == user_guess:
            print(f'YOU WIN!! YOU TOOK {guess_counter} GUESSES\n')
            break

        if guess_counter == 1:
            prev = abs(user_guess - target)
            if prev <= 10:
                print("WARM")
            else:
                print("COLD")
            
        else:
            curr = abs(user_guess - target)
            if curr<prev:
                print("WARMER!! YOU ARE GETTING CLOSER")
            else:
                print("COLDER")
        
        guess_counter += 1

else:
    print('SEE YOU AGAIN!!')



