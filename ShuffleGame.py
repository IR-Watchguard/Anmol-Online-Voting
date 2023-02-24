from random import shuffle

#Function to take user input
def player_guess():
    guess = ''
    while guess not in ['0','1','2']: 
        guess = input('Pick a number: 0,1 or 2:\n')
    
    return int(guess)

#To check user input with the shuffled cups
def cup_game(cups,guess_count):
    guess = player_guess()
    while guess_count<3 or cups[guess]!='O':
        if guess_count==2:
            print(f'YOU LOSE\nTHE CUPS WERE ORGANIZED AS: {cups}')
            exit()

        if cups[guess]=='O':
            print(f'YOU CHOOSE THE RIGHT CUP\n {cups}')
            break
        elif cups[guess]!='O':
            print('WRONG GUESS!! GUESS AGAIN')
            guess_count += 1
            cup_game(cups,guess_count+1)
        else:
            pass

#Initial Cups Configuration
cups = [' ','O',' ']
print(f'This is the initial configuration\n{cups}')
shuffle(cups)
guess_count = 0
cup_game(cups,guess_count)