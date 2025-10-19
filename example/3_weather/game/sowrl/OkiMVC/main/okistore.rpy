init python:

    class OkiStore:
        def __init__(self):
            self.date      = {}
            self.timetasks = {}
            self.places    = {}
            self.clickies  = {}
            self.unclickies= {}
            self.persons   = {}
            self.products  = {}
            self.shops     = {}
            self.stories   = {}
            self.triggers  = {}

            self.machine   = {}
            self.weather   = {}

            self.puppets   = {}

            self.location  = ''
            self.nowhere   = ['']
            
            self.shop      = ''
            self.money     = 18345
            self.money_symbol = '\u20B4'

            self.oki_window = ''
            self.transition = None

            self.colormatrix  = None

            self.weekdayNames = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
            self.dayPartsList = [[0,0],[2,0],[4,0],[6,0],[8,0],[10,0],[12,0],[14,0],[16,0],[18,0],[20,0],[22,0]]
            self.dateLimits   = {
                'hour'    : [0, 23],
                'minute'  : [0, 59],
                'monthday': [1, 28],
                'weekday' : [1, 7],
                'week'    : [1, 4]
            }

            self.game_screen_width     = config.screen_width
            self.game_screen_height    = config.screen_height
            self.imageNotificationPath = False

            self.place_folder_path = 'images/places'
            self.default_place_image_path = 'images/places/default.jpg'
            self.clicky_folder_path = 'images/clickies'
            self.default_clicky_image_path = 'images/clickies/default.png'
            self.unclicky_folder_path = 'images/unclickies'
            self.default_unclicky_image_path = 'images/unclickies/default.png'
            self.person_folder_path = 'images/persons'
            self.default_person_image_path = 'images/persons/default.png'
            self.product_folder_path = 'images/products'
            self.default_product_image_path = 'images/products/default.png'
            self.shop_folder_path = 'images/shops'
            self.default_shop_image_path = 'images/shops/default.jpg'
            #
            self.weather_folder_path = 'images/weather'
            self.default_weather_image_path = 'images/weather/default.png'

            self.default_label = 'no_label'