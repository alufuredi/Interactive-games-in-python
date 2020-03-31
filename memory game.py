# implementation of card game - Memory
# The game allows you to open only two cards at a time
# You are expected to remember positions of numbers and match them

# You can find live, working copy at the url below
# http://www.codeskulptor.org/#user47_cW0p0QjRXu_0.py
# Click the play button to start

import simplegui
import random

WIDTH = 800/16
a = range(1,9)
g = [False]
cards = a+a
card1,card2 = 0,0
count = 0


# helper function to initialize globals
def new_game():
    global state, exposed, count
    
    random.shuffle(cards)
    state = 0
    exposed = g*16
    count = 0
      

     
# define event handlers
def mouseclick(pos):
    global state,card1, card2, count
    index = pos[0]//WIDTH
    
    if exposed[index]:
        return
    
    #exposed[index] = True
    
    if state == 0:
        state = 1
        card1 = index
        exposed[index] = True
        #count += 1
    elif state == 1:
        card2 = index
        state = 2
        exposed[index] = True
        count += 1
    else:
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
        state = 1
        card1 = index
        exposed[index] = True
        #count += 1
     
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    txt_gap = WIDTH/2 - 6
    card_width = WIDTH/2
    x0,x2,y0,y2 = 0,WIDTH,5,95
    
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(cards[i]),[txt_gap,50],30,'White')
        else:
            canvas.draw_polygon([(x0, y0), (x2, y0), (x2, y2), (x0,y2)], 5,'Yellow', 'Green')
        txt_gap += WIDTH
        x0 = x2
        x2 += WIDTH
    
    label_txt = "Turns = " + str(count)
    label.set_text(label_txt)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

