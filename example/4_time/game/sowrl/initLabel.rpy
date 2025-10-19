label okiinit:  # this label initialize game resources (important to have it)
    # create few locations
    $ places.add('Village', 'village')      # create location with name "Village" and location id "village"
    $ places.add('Forest', 'forest')

    # set starting location
    $ places.set_location('village')

    # create few clickable objects
    $ clickies.add('radio_to_forest', 'village', 600, 100)     # create clickable object with sprite and label "radion" in location with id "village"
    $ clickies.add('radio_to_village', 'forest', 900, 100)      # clickable object in location "forest"

    $ clickies.add('time', 'village', 100, 650) 

    # weather
    $ weather.add("greenleaf", intensity=20, xforce=30, yforce=30, rot=False, arts="leaf_green") # "rot" rotates sprite to direction; "arts" - custom sprite
    $ weather.set("greenleaf", "location", ["forest"])   # set locations
    $ weather.set("greenleaf", "isActive", True)         # Activate the effect

    $ weather.add("dandelion", intensity=10, xforce=45, yforce=30, rot=False) # "rot" rotates sprite to direction; we will use default; we do not have folder "dandelion"
    $ weather.set("dandelion", "location", ["forest"])   # set locations
    $ weather.set("dandelion", "isActive", True)         # Activate the effect

    # create few characters
    $ persons.add('Jane', 'Doe', 'jane', 'village', 800, 500)   # create character with name "Jane"(Doe) and character id "jane"

    # set character to location with day of week and time
    $ puppeteer.add('person', 'jane', 'w1', 'cleaning', 'village', 500, 500, [1], "06:00-12:00") # 'w1' - random event name
    $ puppeteer.add('person', 'jane', 'p1', 'dancing',  ['forest', 'castle'], 800,350, [1,2,3], "22:00-06:00")

    # set time
    $ date.time_to("08:00")

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

label clicky_time:
    $ d = game.store.date
    $ minute     = d['minute']
    $ hour       = d['hour']
    $ dayMinutes = d['dayMinutes']
    $ time       = d['time']
    $ dayPart    = d['dayPart']
    $ day        = d['day']
    $ monthday   = d['monthday']
    $ weekday    = d['weekday']
    $ weekname   = d['weekname']
    $ week       = d['week']
    $ month      = d['month']
    "Now: day [day], time [time]."

    menu:
        "Add 2 hours":
            $ date.add_hours(2);
            jump clicky_time

        "Change time to 22:00":
            $ date.time_to("22:00")
            jump clicky_time

        "Add 5 days":
            $ date.add_days(5)
            jump clicky_time

        "Exit":
            return
    return


label person_jane:
    if game.store.location == "forest":
        je "I am dancing!"
        return
    je "I am cleaning!"
    return
