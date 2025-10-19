init python:

    class OkiTriggerController:
        def __init__(self):
            self.model = None


        # model:OkiTrigger
        def add_model(self, model):
            self.model = model


        # cfname:str, case:str, do:str
        def add(self, cfname, case, do):
            self.model.add(cfname, case, do)


        # cfname:str, keyname:str, val:any
        def set(self, cfname, keyname, val):
            dictionary = self.model.get(cfname)
            if dictionary:
                if keyname in dictionary:
                    dictionary[keyname] = val


        # cfname:str, keyname:str=None
        # вернёт dict or False or keyname value
        def get(self, cfname, keyname=None):
            dictionary = self.model.get(cfname)
            if keyname is not None:
                output = False
                try:
                    output = dictionary[keyname]
                finally:
                    return output
            else:
                return dictionary


        # cfname:str
        # remove trigger by cfname
        def remove(self, cfname):
            self.model.remove(cfname)


        # проверка триггеров на проверку клика
        def click(self):
            if self.model.dictionary_store:
                for trigger in self.model.dictionary_store.values():
                    case = trigger['case']
                    if 'game.clickType' in case or 'game.clickAction' in case:
                        cfname = trigger['cfname']
                        do     = trigger['do']
                        # выполняем триггер если выполняется условие
                        if eval(case):                    # check trigger
                            self.model.remove(cfname)     # remove trigger(in dict)
                            exec(do)                      # execute trigger


        # проверка и выполнение триггеров
        def process(self):
            if self.model.dictionary_store:
                for trigger in self.model.dictionary_store.values():
                    case      = trigger['case']
                    cfname    = trigger['cfname']
                    do        = trigger['do']
                    # выполняем триггер если выполняется условие
                    if eval(case):                    # check trigger
                        self.model.remove(cfname)     # remove trigger(in dict)
                        exec(do)                      # execute trigger
        