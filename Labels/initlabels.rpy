label okiinit:

    $ places.add('Комната', 'room')
    $ puppeteer.add('place', 'room', 's1', 'snow', 'room', 0.5, 0.5, 2, "08:00-18:00")
    $ puppeteer.add('place', 'room', 's2', 'snow', 'room', 0.5, 0.5, 2, "18:00-00:00", 'room')
    $ places.add('Больница','hospital')

    $ clickies.add('clock_64', ['room', 'hospital', 'beach', 'park', 'bar'], 100, 100)
    $ clickies.add('info', ['room', 'hospital', 'beach'], 200, 100)
    $ clickies.add('to_room', 'hospital', 300, 100)
    $ clickies.add('to_hospital', 'room', 300, 100)
    $ clickies.add('show_scene_1', 'room', 500, 100)
    $ clickies.add('show_scene_2', 'hospital', 500, 100)

    $ clickies.add('openshop', 'hospital', 900, 100)

    $ clickies.add('to_map', ['room', 'hospital', 'park', 'beach', 'bar', 'market'], 1100, 300)

    $ clickies.add('worldmap_to_room', 'worldmap', 100, 100)
    $ clickies.set('worldmap_to_room', 'action', 'clicky_to_room')
    $ clickies.add('worldmap_to_hospital', 'worldmap', 200, 100)
    $ clickies.set('worldmap_to_hospital', 'action', 'clicky_to_hospital')
    $ clickies.add('worldmap_to_park', 'worldmap', 300, 100)
    $ clickies.set('worldmap_to_park', 'action', 'clicky_to_park')
    $ clickies.add('worldmap_to_beach', 'worldmap', 400, 100)
    $ clickies.set('worldmap_to_beach', 'action', 'clicky_to_beach')
    $ clickies.add('worldmap_to_bar', 'worldmap', 500, 100)
    $ clickies.set('worldmap_to_bar', 'action', 'clicky_to_bar')
    $ clickies.add('worldmap_to_market', 'worldmap', 600, 100)
    $ clickies.set('worldmap_to_market', 'action', 'clicky_to_market')

    $ clickies.add('show_statuses_room', 'show_statuses', 'room', 900, 100)

    $ persons.image_type = 'jpg'
    $ persons.add('Jane', 'Doe', 'jane', 'room', 500, 500)
    $ puppeteer.add('person', 'jane', 'w1', 'working', 'hospital', 500, 500, [1], "06:00-12:00")
    $ puppeteer.add('person', 'jane', 'w2', 'working', 'hospital', 500, 500, [1,5], "14:00-16:00")
    $ puppeteer.add('person', 'jane', 's1', 'sleeping', 'room', 300, 350, [1,2,3], "22:00-05:00")
    $ puppeteer.add('person', 'jane', 'p1', 'playing', ['beach', 'bar'], 800, 350, [1,2,3], "22:00-06:00")

    $ puppeteer.add('person', 'jane', 'p2', 'playing', ['beach', 'bar'], 800, 350, [1,6,7], "22:00-06:00")
    $ puppeteer.set('person', 'jane', 'p2', 'isActive', False)

   

    $ shops.add('Jizz', 'jizz')

    $ products.add('Product 00000000000000000000000000000', 'product0', 'jizz', 3001)
    $ products.add('Product 1', 'product1', 'jizz', 3001)
    $ products.add('Product 2', 'product2', 'jizz', 3002)
    $ products.add('Product 3', 'product3', 'jizz', 3003)
    $ products.add('Product 4', 'product4', 'jizz', 3004)
    $ products.add('Product 5', 'product5', 'jizz', 3005)
    $ products.add('Product 6', 'product6', 'jizz', 3006)
    $ products.add('Product 7', 'product7', 'jizz', 3007)
    $ products.add('Product 8', 'product8', 'jizz', 3008)
    $ products.add('Product 9', 'product9', 'jizz', 3009)
    $ products.add('Product 10', 'product10', 'jizz', 3001)
    $ products.add('Product 11', 'product11', 'jizz', 3002)
    $ products.add('Product 12', 'product12', 'jizz', 3003)
    $ products.add('Product 13', 'product13', 'jizz', 3004)
    $ products.add('Product 14', 'product14', 'jizz', 3005)
    $ products.add('Product 15', 'product15', 'jizz', 3006)
    $ products.add('Product 16', 'product16', 'jizz', 3007)
    $ products.add('Product 17', 'product17', 'jizz', 3008)

    

    $ date.do_in('a1', "renpy.call_in_new_context('event_1')", 1440, 'minutes')
    $ date.do_in('a2', "renpy.call_in_new_context('event_2')", 1440 + 240 + 60, 'minutes')
    $ date.do_at('a3', "renpy.call_in_new_context('event_1')", '16:00')
    $ date.do_at('a4', "renpy.call_in_new_context('event_1')", '16:00', 2)
    $ date.do_in('a5', "renpy.call_in_new_context('event_3')", 10, 'hours')
    $ date.do_in('a6', "renpy.call_in_new_context('event_3')", 3, 'days')

    $ story.add('Сюжет 1', 'plot 01')
    $ story.add('Сюжет 2', 'plot 02')
    $ story.set_part('plot 01', 1)
    $ story.enable('plot 01')
    $ story.set_part('plot 02', 1)
    $ story.enable('plot 02')

    $ story.set_parthint('plot 01', 1, 'Встретиться с Билли в парке')
    $ story.set_parthint('plot 01', 2, 'Еще раз встретиться с Билли в парке')

    $ story.set_parthint('plot 02', 1, 'Встретиться с Дилли на пляже')
    $ story.set_parthint('plot 02', 2, 'Еще раз встретиться с Дилли на пляже')

    $ triggers.add("Trigger_plot_2", "game.clickType == 'Person' and game.clickAction == 'person_dilly'", "story.set_part('plot 02', 2)"  )


    $ story.add('Сюжет 3', 'plot 03')
    $ story.set_part('plot 03', 1)
    $ story.enable('plot 03')
    $ story.set_parthint('plot 03', 1, 'Test for 3: Lacinia auctor natoque sem torquent dictumst curabitur consequat nulla, nec rutrum in risus fringilla eleifend. Euismod montes lobortis phasellus commodo aliquam efficitur viverra fames iaculis maximus platea leo vivamus, sociosqu ultricies quis aptent lacinia scelerisque neque faucibus proin praesent congue')

    $ story.add('Сюжет 4', 'plot 04')
    $ story.set_part('plot 04', 1)
    $ story.enable('plot 04')
    $ story.set_parthint('plot 04', 1, 'Проверка наличия одинакового слова: пляж трололо пляж пляж пляж')
    

    ###
    $ places.add('Карта', 'worldmap')
    $ places.add('Парк',  'park')
    $ places.add('Пляж',  'beach')
    $ places.add('Бар',   'bar')
    $ places.add('Рынок', 'market')

    $ unclickies.add('first_unclicky', 'worldmap', 500, 500)

    $ persons.add('Billy', 'Doe', 'billy', 'park', 500, 500)
    $ puppeteer.add('person', 'billy', 'p1', 'playing', 'park', 500, 500, [1,2,3,4,5,6,7,8,9,10], "08:00-18:00")
    $ puppeteer.add('person', 'billy', 'd1', 'drinking', 'bar', 500, 500, [1,2,3,4,5,6,7,8,9,10], "18:00-00:00")
    $ puppeteer.add('person', 'billy', 's1', 'sleeping', '', 500, 500, [1,2,3,4,5,6,7,8,9,10], "00:00-08:00")

    $ persons.add('Dilly', 'Doe', 'dilly', 'beach', 500, 500)
    #$ puppeteer.add('person', 'dilly', 'w1', 'waiting', 'beach', 500, 500, [1,2,3,4,5,6,7,8,9,10], "00:00-23:59")

    #$ personstatuses.add('billy', 'playing', 'park', [1,2,3,4,5,6,7,8,9,10], "08:00-18:00", 500, 500)
    #$ personstatuses.add('billy', 'drinking', 'bar', [1,2,3,4,5,6,7,8,9,10], "18:00-00:00", 500, 500)

    #$ personstatuses.add('dilly', 'waiting', 'beach', [1,2,3,4,5,6,7,8,9,10], "00:00-23:59", 500, 500)

    $ weather.add('test1', 5, 100, 100, True)
    $ weather.add('test2', 5, -100, -100, True, 'snowflake')

    $ places.set_location('room')

    $ puppeteer.add('clicky', 'info', 's1', 'snow', ['room', 'hospital'], 200, 100, [1,2,3,4,5,6,7,8,9,10], "08:00-18:00")
    $ puppeteer.add('clicky', 'info', 'r1', 'rain', ['room', 'hospital'], 200, 100, [1,2,3,4,5,6,7,8,9,10], "18:00-07:59")

    $ persons.add('Jack', 'Doe', 'jack', 'market', 700, 500)
    $ clickies.add('extra_info', 'market', 200, 100)
    $ clickies.set('extra_info', 'action', 'clicky_info')
    
    return

label person_billy:
    menu:
        "Какая сейчас часть в сюжете 'plot 01'?" if story.get_status('plot 01'):
            $ p = story.get_part('plot 01')
            "Сейчас: [p]."
        "Сколько времени?":
            $ d = game.store.date
            $ t = d['time']
            "Сейчас: [t]!"
        "Давай подождём 2 часа.":
            $ date.add_hours(2)

        "Давай начнём увлекательную историю" if story.get_status('plot 01') == True and story.get_part('plot 01') == 1 and places.get_location() == 'park':
            "И вот началась увлекательная история."
            "Вторая строка увлекательного текста."
            "И еще одна увлекательная строка."
            $ story.part_up('plot 01') # увеличим главу до 2
            $ date.do_at('a7', "renpy.call('task_wait_one_day_billy')", '08:00', 1) # увеличим главу до 3 с отстрочкой
            "Прийди ко мне завтра с утра в парк."

        "Давай продолжем увлекательную историю" if story.get_status('plot 01') == True and story.get_part('plot 01') == 3 and places.get_location() == 'park':
            "Отлично, всё работает."
            $ story.part_up('plot 01')
            $ story.set_partloc('plot 01', 4, ['room', 'hospital'], "renpy.call('plot_01_4_partloc')")
            "Следующая часть истории с билли у бара."

        "Давай продолжем увлекательную историю" if story.get_status('plot 01') == True and story.get_part('plot 01') == 4 and places.get_location() == 'bar':
            "Ты на месте."
            $ story.part_up('plot 01')

        "Созлать новую переменную 'rush'." if not game.store.machine.has_key('rush'): 
            $ machine.add('rush', 5)

        "Значение переменной 'rush'." if game.store.machine.has_key('rush'):
            $ var = game.store.machine['rush']
            "Значение переменной равно: [var]."

        "Созлать новую переменную 'lush'." if machine.get('lush') == False: 
            $ machine.add('lush', 15)

        "Значение переменной 'lush'." if machine.get('lush') != False:
            $ var = machine.get('lush') 
            "Значение переменной равно: [var]."

        "Увеличить значение 'lush'." if machine.get('lush') != False and type(machine.get('lush')) == int:
            $ var = machine.get('lush') 
            $ var += 1
            $ machine.set('lush', var)

        "Пере/создать переменную 'lush'.":
            $ machine.add('lush', 15)

        "Создай триггер":
            $ triggers.add("Триггер для теста", "game.store.money == 12345 and places.get_location() == 'park'", "renpy.say(e, 'Это оно!')")

        "Создай триггер in new context":
            $ triggers.add("Триггер для теста in new context", "game.store.money == 12345", "renpy.call_in_new_context('clicky_info')")

        "Создай пару ярлыков триггеров":
            $ triggers.add("Trigger1", "places.get_location() == 'bar'", "renpy.call('trigger1')" )
            $ triggers.add("Trigger2", "places.get_location() == 'bar'", "renpy.call('trigger2')" )

        "Создай триггер закрытия магазина":
            $ triggers.add("Trigger3", "game.clickType == 'Shop' and game.clickAction == 'close' and game.store.shop == ''" , "e('Триггер из-за из-за клика на Билли')" )

        "Создай триггер клика на себя":
            $ triggers.add("Trigger4", "game.clickType == 'Person' and game.clickAction == 'person_billy'", "renpy.say(e, 'Триггер из-за из-за клика на Билли')\ngame.refreshClick()"  )
            $ game.refreshClick()

        "Триггер?" if len(game.store.triggers) > 0:
            $ triggers.process()

        "Сколько триггеров?" if len(game.store.triggers) > 0:
            $ var = len(game.store.triggers)
            "Триггеров: [var]"

        "Назад":
            $ l = game.store.location
            $ places.set_location(l)
    return

label plot_01_4_partloc:
    "Мне нужно в бар"
    return

label person_dilly:
    menu:
        "Открыть магазин":
            $ shops.open('jizz')
        "Открыть магазин через сцену":
            $ game.Scene()
            $ shops.open('jizz', fade)
            $ game.noScene(fade)
        "Открыть магазин в сцене":
            $ game.Scene()
            "Тестовый текст до магазина"
            # создание триггера после закрытия магазина
            $ triggers.add("shopclosed", "game.clickType == 'Shop' and game.clickAction == 'close' and game.store.shop == ''", "renpy.call_in_new_context('trigger_shopclosed')" )
            $ shops.open('jizz', fade)
            $ game.noScene(fade)
        "Добавить локицию в погоду":
            $ weather.set('test1','location', ['room', 'hospital'])
            $ weather.set('test1','arts', 'rain')
            $ weather.set('test2','location', 'room')
            #
            $ weather.set('test1','isActive', True)
            $ weather.set('test2','isActive', True)
        "Изменить текст в инфо-клики":
            $ clickies.set('info', 'text', 'Set works')
        "Удалить Инфо-клики":
            $ clickies.model.remove('info')
        "Замени стандартную картинку клики":
            $ game.store.default_clicky_image_path = 'images/clickies/ava_png.png'
        "Запуск сцены с погодой":
            call weather_test_label
        "Покажи подсказки":
            $ game.story_controller.show_hints(fade)
        "Назад":
            $ l = game.store.location
            $ places.set_location(l)
    return

label person_jack:
    menu:
        "Сколько времени?":
            $ d = game.store.date
            $ t = d['time']
            "Сейчас: [t]!"
        "Давай подождём 2 часа.":
            $ date.add_hours(2)
        "Перемотать время на 06.00":
            $ date.time_to('06:00')
        "Перемотать время на 12.00":
            $ date.time_to('12:00')
        "Перемотать время на 06.00 + 1 день":
            $ date.time_to('06:00', 1)
        "Проверим открытие магазина в сцене":
            $ game.Scene()
            'Какойто текст 1'
            'Какойто текст 2'
            $ game.store.shop = 'jizz'
            $ renpy.show_screen('ShopScreen')
            #$ game.store.shop = ''
            'Какойто текст 3'
            'Какойто текст 4'
            $ game.noScene(dissolve)
        "Назад":
            $ l = game.store.location
            $ places.set_location(l)
    return

label weather_test_label:
    $ game.Scene()
    'Это сцена без погоды'
    $ weather.show('test1', True, dissolve)
    #$ renpy.with_statement(dissolve)
    'А сейчас эта сцена с погодой'
    'Просто текст'
    'Сейчас спрячем погоду'
    $ weather.hide('test1', dissolve)
    #$ renpy.with_statement(dissolve)
    'Уже без погоды!'
    $ game.noScene(fade)
    return

label trigger_shopclosed:
    $ game.Scene()
    "Тестовый текст после магазина"
    $ game.noScene(fade)
    return

label trigger1:
    "Текст из triger1"
    return

label trigger2:
    "Текст из triger2"
    return

label task_wait_one_day_billy:
    $ story.part_up('plot 01')
    return

label clicky_to_map:
    $ game.Scene()
    $ places.go_to('worldmap')
    $ game.noScene(fade)
    return

label clicky_to_park:
    $ game.Scene()
    $ places.go_to('park')
    $ game.noScene(fade)
    return

label clicky_to_beach:
    $ game.Scene()
    $ places.go_to('beach')
    $ game.noScene(pixellate)
    return

label clicky_to_bar:
    $ game.Scene()
    $ places.go_to('bar')
    $ game.noScene(fade)
    return

label clicky_to_market:
    $ game.Scene()
    $ places.go_to('market')
    $ game.noScene(pixellate)
    return

label clicky_clock_64:
    #$ game.Scene()
    $ date.add_hours(2)
    #$ game.noScene(pixellate)
    return

label clicky_info:
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
    'Часы: [hour], Минуты: [minute], Минуты дня: [dayMinutes], Время: [time], Часть дня: [dayPart], День: [day], День месяца: [monthday], День недели: [weekday], Название дня: [weekname], Неделя: [week], Месяць: [month].'
    return 

label clicky_to_room:
    $ game.Scene()
    $ places.go_to('room')
    $ game.noScene(pixellate)
    return

label clicky_to_hospital:
    $ game.Scene()
    $ places.go_to('hospital')
    $ game.noScene(pixellate)
    return

label clicky_show_scene_1:
    $ game.Scene()
    $ game.FixColorMatrix()
    
    e 'Сейчас сменятся цвета'
    e 'Эта сцена происходит вне экранов!'
    show logo

    $ game.ShowImg('logo', 'images/persons/default.png', 0.3, 0.5) 
    $ renpy.with_statement(pixellate)
    #$ game.FixColorMatrix()
    
    e 'Просто еще одна фраза в сцене.'
    $ places.go_to('hospital')
    e 'Инвертируем экраны'
    $ game.noScene(fade)
    return

label clicky_show_scene_2:
    $ game.Scene()
    'test 1'
    $ game.ColorMatrix(InvertMatrix(), 3, 'all')
    'test 2'
    'test 3'
    $ game.noScene(fade)
    return

label clicky_show_statuses:
    $ game.Scene()
    'test 1'
    'test 2'
    $ game.noScene(pixellate)
    return

label person_jane:
    $ person_jane = game.person.get('jane')
    $ status = person_jane['status']
    $ x = person_jane['x']
    $ y = person_jane['y']
    'Мой статус: [status], x: [x], y: [y]'
    return

label clicky_openshop:
    $ game.Scene()
    $ shops.open('jizz', blinds)
    $ game.noScene(squares)
    return

label event_1:
    $ game.ScreenshotScene()
    'Event 1'
    return

label event_2:
    $ game.ScreenshotScene()
    'Event 2'
    return

label event_3:
    $ game.ScreenshotScene()
    'Event 3'
    #$ game.noScene()
    return