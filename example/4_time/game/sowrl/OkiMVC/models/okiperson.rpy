init python:

    class OkiPerson:
        def __init__(self):
            self.store = None
            self.type = 'person'
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.persons


        # name:str, surname:str, cfname:str, location:str, x:int, y:int, arts:str=None
        def add(self, name, surname, cfname, location, x, y, arts=None):
            obj = {
                'name'       : name,
                'surname'    : surname,
                'cfname'     : cfname,
                'arts'       : cfname,
                'location'   : location,
                'x'          : x,
                'y'          : y,
                'isActive'   : True,
                'scale'      : 1.0,
                'hue'        : 3.0,
                'brightness' : 0.15,
                'saturation' : 1.4,
                'action'     : self.type + '_' + cfname,
                'image'      : None,
                'text'       : '',
                'status'     : cfname,
                'use_daypart': True
            }

            if arts is not None:
                obj['arts'] = arts
                obj['status'] = arts

            if isinstance(location, str):
                obj['location'] = [location]

            self.dictionary_store[cfname] = obj


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