label okiinit:

    $ places.add('Village', 'village')      # create location with name "Village" and location id "village"
    $ places.add('Forest', 'forest')        # forest location
    $ places.add('Castle', 'castle')        # castle location
    $ places.add('Room', 'room')            # castle location

    $ persons.image_type = 'png'            # no need to set "png", "png" is default 

    $ persons.add('Jane', 'Doe', 'jane', 'village', 800, 500)   # create character with name "Jane"(Doe) and character id "jane"
    $ persons.add('John', 'Doe', 'john', 'village', 200, 500)   # character "John"

    $ clickies.add('radio', 'room', 600, 100)           # create clickable object with sprite and label "radion" in location with id "room"
    $ clickies.add('hollowRadio', 'village', 900, 100)  # clickable object in location "village"
    return

# for clickable objects we have to use prefix "clicky_" + id name for object
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