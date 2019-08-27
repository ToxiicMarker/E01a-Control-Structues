#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #this line prints a greeting
colors = ['red','orange','yellow','green','blue','violet','purple'] #this line states the the variable "color" is equal to red, orange, yellow, green, blue, violet, and purple. (all lowercase)
play_again = '' #this means that play_again is defined later in the code
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): #this line means that the subordinate code will be run until the input to the play_again question is equal to no or n
    match_color = random.choice(colors) #this line randomly picks one of the colors from the colors that the variable colors can be equal to 
    count = 0 #this line sets the count to 0 so that the counter resets each time the game is played again
    color = '' #this line says that color is further defined int eh subordinate code
    while (color != match_color): #this line will run the subordinate code until the correct input for color is equal to the randomly chosen match_color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #this line defines the color input as being lowercase and removes the spaces from the responses
        count += 1 #this increases the value of the count variable by 1
        if (color == match_color): #these two lines say that if the input is equal to the randomly selected match_color variable it will print "Correct!"
            print('Correct!')
        else: #these two lines print "Sorry, try again. You have guessed {the count is set to be equal to the guesses} times."
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))
    print('\nYou guessed it in {0} tries!'.format(count)) #this line prints the amount of guesses it took you to guess the correct color that was randomly selected
    if (count < best_count): #these three lines print "This was your best guess so far!" if your count was less than the best_cunt which is then set to be equal to the count 
        print('This was your best guess so far!')
        best_count = count
    play_again = input("\nWould you like to play again? ").lower().strip() #this line creates a space and then creates an input after the question "Would you like to play again?"
print('Thanks for playing!') #this line prints "Thanks for playing!" if the input to play_again is equal to n or no