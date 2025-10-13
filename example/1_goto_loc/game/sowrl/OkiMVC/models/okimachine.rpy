init python:

    class OkiMachine:
        def __init__(self):
            self.store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.machine


        # varname:str, value:any
        def add(self, varname, value):
            if not isinstance(varname, str):
                varname = str(varname)
            self.dictionary_store[varname] = value


        # cfname:str
        # вернёт значение с ключом cfname или False
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