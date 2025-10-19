init python:

    class OkiProductController:
        def __init__(self):
            self.model = None
            self.image_type = 'png'

        # model:OkiProduct
        def add_model(self, model):
            self.model = model


        # name:str, cfn:str, shop:str, price:int, arts:str = None
        def add(self, name, cfn, shop, price, arts=None):
            self.model.add(name, cfn, shop, price, arts)


        # shop:str, cfname:str, keyname:str, val:any
        def set(self, shop, cfname, keyname, val):
            dictionary = self.model.get(shop, cfname)
            if dictionary:
                if keyname in dictionary:
                    dictionary[keyname] = val


        # shop:str, cfname:str=None, keyname:str=None
        # вернёт dict or False or keyname value
        def get(self, shop, cfname=None, keyname=None):
            product = self.model.get(shop, cfname)
            if keyname is not None:
                output = False 
                try:
                    output = product[keyname]
                finally:
                    return output
            return product


        # shop:str, isActive:bool
        # вернёт list
        def get_not_buyed_list(self, shop, isActive=True):
            products = self.get(shop)
            output = []
            if products:
                for p in products.values():
                    if p['isActive'] == isActive:
                        if not p['buyed']:
                            output.append(p)
            return output


        # shop:str, isActive:bool
        # вернёт list
        def get_buyed_list(self, shop, isActive=True):
            products = self.get(shop)
            output = []
            if products:
                for p in products.values():
                    if p['isActive'] == isActive:
                        if p['buyed']:
                            output.append(p)
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

            folder = self.model.store.product_folder_path
            default_image = self.model.store.default_product_image_path

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
        

        # shop:str, cfname:str, price:int
        def buy(self, shop, cfname, price=0):
            product = self.get(shop, cfname)
            try:
                if 'buyed' in product:
                    product['buyed'] = True
                    self.model.store.money -= price
            finally:
                return


        # shop:str, cfname:str=None
        def remove(self, shop, cfname=None):
            self.model.remove(shop, cfname)
        