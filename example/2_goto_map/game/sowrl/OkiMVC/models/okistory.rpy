init python:

    class OkiStory:
        def __init__(self):
            self.store = None
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.stories


        # name:str, cfname:str, part:int
        def add(self, name, cfname, part=0):
            # создания словаря истории
            story = {
                'name'     : name,
                'cfname'   : cfname,
                'part'     : part,
                'isActive' : False,
                'parthint' : {},
                'partloc'  : {},
                'text'     : ''
            }

            self.dictionary_store[cfname] = story


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
