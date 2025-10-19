label okiinit:  # this label initialize game resources (important to have it)
    # create few locations
    $ places.add('Village', 'village')      # create location with name "Village" and location id "village"
    $ places.add('Forest', 'forest')

    # set starting location
    $ places.set_location('village')
    
    # create few clickable objects
    $ clickies.add('radio_to_forest', 'village', 600, 100)     # create clickable object with sprite and label "radion" in location with id "village"
    $ clickies.add('radio_to_village', 'forest', 900, 100)      # clickable object in location "forest"

    return  # label's end

### You do not need create all labels inside this file ###
### And always close your labels with "return"

# for clickable objects we have to use prefix "clicky_" + id name for object
# we setting logic on click up
label clicky_radio_to_forest:
    $ game.Scene()
    $ places.go_to('forest')
    $ game.noScene(fade)
    return

label clicky_radio_to_village:
    $ game.Scene()
    $ places.go_to('village')
    $ game.noScene(fade)
    return
