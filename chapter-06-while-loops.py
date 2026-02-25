# File: MoveToWall.py
# ------------------------------
# Uses a "while" loop to move Karel until it hits
# a wall. Works on any sized world.
from karel.stanfordkarel import *

# the program starts with main
def main():
   # call the move to wall function
   move_to_wall()

# this is a very useful function 
def move_to_wall():
   # repeat the body while the condition holds
   while front_is_clear():
      move()


# File: BeeperLineBug.py
# ------------------------------
# Uses a while loop to place a line of beepers.
# This program works for a world of any size.
# However, because each world requires one fewer
# moves than put_beepers it always misses a beeper.
from karel.stanfordkarel import *

# program starts at main
def main():
   # repeats until karel faces a wall
   while front_is_clear():
      # place a beeper on current square
      put_beeper()
      # move to the next square
      move()


# The bug in this program is an example of a programming problem called a fencepost error. 
# The name comes from the fact that if you want to build a fence made of panels 
# which have one fence post on either size, the number of fence posts is always one greater 
# than the number of panels. How many fence posts, for example, 
# do you need to build a fence with 10 panels? The answer is 11

# File: BeeperLine.py
# ------------------------------
# Uses a while loop to place a line of beepers.
# This program works for a world of any size.
from karel.stanfordkarel import *

# program starts at main
def main():
   # repeats until karel faces a wall
   while front_is_clear():
      # place a beeper on current square
      put_beeper()
      # move to the next square
      move()
   # solves the fencepost bug
   put_beeper()