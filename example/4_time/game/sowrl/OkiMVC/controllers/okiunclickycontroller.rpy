init python:

    class OkiUnclickyController:
        def __init__(self):
            self.model = None
            self.image_type = 'png'


        # model:OkiUnclicky
        def add_model(self, model):
            self.model = model


        # cfname:str, location:str, x:int, y:int, arts:str=None
        def add(self, cfname, location, x, y, arts=None):
            self.model.add(cfname, location, x, y, arts)


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
        # вернёт list or False
        def get_all_from_location(self, location=''):
            dictionary = self.model.get_all()
            output = False
            try:
                result_list = []
                for obj in dictionary.values():
                    if location in obj['location']:
                        result_list.append(obj)
                if result_list:
                    output = result_list
            finally:
                return output


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

            folder = self.model.store.unclicky_folder_path
            default_image = self.model.store.default_unclicky_image_path

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


        # cfname:str
        def remove(self, cfname):
            self.model.remove(cfname)
