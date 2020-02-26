import random
print('Name: ')
name=input()
secretNum=random.randint(1,7)
print('Well '+name+' range(1,20):')
for guessesTaken in range(1,7):
    print('Take guess')
    guess=int(input())
    if guess < secretNum:
        print('Your guess is too low')
    elif guess > secretNum:
        print('Your guess is too high')
    #elif guess == secretNum:
     #   print('Your guess was correct')
    else:
        print('Your guess was correct')
        break
print('You took '+str(guessesTaken)+' guesses')
        
