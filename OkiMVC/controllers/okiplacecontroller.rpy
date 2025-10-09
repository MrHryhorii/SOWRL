init python:

    class OkiPlaceController:
        def __init__(self):
            self.model = None
            self.image_type = 'jpg'


        # model:OkiPlace
        def add_model(self, model):
            self.model = model


        # name:str, cfname:str, arts:str = None
        def add(self, name, cfname, arts=None):
            self.model.add(name, cfname, arts)


        # cfname:str, keyname:str
        # вернёт dict or False or keyname value
        def get(self, cfname, keyname=None):
            dictionary = self.model.get(cfname)
            if keyname is not None:
                output = False 
                try:
                    output = dictionary[keyname]
                finally:
                    return output
            return dictionary


        # cfname:str, keyname:str, val:any
        def set(self, cfname, keyname, val):
            dictionary = self.model.get(cfname)
            if dictionary:
                if keyname in dictionary:
                    dictionary[keyname] = val


        # location:str
        # вернёт dict or False
        def get_all_from_location(self, location=''):
            dictionary = self.model.get(location)
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

            folder = self.model.store.place_folder_path
            default_image = self.model.store.default_place_image_path

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


        # location:str
        def go_to(self, location):
            loc = self.model.get(location)
            if loc:
                stories = self.model.store.stories
                go = True
                if stories:
                    for s in stories.values():
                        if s['isActive']:
                            part = str(s['part']) 

                            if part in s['partloc']:
                                location_list = s['partloc'][part]['location']
                                do = s['partloc'][part]['do']

                                if location in location_list:
                                    go = False
                                    exec(do)
                if go:
                    self.model.store.location = location


        # location:str
        def set_location(self, location):
            loc = self.model.get(location)
            if loc:
                self.model.store.location = location


        # location:str
        # вернёт str
        def get_location(self):
            loc = self.model.store.location
            return loc
