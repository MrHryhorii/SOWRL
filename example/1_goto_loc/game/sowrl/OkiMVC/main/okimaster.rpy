init python:

    class OkiMaster:
        def __init__(self):
            # database
            self.store = OkiStore()
            # models
            self.date         = OkiDate()
            self.place        = OkiPlace()
            self.clicky       = OkiClicky()
            self.unclicky     = OkiUnclicky()
            self.person       = OkiPerson()
            self.product      = OkiProduct()
            self.shop         = OkiShop()
            self.story        = OkiStory()
            self.machine      = OkiMachine()
            self.trigger      = OkiTrigger()
            self.weather      = OkiWeather()
            self.puppeteer    = OkiPuppeteer()
            # controllers
            self.date_controller         = OkiDateController()
            self.place_controller        = OkiPlaceController()
            self.clicky_controller       = OkiClickyController()
            self.unclicky_controller     = OkiUnclickyController()
            self.person_controller       = OkiPersonController()
            self.product_controller      = OkiProductController()
            self.shop_controller         = OkiShopController()
            self.story_controller        = OkiStoryController()
            self.machine_controller      = OkiMachineController()
            self.trigger_controller      = OkiTriggerController()
            self.weather_controller      = OkiWeatherController()
            self.puppeteer_controller    = OkiPuppeteerController()
            # extra
            self.extra = OkiExtra()
            ##################################
            self.clickType    = ""
            self.clickBuffer  = ""
            self.clickAction  = ""
            self.playing      = False
            self.isOkiScene   = False
            ##################################
            self._bind()
            self._add_extra()
            self._addDate()
            self._checkMatrix()


        def _bind(self):
            # bind models and database
            self.date.add_store(self.store)
            self.place.add_store(self.store)
            self.clicky.add_store(self.store)
            self.unclicky.add_store(self.store)
            self.person.add_store(self.store)
            self.product.add_store(self.store)
            self.shop.add_store(self.store)
            self.story.add_store(self.store)
            self.machine.add_store(self.store)
            self.trigger.add_store(self.store)
            self.weather.add_store(self.store)
            self.puppeteer.add_store(self.store)
            # bind controllers and models
            self.date_controller.add_model(self.date)
            self.place_controller.add_model(self.place)
            self.clicky_controller.add_model(self.clicky)
            self.unclicky_controller.add_model(self.unclicky)
            self.person_controller.add_model(self.person)
            self.product_controller.add_model(self.product)
            self.shop_controller.add_model(self.shop)
            self.story_controller.add_model(self.story)
            self.machine_controller.add_model(self.machine)
            self.trigger_controller.add_model(self.trigger)
            self.weather_controller.add_model(self.weather)
            self.puppeteer_controller.add_model(self.puppeteer)


        def _add_extra(self):
            self.extra.add_store(self.store)
            self.extra.addMaster(self)
            # add extra to models
            self.date.add_extra(self.extra)
            self.shop.add_extra(self.extra)
            self.weather.add_extra(self.extra)
            self.puppeteer.add_extra(self.extra)
        

        def _addDate(self):
            self.date_controller.add()


        def _checkMatrix(self):
            if self.store.colormatrix is None:
                self.store.colormatrix = [ 1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1 ]


        def _setClickType(self, ct):
            self.clickType = ct


        def _setClickBuffer(self, r):
            self.clickBuffer = r


        def refreshClick(self):
            self.clickType    = ""
            self.clickBuffer  = ""
            self.clickAction  = ""
            

        def refreshScreen(self):
            self.refreshClick()
            self.clickAction  = renpy.call_screen("LoopScreen")
    

        def updateScreen(self):
            renpy.restart_interaction()


        # tr:transition
        def Start(self, tr=fade):
            self.playing = True
            renpy.scene()
            self.ScreenshotScene()  
            renpy.show_screen("OkiUI")
            renpy.with_statement(tr)    
            self.isOkiScene = False

        #####################################################################     


        def ScreenshotScene(self):
            data = renpy.screenshot_to_bytes((self.store.game_screen_width , self.store.game_screen_height))
            renpy.show('ScreenshotScene', at_list=[Transform(xalign=0.5, yalign=0.5)], what=renpy.displayable(im.Data(data, "screenshot.jpg")))


        #####################################################################

        def Scene(self):
            renpy.scene()
            self.ScreenshotScene()
            renpy.hide_screen("OkiUI")
            self.isOkiScene = True
            renpy.pause(0.01) # пауза (обезательно нужна задержка, для корректной отрисовки)


        def noScene(self, transition=None):
            renpy.scene()
            self.ScreenshotScene()
            #
            self.weather_controller.update() # это не обезательно
            #
            renpy.show_screen("OkiUI")
            if transition is not None:
                renpy.with_statement(transition, True)
            self.isOkiScene = False

        #####################################################################


        def ColorMatrix(self, colormatrix=None, timepiece=0.5, layer='master', rst=True):
            from_matrix = self.store.colormatrix
            to_matrix = colormatrix
            #
            if from_matrix is None:
                from_matrix = [ 1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1 ]
            if to_matrix is None:
                colormatrix = [ 1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1 ]
            #
            if self.store.colormatrix != colormatrix:
                self.store.colormatrix = colormatrix
            #
            if layer == 'master':
                renpy.show_layer_at(oki_matrix(from_matrix, to_matrix, timepiece), layer=u'master',  reset=rst)
            if layer == 'screens':
                renpy.show_layer_at(oki_matrix(from_matrix, to_matrix, timepiece), layer=u'screens', reset=rst)
            if layer == 'all':
                renpy.show_layer_at(oki_matrix(from_matrix, to_matrix, timepiece), layer=u'master',  reset=rst)
                renpy.show_layer_at(oki_matrix(from_matrix, to_matrix, timepiece), layer=u'screens', reset=rst)


        def FixColorMatrix(self, layer='master', rst=True):
            if layer == 'master':
                renpy.show_layer_at(Transform(matrixcolor=OkiColorMatrix(self.store.colormatrix)), layer=u'master',  reset=rst)
            if layer == 'screens':
                renpy.show_layer_at(Transform(matrixcolor=OkiColorMatrix(self.store.colormatrix)), layer=u'screens', reset=rst)
            if layer == 'all':
                renpy.show_layer_at(Transform(matrixcolor=OkiColorMatrix(self.store.colormatrix)), layer=u'master',  reset=rst)
                renpy.show_layer_at(Transform(matrixcolor=OkiColorMatrix(self.store.colormatrix)), layer=u'screens', reset=rst)

        #######################################################################

        def ShowImg(self, name, path, x, y):
            if isinstance(x, float) or isinstance(y, float):
                renpy.show(name, at_list=[Transform(xalign=x, yalign=y)], what=renpy.displayable(path))
            else:
                renpy.show(name, at_list=[Transform(xcenter=x, ycenter=y)], what=renpy.displayable(path))

        ########################################################################