init python:

    class OkiWeather:
        def __init__(self):
            self.store = None
            self.dictionary_store = None
            self.extra = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.weather


        # extra:OkiExtra
        def add_extra(self, extra):
            self.extra = extra


        # cfname:str, intensity:int=10, xforce:int=10, yforce:int=50, rot:int or bool=0, arts:str=None
        def add(self, cfname, intensity=10, xforce=10, yforce=50, rot=0, arts=None):
            weather = {
                'name'       : '',
                'cfname'     : cfname,
                'arts'       : cfname,
                'intensity'  : intensity,
                'xforce'     : xforce,
                'yforce'     : yforce,
                'rotate'     : rot,
                'image'      : self.store.default_weather_image_path,
                'items'      : [],
                'location'   : None,
                'isActive'   : False,
                'text'       : '',
                'use_daypart': True
            }
            if arts is not None:
                weather['arts'] = arts

            if intensity <= 0:
                weather['intensity'] = 1
                
            for i in range(weather['intensity']):

                x = renpy.random.randint(0, self.store.game_screen_width)
                y = renpy.random.randint(0, self.store.game_screen_height)

                item = {
                    'xstart'       : x,
                    'ystart'       : y,
                    'x'            : x,
                    'y'            : y,
                    'xend'         : x,
                    'yend'         : y,
                    'speedfrompos' : 5,
                    'speedtopos'   : 5,
                    'zoomstart'    : 1.0,
                    'zoom'         : 1.0,
                    'zoomend'      : 1.0,
                    'rotate'       : rot
                }

                xdis = abs(xforce * 15 / 100)
                ydis = abs(yforce * 15 / 100)
                sc   = 128

                xch = renpy.random.randint(xforce - xdis, xforce + xdis)
                ych = renpy.random.randint(yforce - ydis, yforce + ydis)

                zoomstart = float(renpy.random.randint(85, 115)) / 100
                zoomend   = float(renpy.random.randint(85, 115)) / 100

                if abs(yforce) >= abs(xforce):
                    if yforce > 0:
                        item['ystart']        = -sc
                        item['yend']          = self.store.game_screen_height + sc
                    if yforce < 0:
                        item['ystart']        = self.store.game_screen_height + sc
                        item['yend']          = -sc

                    if xforce != 0:
                        item['xstart']        = item['x'] - self.extra.distance(item['y'], item['ystart']) * xch / 100
                        item['xend']          = item['x'] + (self.extra.distance(item['x'], item['xstart']) * self.extra.distance(item['y'], item['yend']) / 
                                                self.extra.distance(item['y'], item['ystart'])) * (xforce/abs(xforce))

                    if yforce != 0:
                        item['speedtopos']    = round(abs(self.extra.distance2D(item['x'], item['y'], item['xstart'], item['ystart'])/ych), 2)
                        item['speedfrompos']  = round(abs(self.extra.distance2D(item['x'], item['y'], item['xend'], item['yend'])/ych), 2)
                        #
                        k      = (zoomend - zoomstart) / (item['yend'] - item['ystart'])
                        b      = ((item['yend'] * zoomstart) - (zoomend * item['ystart'])) / (item['yend'] - item['ystart'])
                        zoomXY = k * item['y'] + b

                        item['zoomstart']     = zoomstart
                        item['zoom']          = round(zoomXY, 2) # находим зум словно это часть координат
                        item['zoomend']       = zoomend 
                    #
                else:   
                    if xforce > 0:
                        item['xstart']        = -sc
                        item['xend']          = self.store.game_screen_width + sc
                    if xforce < 0:
                        item['xstart']        = self.store.game_screen_width + sc
                        item['xend']          = -sc

                    if yforce != 0:
                        item['ystart']        = item['y'] - self.extra.distance(item['x'], item['xstart']) * ych / 100
                        item['yend']          = item['y'] + (self.extra.distance(item['y'], item['ystart']) * self.extra.distance(item['x'], item['xend']) / 
                                                self.extra.distance(item['x'], item['xstart'])) * (yforce/abs(yforce))

                    if xforce != 0:
                        item['speedtopos']    = round(abs(self.extra.distance2D(item['x'], item['y'], item['xstart'], item['ystart'])/xch), 2)
                        item['speedfrompos']  = round(abs(self.extra.distance2D(item['x'], item['y'], item['xend'], item['yend'])/xch), 2)
                        #
                        k      = (zoomend - zoomstart) / (item['xend'] - item['xstart'])
                        b      = ((item['xend'] * zoomstart) - (zoomend * item['xstart'])) / (item['xend'] - item['xstart'])
                        zoomXY = k * item['x'] + b

                        item['zoomstart']     = zoomstart
                        item['zoom']          = round(zoomXY, 2) # находим зум словно это часть координат
                        item['zoomend']       = zoomend 
                    #

                # формула нахождения У-точки на прямой 
                # k = (y2-y1)/(x2-x1)
                # b = ((x2*y1)-(y2*x1))/(x2-x1)
                # y = k*x+b

                # rotate
                if isinstance(rot, bool):
                    if xforce or yforce != 0:
                        if rot:
                            item['rotate'] = round(self.extra.arccos(self.extra.cos2D(0, 100, xch, ych)), 2)
                            if xch >= 0:
                                item['rotate'] = item['rotate'] * -1
                        else:
                            item['rotate'] = 0
                    else:
                        item['rotate'] = 0
              
                weather['items'].append(item)
            #
            self.dictionary_store[cfname] = weather


        # cfname:str
        # вернёт dict или False
        def get(self, cfname):
            dictionary = self.get_all()
            output = False 
            try:
                output = dictionary[cfname]
            finally:
                return output


        # вернёт dict или False
        def get_all(self):
            output = self.dictionary_store
            if output:
                return output
            else:
                return False


        # cfname:str
        def remove(self, cfname):
            dictionary = self.get_all()
            try:
                del dictionary[cfname]
            finally:
                return
