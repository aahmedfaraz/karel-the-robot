# write any code you want

# This program fills the diagonals of the world with beepers, 
# then turns around and collects them back up

from karel.stanfordkarel import *

def main():
   # Fill beepers on diagonals
   fill_beepers()
   # Now face opposite direction to move back
   turn_around()
   # Collect beepers from diagonals
   collect_beepers()
   
def fill_beepers():
   while front_is_clear():
      put_beeper()
      move_to_diagonal()
   put_beeper()
   
def collect_beepers():
   while front_is_clear():
      pick_beeper()
      move_to_diagonal()
   pick_beeper()
      
def move_to_diagonal():
   move()
   turn_left()
   move()
   turn_right()

def turn_right():
   turn_around()
   turn_left()
   
def turn_around():
   turn_left()
   turn_left()