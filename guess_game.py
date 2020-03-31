# "Guess the number" mini-game
# input will come from buttons and an input field
# all output for the game will be printed in the console


# You can find live, working copy at the url below
# http://www.codeskulptor.org/#user47_efpxT1AA10_0.py
# Click the play button to start


import simplegui
import random

secret_number = 0
range_type = 100
counter = 7

# helper function to start and restart the game
def new_game():
    
    if range_type == 1000:
        range1000()
    else:
        range100()
       
    
  

# define event handlers for control panel
def range100():
    global range_type, counter, secret_number
    counter = 7
    range_type = 100
    print
    print 'New game started. Range is 0 to 100'
    print counter,'guesses remaining'
    secret_number = random.randrange(0, 100) 
    

def range1000():
    global range_type, counter, secret_number
    counter = 10
    range_type = 1000
    print
    print 'New game started. Range is 0 to 1000'
    print counter,'guesses remaining'
    secret_number = random.randrange(0, 1000)
    

    
def input_guess(guess):
    global counter
    loc_guess = int(guess)
    print
    print 'Guess was',loc_guess
    if loc_guess > secret_number:
        print 'lower!'
        counter -= 1
        print counter,'guesses remaining'
    elif loc_guess < secret_number:
        print 'higher!'
        counter -= 1
        print counter,'guesses remaining'
    else:
        print 'correct!'
        new_game()
   
    if counter == 0:
        print 'sorry, you lose. Correct guess was',secret_number
        new_game()


    
# create frame
frame = simplegui.create_frame('guess the number game',200,200)

# register event handlers for control elements and start frame
frame.add_input('Guess my number:', input_guess, 100)
frame.add_button('Range [0, 100)', range100, 150)
frame.add_button('Range [0, 1000)', range1000, 150)
frame.start()



# call new_game 
new_game()

