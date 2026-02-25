# karel-the-robot
This repo contains my practice about Karel the Robot for Section-Leader application in Stanford-Code-In-Place.

# Reference

This appendix defines the structure of the Karel programming language on a single page.

## Base Karel commnds:

```py
move()
turn_left()
put_beeper()
pick_beeper()
```

## Karel program structures:

```py
# Comments can be included in any part
# of a program. They start with a #
# and include the rest of the line.

def main() :
   code to execute

declarations of other functions
```

## Names of the conditions:

```py
front_is_clear()
beepers_present()
beepers_in_bag()
left_is_clear()
right_is_clear()
facing_north()
facing_south()
facing_east()
facing_west()
front_is_blocked() no_beepers_present()
no_beepers_in_bag()
left_is_blocked()
right_is_blocked()
not_facing_north()
not_facing_south()
not_facing_east()
not_facing_west()
```

## Conditions:

```py
if condition:
    code run if condition passes

if condition:
    code block for "yes"
else:
    code block for "no"
```

## Loops:

```py
for i in range( count):
    code to repeat

while condition:
    code to repeat
```

## Function Declaration:

```py
defname():
    code in the body of the function.
```

## Extra Karel Commands:

```py
paint_corner(COLOR_NAME)
corner_color_is(COLOR_NAME)
```