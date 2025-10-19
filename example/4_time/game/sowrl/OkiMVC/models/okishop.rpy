init python:

    class OkiShop:
        def __init__(self):
            self.store = None
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.shops


        # extra:OkiExtra
        def add_extra(self, extra):
            self.extra = extra


        # name:str, cfn:str, arts:str = None
        def add(self, name, cfn, arts=None):
            shop = {
                'name'       : name,
                'cfname'     : cfn,
                'arts'       : cfn,
                'isActive'   : True,
                'image'      : self.store.default_shop_image_path,
                'text'       : '',
                'use_daypart': False
            }
            if arts is not None:
                shop['arts']  = arts

            self.dictionary_store[cfn] = shop

        
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
