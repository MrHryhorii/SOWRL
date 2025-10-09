default game = OkiMaster()
# default extra = game.extra
default places = game.place_controller 
default clickies = game.clicky_controller
default unclickies = game.unclicky_controller
default date = game.date_controller
default persons = game.person_controller
default products = game.product_controller
default shops = game.shop_controller
default story = game.story_controller
default machine = game.machine_controller
default triggers = game.trigger_controller
default weather = game.weather_controller
default puppeteer = game.puppeteer_controller

label okigamelabel:
    
    define config.gl2 = True # As of Ren'Py 7.4 (late 2020), Model-Based rendering needs to be enabled to be used. This is done by setting config.gl2 to True
    
    call okiinit # использовать ярлык на код, где происходит начальная инициализация мира

    $ game.Start()
    # цикл игры
    while game.playing:                          
        window hide                              # убираем пустое окно
        $ game.refreshScreen()                   # обновляем ожидание клика
        $ print(str(game.clickType) +":"+ str(game.clickAction)) # for debug
        $ triggers.click()                       # проверка триггера на клик
        # проверка, был ли клик clicky-объекта
        if game.clickType == "Clicky": 
            if game.clickAction:                 # проверка наличия действия
                call expression game.clickAction # выполняем действия
        # проверка, был ли клик person-объекта
        if game.clickType == "Person": 
            if game.clickAction:                 # проверка наличия действия  
                call expression game.clickAction # выполняем действия
        # проверка, закрытия окна
        if game.clickType == "Window":
            #
            $ window_type = game.store.oki_window
            #
            if game.clickAction == "close":
                $ game.ScreenshotScene()
                $ game.store.oki_window = ''
                if game.store.transition is not None:
                    $ renpy.with_statement(game.store.transition, True)
            #
            if window_type == 'shop':
                $ game.store.shop = ''            # сбросим магазин
                $ game.shop_controller.page = 1   # сбросим страницу

            if window_type == 'hints':
                $ game.story_controller.page = 1  # сбросим страницу

        #
        $ triggers.process()                     # проверка всех условий для триггеров
    return

label no_label:
    'Нет действия!'
    return

transform oki_matrix(from_matrix, to_matrix, timepiece=0.5):
    matrixcolor OkiColorMatrix(from_matrix)
    linear timepiece matrixcolor OkiColorMatrix(to_matrix)

transform oki_weather(xstart, ystart, x, y, xend, yend, speedfrompos, speedtopos, zoomstart, zoom_default, zoomend, rot):
    subpixel True
    around (.5, .5) 
    alignaround (.5, .5) 
    xalign .5 
    yalign .5
    rotate rot

    parallel:
        zoom zoom_default
        linear speedfrompos zoom zoomend
        zoom zoomstart
        linear speedtopos zoom zoom_default
        repeat

    parallel:
        xcenter x
        linear speedfrompos xcenter xend
        xcenter xstart
        linear speedtopos xcenter x
        repeat
    
    parallel:
        ycenter y
        linear speedfrompos ycenter yend
        ycenter ystart
        linear speedtopos ycenter y
        repeat

