label okiinit:  # this label initialize game resources (important to have it)
    # create few locations
    $ places.add('Village', 'village')      # create location with name "Village" and location id "village"
    $ places.add('Forest', 'forest')

    # set starting location
    $ places.set_location('village')

    # create few clickable objects
    $ clickies.add('radio_to_forest', 'village', 600, 100)     # create clickable object with sprite and label "radion" in location with id "village"
    $ clickies.add('radio_to_village', 'forest', 900, 100)      # clickable object in location "forest"

    # weather
    $ weather.add("greenleaf", intensity=20, xforce=30, yforce=30, rot=False, arts="leaf_green") # "rot" rotates sprite to direction; "arts" - custom sprite
    $ weather.set("greenleaf", "location", ["forest"])   # set locations
    $ weather.set("greenleaf", "isActive", True)         # Activate the effect

    $ weather.add("dandelion", intensity=10, xforce=45, yforce=30, rot=False) # "rot" rotates sprite to direction; we will use default; we do not have folder "dandelion"
    $ weather.set("dandelion", "location", ["forest"])   # set locations
    $ weather.set("dandelion", "isActive", True)         # Activate the effect

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
