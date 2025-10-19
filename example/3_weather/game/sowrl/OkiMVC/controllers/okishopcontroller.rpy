init python:

    class OkiShopController:
        def __init__(self):
            self.model       = None
            self.image_type  = 'jpg'
            #
            self.page        = 1
            self.pages       = 1
            #
            self.row_sort    = 'horizontal' # 'vertical' or 'horizontal'
            self.max_items   = 6        # количество товаров на странице
            self.slip        = 170      # общее смещение товаров по высоте
            self.image_x     = 70       # размер изображения по высоте
            self.image_y     = 70       # размер изображения по ширине
            self.v_gap       = 10       # разрыв между элементами по высоте
            self.h_gap       = 50       # разрыв между элементами по ширине (only for horizontal)
            self.width_slip  = 0.2      # относительное смещение элеметов от центра(0.5)
            self.text_color  = '#000' # цвет текста 
            self.text_outlines = [ (3, "#000", 0, 0), (2, "#fff", 0, 0) ] # цвет обводки


        # model:OkiShop
        def add_model(self, model):
            self.model = model


        # name:str, cfn:str, arts:str = None
        def add(self, name, cfn, arts=None):
            self.model.add(name, cfn, arts)

        
        # cfname:str, keyname:str, val:any
        def set(self, cfname, keyname, val):
            dictionary = self.model.get_all()
            if dictionary:
                if cfname in dictionary:
                    if keyname in dictionary[cfname]:
                        dictionary[cfname][keyname] = val


        # cfn:str, keyname:str=None
        # вернёт dict or False or keyname value
        def get(self, cfn, keyname=None):
            shop = self.model.get(cfn)
            if keyname is not None:
                output = False 
                try:
                    output = shop[keyname]
                finally:
                    return output
            return shop


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

            folder = self.model.store.shop_folder_path
            default_image = self.model.store.default_shop_image_path

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


        # shop:str=''. transition:transition=None
        def open(self, shop='', transition=None):
            if self.get(shop, 'isActive'):
                self.model.store.shop = shop
                self.model.store.transition = transition
                #
                self.model.store.oki_window = 'shop'


        # page:int, pages:int
        def _setPage(self, page, pages=0):
            if pages == 0:
                pages = self.pages
            #
            res = page
            if res < 1:
                res = 1
            if res > pages:
                res = pages
            self.page = res


        # pages:int
        def _setPages(self, pages):
            if pages < 1:
                self.pages = 1
            if self.page > pages:
                self.page = pages
            self.pages = pages 


        # product_list:list
        # return list
        def get_product_for_page(self, product_list):
            page = self.page - 1
            products_max = self.max_items
            return product_list[page * products_max:page * products_max + products_max]
            
            
        