init python:

    class OkiTrigger:
        def __init__(self):
            self.store = None
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.triggers


        # cfname:str, case:str, do:str
        def add(self, cfname, case, do):
            trigger = {
                'name'      : '',
                'cfname'    : cfname,
                'case'      : case,
                'do'        : do,
                'text'      : ''
            }
            self.dictionary_store[cfname] = trigger


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