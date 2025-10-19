init python:

    class OkiStoryController:
        def __init__(self):
            self.model = None
            #
            self.page = 1                # стартавая страница
            self.pages = 1
            #
            self.hint_max_length = 48    # максимальное количество символов в строке
            self.hint_max_string = 20    # максимальное количество строк на странице
            self.hints_background = ''   # путь к картике, если пусто, то серый фон
            self.y_slip = 128            # сдвиг текста вниз
            self.x_slip = 128            # сдвиг текств вправо
            self.width_slip = 0.2        # относительное смещение элеметов от центра(0.5)
            self.text_color  = '#000'  # цвет текста
            self.hint_outline = [ (2, "#fff", 0, 0) ] # цвет обводки подсказки
            self.text_outlines = [ (3, "#000", 0, 0), (2, "#fff", 0, 0) ] # цвет обводки


        # model:OkiStory
        def add_model(self, model):
            self.model = model


        # name:str, cfname:str, part:int = 0
        def add(self, name, cfname, part=0):
            self.model.add(name, cfname, part)


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


        # cfname:str, part:int or str, hint:str
        def set_parthint(self, cfname, part, hint):
            story = self.model.get(cfname)
            if story:
                if not isinstance(part, str):
                    part = str(part) 

                story['parthint'][part] = hint


        # cfname:str, part:int or str, hint:str
        def get_hint(self, cfname, part, hint):
            parthint = self.get(cfname, 'parthint')
            if not isinstance(part, str):
                part = str(part)
            if part in parthint:
                return parthint[part]
            return False


        # cfname:str, part:int or str, location:str or list, orlabel:str
        def set_partloc(self, cfname, part, location, do):
            story = self.model.get(cfname)
            if story:
                if not isinstance(part, str):
                    part = str(part) 
                if not isinstance(location, list):
                    location = [location] 
                if not isinstance(do, str):
                    do = str(do)

                story['partloc'][part] = {
                    'location' : location,
                    'do'       : do
                }


        # cfname:str
        # вернёт bool
        def get_status(self, cfname):
            story = self.model.get(cfname)
            if story:
                return story['isActive']
            else:
                return False


        # cfname:str
        def enable(self, cfname):
            story = self.model.get(cfname)
            if story:
                story['isActive'] = True
                

        # cfname:str
        def disable(self, cfname):
            story = self.model.get(cfname)
            if story:
                story['isActive'] = False
                
                
        # cfname:str
        # вернёт int or False
        def get_part(self, cfname):
            story = self.model.get(cfname)
            if story:
                part = story['part']
                return part
            else:
                return False


        # cfname:str, number:int
        def set_part(self, cfname, number):
            story = self.model.get(cfname)
            if story:
                story['part'] = number
                

        # cfname:str, number:int = 1
        def part_up(self, cfname, number=1):
            story = self.model.get(cfname)
            if story:
                story['part'] += number
                

        # cfname:str, number:int = 1
        def part_down(self, cfname, number=1):
            story = self.model.get(cfname)
            if story:
                story['part'] -= number


        # img_path:str
        def set_hints_background(self, img_path):
            if renpy.loadable(img_path):
                self.hints_background = img_path


        # transition:transition=None
        def show_hints(self, transition=None):
            self.model.store.transition = transition
            self.model.store.oki_window = 'hints'


        ###################################################


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


        # isActive:bool
        def get_all_parthints(self, isActive=True):
            stories = self.model.get_all()
            hints = []
            if stories:
                for story in stories.values():
                    if story['isActive'] == isActive:
                        part = self.get_part(story['cfname']) # int or False
                        if part:
                            if not isinstance(part, str):
                                part = str(part)
                            if part in story['parthint']:
                                hints.append(story['parthint'][part])
            if hints:
                return hints
            else:
                return False

        
        # hints:list[str]
        # return list[list[str]]
        def hintlist_to_screen(self, hints):
            output = False
            if hints:
                new_hints = []
                for hint in hints:
                    words = hint.split()
                    if words:
                        string = ''
                        items = len(words)
                        item = 1
                        for word in words:
                            if not string:
                                string += word + ' '
                                if len(string) > self.hint_max_length:
                                    new_hints.append(string)
                                    string = ''
                            else:
                                if len(string + word + ' ') > self.hint_max_length:
                                    new_hints.append(string)
                                    string = word + ' '
                                else:
                                    string += word + ' '
                                    if len(string) >= self.hint_max_length:
                                        new_hints.append(string)
                                        string = ''
                            #
                            if item == items:
                                if string:
                                    new_hints.append(string)
                                new_hints.append(' ')
                            item += 1
                #
                if new_hints:
                    if new_hints[-1] == ' ':
                        del new_hints[-1]
                #
                output = new_hints
            return output


        # hints:list
        # return list
        def get_strings_for_page(self, hints):
            page = self.page - 1
            hint_max_string = self.hint_max_string
            return hints[page * hint_max_string:page * hint_max_string + hint_max_string]
                