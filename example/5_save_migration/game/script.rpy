# The script of the game goes in this file.
# --- Characters ---(not important but good to have them)
define jn = Character("John")
define je = Character("Jane")
define you = Character("You")

define SAVE_VERSION = 4     # defined is not merging with new game version; change value with new update
default save_version = 0    # default is merging with version; but we updating it manually with labels
# The game starts here.

label start:
    
    call okigamelabel
    
    return

# auto-called after any Load/Continue (not on new game start)
# we can modify okigamelabel to call migration after initialization in OkiMVC/main/okigameLabel.rpy
label after_load:
    if save_version < SAVE_VERSION:
        call _migrate
    return

label _migrate:
    if save_version >= SAVE_VERSION:
        return
    if save_version == 0:
        call _update_1
    if save_version == 1:
        call _update_2
    if save_version == 2:
        call _update_3
    if save_version == 3:
        call _update_4
    return

# created in new versions
label _update_1:
    # create new objects here

    $ clickies.add('from_room_to_castle', 'room', 700, 300)  
    $ clickies.add('from_castle_to_room', 'castle', 700, 300)  

    # and update save_version
    $ save_version = 1
    jump _migrate
    return

label _update_2:

    $ save_version = 2
    jump _migrate
    return

label _update_3:

    $ save_version = 3
    jump _migrate
    return

label _update_4:

    $ save_version = 4
    jump _migrate
    return