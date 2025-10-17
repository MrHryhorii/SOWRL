init python:

    class OkiWeatherController:
        def __init__(self):
            self.model = None
            self.image_type = 'png'


        # model:OkiWeather
        def add_model(self, model):
            self.model = model


        # cfname:str, intensity:int=10, xforce:int=10, yforce:int=50, rot:int or bool=0, arts:str=None
        def add(self, cfname, intensity=10, xforce=10, yforce=50, rot=0, arts=None):
            self.model.add(cfname, intensity, xforce, yforce, rot, arts)


        # cfname:str, keyname:str, val:any
        def set(self, cfname, keyname, val):
            dictionary = self.model.get(cfname)
            if dictionary:
                if keyname in dictionary:
                    dictionary[keyname] = val


        # cfn:str, keyname:str=None
        def get(self, cfn, keyname=None):
            dictionary = self.model.get(cfn)
            if keyname is not None:
                output = False
                try:
                    output = dictionary[keyname]
                finally:
                    return output
            return dictionary


        # obj_arts:str, dp:int or bool
        # вернёт str
        def get_image(self, obj_arts, dp=True):
            simple = False
            if isinstance(dp, bool):
                if dp:
                    dp = self.model.store.date['dayPart']
                else:
                    simple = True

            day_part = dp
            art = obj_arts

            folder = self.model.store.weather_folder_path
            default_image = self.model.store.default_weather_image_path

            if not simple:
                file_path = folder + '/' + art + '/' + art + '_' + str(day_part) + '.' + self.image_type
                if renpy.loadable(file_path):
                    return file_path
                else:
                    while day_part > 0:
                        day_part -= 1
                        file_path = folder + '/' + art + '/' + art + '_' + str(day_part) + '.' + self.image_type
                        if renpy.loadable(file_path):
                            return file_path
                    else:
                        simple = True
            
            if simple:
                file_path = folder + '/' + art + '/' + art  + '.' + self.image_type
                if renpy.loadable(file_path):
                    return file_path
                else:
                    return default_image


        # cfn:str=None
        def update(self, cfn=None):
            if self.model.dictionary_store:

                def upd():
                    cfname = weather['cfname']
                    intensity = weather['intensity']
                    xforce = weather['xforce']
                    yforce = weather['yforce']
                    rot = weather['rotate']
                    arts = weather['arts']
                    #
                    location = weather['location']
                    isActive = weather['isActive']
                    name = weather['name']
                    text_ = weather['text']
                    use_daypart = weather['use_daypart']
                    #
                    self.add(cfname, intensity, xforce, yforce, rot, arts)
                    #
                    self.set(cfname, 'location', location)
                    self.set(cfname, 'isActive', isActive)
                    self.set(cfname, 'name', name)
                    self.set(cfname, 'text', text_)
                    self.set(cfname, 'use_daypart', use_daypart)

                if cfn is None:
                    for weather in self.model.dictionary_store.values():
                        if weather['isActive']:
                            upd()
                else:   
                    weather = self.model.get(cfn)
                    if weather:  
                        if weather['isActive']: 
                            upd()


        # cfname:str, dp:int=None
        def show(self, cfname, dp=True, transition=None):
            weather = self.model.get(cfname)
            if weather:
                weather['image'] = self.get_image(weather['arts'], dp)
                img = weather['image']
                if weather['items']:
                    n = 0
                    for i in weather['items']:
                        #
                        x = i['x']
                        y = i['y']
                        xstart = i['xstart']
                        ystart = i['ystart']
                        xend = i['xend']
                        yend = i['yend']
                        speedfrompos = i['speedfrompos']
                        speedtopos = i['speedtopos']
                        zoomstart = i['zoomstart']
                        zoom_default = i['zoom']
                        zoomend = i['zoomstart']
                        rot = i['rotate']
                        #
                        n += 1
                        #
                        tr = oki_weather(xstart, ystart, x, y, xend, yend, speedfrompos, speedtopos, zoomstart, zoom_default, zoomend, rot) 
                        renpy.show(cfname + '_' + str(n), at_list=[tr], what=renpy.displayable(img))
                    if transition is not None:
                        renpy.with_statement(transition)

        
        def hide(self, cfname, transition=None):
            weather = self.model.get(cfname)
            if weather:
                if weather['items']:
                    n = 0
                    for i in weather['items']:
                        n += 1
                        renpy.hide(cfname + '_' + str(n))
                    if transition is not None:
                        renpy.with_statement(transition)
