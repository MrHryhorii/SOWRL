init python:

    class OkiPlace:
        def __init__(self):
            self.store = None
            self.type = 'place'
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.places


        # name:str, cfname:str, arts:str = None
        def add(self, name, cfname, arts=None):
            obj = {
                'name'       : name,
                'cfname'     : cfname,
                'arts'       : cfname,
                'location'   : [cfname],
                'x'          : 0.5,
                'y'          : 0.5,
                'isActive'   : True,
                'image'      : None,
                'text'       : '',
                'status'     : cfname,
                'use_daypart': True
            }

            if arts is not None:
                obj['arts'] = arts
                obj['status'] = arts

            self.dictionary_store[cfname] = obj
            self.store.location = cfname


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