screen Schedule(kind, cfname, puppet_item):
    $ h_size = game.store.game_screen_height
    $ fixed_height = 0
    $ slide_height = 190
    $ slide_days = 220
    $ count_slide = 0

    $ date = game.store.date
    $ puppet = game.puppeteer_controller.get(kind, cfname)
    $ sorted_list = []
    $ day_list = []

    if puppet:
        $ not_sorted_list = puppet.values() 
        $ sorted_list = sorted(not_sorted_list, key=lambda d: (game.extra.start_minutes_from_interval(d['interval']), game.extra.end_minutes_from_interval(d['interval']), d['status'], d['id']), reverse=False) 
        #
        for days in sorted_list:
            for day in days['day']:
                $ day_list.append(day)
        if day_list:
            $ count_slide += len(day_list) 
            #
            $ day_list = list(set(day_list)) # remove dublicates
            $ day_list = sorted(day_list)
        
    $ fixed_height = (count_slide * slide_height) + slide_days + 100
    if fixed_height < h_size:
        $ fixed_height = h_size

    frame:
        background Solid("#808080")
        viewport id "vp":
            mousewheel True
            draggable True
            if fixed_height > h_size:
                scrollbars 'vertical'
            
            fixed ysize fixed_height:
                vbox xalign 0.5:
                    if puppet_item:
                        $ i_name = puppet_item['name']
                        $ i_cfname = puppet_item['cfname']
                        $ i_arts = puppet_item['arts']
                        $ i_location = puppet_item['location']
                        text '===============' xalign 0.5 outlines [ (1, "#000", 0, 0) ]
                        text 'name: ' + i_name outlines [ (1, "#000", 0, 0) ]
                        text 'cfname: ' + i_cfname outlines [ (1, "#000", 0, 0) ]
                        text 'month day: ' + str(date['monthday']) outlines [ (1, "#000", 0, 0) ]
                        text 'time: ' + date['time'] outlines [ (1, "#000", 0, 0) ]
                        text 'location: ' + game.extra.list_to_string(i_location, ', ') outlines [ (1, "#000", 0, 0) ]
                        text '===============' xalign 0.5 outlines [ (1, "#000", 0, 0) ]

                textbutton 'Close' action Function(renpy.hide_screen, 'Schedule') xalign 0.5 ypos 170 text_outlines [ (3, "#000", 0, 0), (2, "#fff", 0, 0) ] 

                if day_list:
                    vbox xalign 0.5 ypos slide_days:  
                        for day in day_list:
                            
                            vbox xalign 0.5:
                                if day == date['day']:
                                    text 'Day' + ' : ' + str(day) outlines [ (3, "#000", 0, 0), (2, "#fff", 0, 0) ] xalign 0.5 color '#00ff00'
                                else:
                                    text 'Day' + ' : ' + str(day) outlines [ (3, "#000", 0, 0), (2, "#fff", 0, 0) ] xalign 0.5 

                                for p in sorted_list:
                                    if day in p['day']:
                                        $ color_text = "#fff"
                                        if p['isActive']:
                                            if game.date_controller.is_in_interval(date['time'], p['interval']) and puppet_item['location'] == p['location'] and day == date['day']:
                                                $ color_text = "#00ff00"
                                            elif game.date_controller.is_in_interval(date['time'], p['interval']) and day == date['day']:
                                                $ color_text = "#ffff00"
                                            else:
                                                $ color_text = "#fff"
                                        else:
                                            $ color_text = "#808080"

                                        text 'interval: ' + p['interval'] outlines [ (1, "#000", 0, 0) ] color color_text
                                        text 'status: ' + p['status'] outlines [ (1, "#000", 0, 0) ] color color_text
                                        text 'id: ' + p['id'] outlines [ (1, "#000", 0, 0) ] color color_text
                                        text 'arts: ' + p['arts'] outlines [ (1, "#000", 0, 0) ] color color_text
                                        text 'location: ' + game.extra.list_to_string(p['location'], ', ') outlines [ (1, "#000", 0, 0) ] color color_text
                                        text '===============' xalign 0.5 outlines [ (1, "#000", 0, 0) ]
