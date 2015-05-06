# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# helper function to start and restart the game
num_range=100
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    
    print "New Game , Guess[0,100]"
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range=random.randint(0,100)
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=random.randint(0,1000)

    
def input_guess(guess):
    # main game logic goes here
    
    guess_count=1
    
    global num_range
    if int(guess)>num_range:
        print "Ni Cai : "+str(guess)
        print "Tai Da Le >"
        print "-----------------"
    elif int(guess)<num_range:
        print "Ni Cai : " + str(guess)
        print "Tai Xiao Le <"
        print "-----------------"        
    else:
        print "Cai Dui Le! :"+str(num_range)
        print "=================="
        new_game()
    # remove this when you add your code


    
# create frame
f=simplegui.create_frame("Cai Shu Zi",300,200)

# register event handlers for control elements and start frame
f.add_button("FanWei[0-100]",range100,200)
f.add_button("FanWei[0-1000]",range1000,200)
f.add_input("ShuRuYiGeShuZi:",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
