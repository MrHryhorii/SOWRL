init python:

    class OkiProduct:
        def __init__(self):
            self.store = None
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.products


        # name:str, cfn:str, shop:str, price:int, arts:str = None
        def add(self, name, cfn, shop, price, arts = None):
            product = {
                'name'       : name,
                'cfname'     : cfn,
                'shop'       : shop,
                'price'      : price,
                'arts'       : cfn,
                'buyed'      : False,
                'isActive'   : True,
                'image'      : self.store.default_product_image_path,
                'text'       : '',
                'use_daypart': False
            }
            if arts is not None:
                product['arts'] = arts

            if shop not in self.dictionary_store:
                self.dictionary_store[shop] = {}

            if cfn not in self.dictionary_store[shop]:
                self.dictionary_store[shop][cfn] = {}

            self.dictionary_store[shop][cfn] = product


        # shop:str, cfname:str=None
        # вернёт dict или False
        def get(self, shop, cfname=None):
            dictionary = self.get_all()
            output = False 
            if cfname is not None:
                try:
                    output = dictionary[shop][cfname]
                finally:
                    return output
            else:
                try:
                    output = dictionary[shop]
                finally:
                    return output


        # вернёт dict или False
        def get_all(self):
            output = self.dictionary_store
            if output:
                return output
            else:
                return False


        # shop:str, cfname:str=None
        def remove(self, shop, cfname=None):
            dictionary = self.get_all()
            if cfname is not None:
                try:
                    del dictionary[shop][cfname]
                finally:
                    return
            else:
                try:
                    del dictionary[shop]
                finally:
                    return