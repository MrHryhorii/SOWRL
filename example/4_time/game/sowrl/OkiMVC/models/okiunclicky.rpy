init python:

    class OkiUnclicky:
        def __init__(self):
            self.store = None
            self.type = 'unclicky'
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.unclickies


        # cfname:str, location:str, x:int, y:int, arts:str=None
        def add(self, cfname, location, x, y, arts=None):
            obj = {
                'cfname'     : cfname,
                'arts'       : cfname,
                'location'   : location,
                'x'          : x,
                'y'          : y,
                'isActive'   : True,
                'scale'      : 1.0,
                'brightness' : 0.1,
                'saturation' : 1.1,
                'image'      : None,
                'text'       : '',
                'name'       : cfname,
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