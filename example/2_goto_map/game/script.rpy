# The script of the game goes in this file.
# --- Characters ---(not important but good to have them)
define jn = Character("John")
define je = Character("Jane")
define you = Character("You")
# The game starts here.

label start:

    call okigamelabel
    $ places.set_location('room')   # set starting location

    return