label okiinit:  # this label initialize game resources (important to have it)
    # create few locations
    $ places.add('Village', 'village')      # create location with name "Village" and location id "village"
    $ places.add('Forest', 'forest')        # forest location
    $ places.add('Castle', 'castle')        # castle location
    $ places.add('Room', 'room')            # castle location

    #$ persons.image_type = 'png'            # no need to set "png", "png" is default 
    # create few characters
    $ persons.add('Jane', 'Doe', 'jane', 'village', 800, 500)   # create character with name "Jane"(Doe) and character id "jane"
    $ persons.add('John', 'Doe', 'john', 'village', 200, 500)   # character "John"
    # create few clickable objects
    $ clickies.add('radio', 'room', 600, 100)           # create clickable object with sprite and label "radion" in location with id "room"
    $ clickies.add('hollowRadio', 'village', 900, 100)  # clickable object in location "village"

    # create some variables
    $ machine.add('isJohn', "false")
    $ machine.add('isJane', "false")
    $ machine.add('firstTimeVillage', False)

    # create triggers
    # create event on trigger with a name "event_1" and call label with a name "event_1_label"
    $ triggers.add(
        "event_1",                                                                  # random name
        "machine.get('isJohn') == 'true' and machine.get('isJane') == 'true'",      # condition
        "renpy.call('event_1_label')"                                               # what to do
    )

    $ triggers.add(
        "event_2",                                                                  
        "places.get_location() == 'village' and not machine.get('firstTimeVillage')",      
        "renpy.call('village_hub')"                                               
    )

    return  # label's end

### You do not need create all labels inside this file ###

# for clickable objects we have to use prefix "clicky_" + id name for object
# we setting logic on click up
label clicky_radio:
    $ game.Scene()
    $ places.go_to('village')
    $ game.noScene(pixellate)
    return

label clicky_hollowRadio:
    $ game.Scene()
    $ places.go_to('room')
    $ game.noScene(fade)
    return

# John talk: first vs repeat
label person_john:
    # First time
    if machine.get("isJohn") == "false":
        $ machine.set("isJohn", "true")
        jn "Road's muddy. If you're wise, you ask Jane before stepping further."
        jn "She knows which paths bite back."
        return

    # Repeat (short)
    jn "Jane's by the well. Don't keep her waiting."
    return

# Jane talk: first vs repeat
label person_jane:
    if machine.get("isJane") == "false":
        $ machine.set("isJane", "true")
        je "So John sent you. Good. Hear me once: pack dry tinder."
        je "And keep your eyes above the roots; the forest likes to trip fools."
        return

    je "Tinder, water, knife. Then talk."
    return


# first time in the village
label village_hub:
    you "Meet John and Jane first. They'll keep you out of the mud."
    $ machine.set('firstTimeVillage', True)
    return

# triggered event if we met Jane and John
label event_1_label:
    you "I prepered to go to forest"
    return

# first time in the forest
label forest_entry:
    you "Cold air. Wet bark. Let's keep our steps light."
    return