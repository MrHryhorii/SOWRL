
screen OkiUI():
    
    if not game.store.oki_window:
        use PlaceScreen()
        use UnclicyScreen()
        use ClickyScreen()
        use PersonScreen()
        #
        use WeatherScreen()
    else:
        if game.store.oki_window == 'shop':
            use ShopScreen()
        if game.store.oki_window == 'hints':
            use HintScreen()

    
screen PlaceScreen():
    $ location = game.store.location
    $ day_time = game.store.date['time']
    $ month_day = game.store.date['monthday']

    $ game.puppeteer_controller.process('place', location, day_time, month_day)

    $ item = game.place_controller.get_all_from_location(location)

    if item:
        if item['isActive']:
            $ item['image'] = game.place_controller.get_image(item['arts'], item['use_daypart'])
            add item['image'] xalign item['x'] yalign item['y'] xysize(game.store.game_screen_width, game.store.game_screen_height)


screen UnclicyScreen():
    $ location = game.store.location
    $ day_time = game.store.date['time']
    $ month_day = game.store.date['monthday']

    $ game.puppeteer_controller.process('unclicky', location, day_time, month_day)

    $ items = game.unclicky_controller.get_all_from_location(location)

    if items:
        for i in items:
            if i['isActive']:
                $ i['image'] = game.unclicky_controller.get_image(i['arts'], i['use_daypart'])
                $ img = At(i['image'], Transform(zoom = 1.0, matrixcolor = IdentityMatrix()))

                add img xcenter i['x'] ycenter i['y']


screen ClickyScreen():
    $ location = game.store.location
    $ day_time = game.store.date['time']
    $ month_day = game.store.date['monthday']

    $ game.puppeteer_controller.process('clicky', location, day_time, month_day)

    $ items = game.clicky_controller.get_all_from_location(location)

    if items:
        for i in items:
            if i['isActive']:
                $ i['image'] = game.clicky_controller.get_image(i['arts'], i['use_daypart'])
                $ act = game.clicky_controller.get_action(i['action'])

                $ hover_img = At(i['image'], Transform(zoom = i['scale'], matrixcolor = BrightnessMatrix(i['brightness']) * SaturationMatrix(i['saturation']) * HueMatrix(i['hue'])))
                $ idle_img = At(i['image'], Transform(zoom = 1.0, matrixcolor = IdentityMatrix()))

                imagebutton:
                    hover hover_img
                    idle idle_img
                    focus_mask True
                    xcenter i['x']
                    ycenter i['y']
                    action Function(game._setClickType, "Clicky"), Function(game._setClickBuffer, act)


screen PersonScreen():
    $ location = game.store.location
    $ day_time = game.store.date['time']
    $ month_day = game.store.date['monthday']

    $ game.puppeteer_controller.process('person', location, day_time, month_day)

    $ items = game.person_controller.get_all_from_location(location)

    if items:
        for i in items:
            if i['isActive']:
                $ i['image'] = game.person_controller.get_image(i['arts'], i['use_daypart'])
                $ act = game.person_controller.get_action(i['action'])

                $ hover_img = At(i['image'], Transform(zoom = i['scale'], matrixcolor = BrightnessMatrix(i['brightness']) * SaturationMatrix(i['saturation']) * HueMatrix(i['hue'])))
                $ idle_img = At(i['image'], Transform(zoom = 1.0, matrixcolor = IdentityMatrix()))

                imagebutton:
                    hover hover_img
                    idle idle_img
                    focus_mask True
                    xcenter i['x']
                    ycenter i['y']
                    action Function(game._setClickType, "Person"), Function(game._setClickBuffer, act)


screen LoopScreen():
    if game.clickBuffer != "":
        $ result = game.clickBuffer
        timer 0.01 action Function(game._setClickBuffer, ""), Return (result)


screen HintScreen():
    $ y_slip = game.story_controller.y_slip                      
    $ x_slip = game.story_controller.x_slip
    $ w_slip = game.story_controller.width_slip
    $ string_count = game.story_controller.hint_max_string
    $ t_color = game.shop_controller.text_color
    $ h_outline = game.story_controller.hint_outline
    $ t_outline = game.story_controller.text_outlines
    $ background_image = game.story_controller.hints_background

    $ screen_width  = game.store.game_screen_width
    $ screen_height = game.store.game_screen_height

    $ hints = game.story_controller.get_all_parthints()
    $ hints = game.story_controller.hintlist_to_screen(hints)

    if hints:
        $ pages = game.extra.ceil(len(hints), string_count)
        $ game.story_controller._setPages(pages) # important

    if background_image:
        add background_image xalign 0.5 yalign 0.5 size(screen_width, screen_height)
    else:
        add Solid("#808080", xsize=screen_width, ysize=screen_height)
        
    # Отображаем название магазина
    text 'Цели:' xalign 0.5 yalign 0.05 outlines t_outline color t_color
    # Кнопка - Закрыть магазин
    textbutton "Close" action Function(game._setClickType, "Window"), Function(game._setClickBuffer, "close") xalign 0.5 yalign 0.1 text_outlines t_outline
    # Кнопки - Вперёд и Назад
    if game.story_controller.page < game.story_controller.pages:
        textbutton "Вперед" action Function(game.story_controller._setPage, game.story_controller.page + 1) xalign 0.5 + w_slip yalign 0.1 text_outlines t_outline
    if game.story_controller.page > 1:
        textbutton "Назад"  action Function(game.story_controller._setPage, game.story_controller.page - 1) xalign 0.5 - w_slip yalign 0.1 text_outlines t_outline
    
    if hints:
        $ sorted_strings = game.story_controller.get_strings_for_page(hints)
        vbox xpos x_slip ypos y_slip:
            for string in sorted_strings:
                text string outlines h_outline color t_color

screen ShopScreen():
    $ shop_cfname  = game.store.shop
    $ shop         = game.shop_controller.get(shop_cfname)
    $ money        = game.store.money
    $ money_symbol = game.store.money_symbol

    if shop:
        $ screen_width  = game.store.game_screen_width
        $ screen_height = game.store.game_screen_height
        #
        $ products      = game.product_controller.get_not_buyed_list(shop_cfname)
        $ products      = sorted(products, key=lambda d: (d['price'], d['name']), reverse=False) # сортировка по цене и имени
        #
        $ products_max  = game.shop_controller.max_items
        $ products_slip = game.shop_controller.slip
        $ v_gap         = game.shop_controller.v_gap
        $ h_gap         = game.shop_controller.h_gap
        $ product_x     = game.shop_controller.image_x
        $ product_y     = game.shop_controller.image_y
        $ w_slip        = game.shop_controller.width_slip
        $ t_color       = game.shop_controller.text_color
        $ t_outline     = game.shop_controller.text_outlines
        #
        $ row_sort = game.shop_controller.row_sort
        #
        $ shop['image'] = game.shop_controller.get_image(shop['arts'], shop['use_daypart'])
        # Отображаем фон магазина
        add shop['image'] xalign 0.5 yalign 0.5 size(screen_width, screen_height)

        $ pages = game.extra.ceil(len(products), products_max)
        $ game.shop_controller._setPages(pages) # important

        # Отображаем название магазина
        text 'Shop: ' + shop['name'] xalign 0.5 yalign 0.05 outlines t_outline color t_color
        # Кнопка - Закрыть магазин
        textbutton "Close" action Function(game._setClickType, "Window"), Function(game._setClickBuffer, "close") xalign 0.5 yalign 0.1 text_outlines t_outline
        # Кнопки - Вперёд и Назад
        if game.shop_controller.page < game.shop_controller.pages:
            textbutton "Вперед" action Function(game.shop_controller._setPage, game.shop_controller.page + 1) xalign 0.5 + w_slip yalign 0.1 text_outlines t_outline
        if game.shop_controller.page > 1:
            textbutton "Назад"  action Function(game.shop_controller._setPage, game.shop_controller.page - 1) xalign 0.5 - w_slip yalign 0.1 text_outlines t_outline
        # Выборка ограничего количества товаров
        $ sorted_products = game.shop_controller.get_product_for_page(products)
        # Отображение товара, цены и кнопки - Купить
        # Вертикальное отображение
        if row_sort == 'vertical':
            if sorted_products:
                # значение смещения товара
                $ slip = 0
                for i in sorted_products:
                    $ img = game.product_controller.get_image(i['arts'], i['use_daypart'])
                    # Отображение товара
                    add img xalign 0.5 - w_slip ycenter products_slip + slip xysize(product_x, product_y)
                    if money >= i['price']:
                        # Отображение цены
                        text str(i['price']) + ' ' + money_symbol xalign 0.5 ycenter products_slip + slip outlines t_outline color '#00ff00'
                        # Отображение кнопки - Купить
                        textbutton "Купить" action Function(game.product_controller.buy, shop_cfname, i['cfname'], i['price']) xalign 0.5 + w_slip ycenter products_slip + slip text_outlines t_outline
                    else:
                        # Отображение цены
                        text str(i['price']) + ' ' + money_symbol xalign 0.5 ycenter products_slip + slip outlines t_outline color '#ff0000'
                    # Смещаем следующий товар по высоте
                    $ slip += product_y + v_gap
        # Горизонтальное отображение
        if row_sort == 'horizontal':
            if sorted_products:
                # значение смещения товара
                $ slip = 0
                hbox xalign 0.5 ypos products_slip:
                    for i in sorted_products:
                        $ img = game.product_controller.get_image(i['arts'], i['use_daypart'])
                        vbox xsize product_x + h_gap:
                            # Отображение товара
                            add img xysize(product_x, product_y) xalign 0.5
                            if money >= i['price']:
                                # Отображение цены
                                text str(i['price']) + ' ' + money_symbol outlines t_outline xalign 0.5 yoffset v_gap color '#00ff00'
                                # Отображение кнопки - Купить
                                textbutton "Купить" action Function(game.product_controller.buy, shop_cfname, i['cfname'], i['price']) xalign 0.5 yoffset v_gap*2 text_outlines t_outline
                            else:
                                # Отображение цены
                                text str(i['price']) + ' ' + money_symbol outlines t_outline xalign 0.5 yoffset v_gap color '#ff0000'
        # Отображаем деньги
        text 'Money: ' + str(money) + ' ' + money_symbol xalign 0.5 yalign 0.95 outlines t_outline color t_color
    else:
        timer 0.01 action Function(game._setClickType, "Shop"), Function(game._setClickBuffer, "close")


###########################################

screen WeatherScreen():
    if game.store.weather:
        $ location = game.store.location
        for weather in game.store.weather.values():
            if weather['isActive']:
                if not isinstance(weather['location'], list):
                    $ weather['location'] = [weather['location']]
                if location in weather['location']:
                    $ weather['image'] = game.weather_controller.get_image(weather['arts'], weather['use_daypart'])
                    if weather['items']:
                        for i in weather['items']:
                            $ x             = i['x']
                            $ y             = i['y']
                            $ xstart        = i['xstart']
                            $ ystart        = i['ystart']
                            $ xend          = i['xend']
                            $ yend          = i['yend']
                            $ speedfrompos  = i['speedfrompos']
                            $ speedtopos    = i['speedtopos']
                            $ zoomstart     = i['zoomstart']
                            $ zoom_default  = i['zoom']
                            $ zoomend       = i['zoomstart']
                            $ rot           = i['rotate']
                            
                            add weather['image'] xpos x ypos y at oki_weather(xstart, ystart, x, y, xend, yend, speedfrompos, speedtopos, zoomstart, zoom_default, zoomend, rot)

