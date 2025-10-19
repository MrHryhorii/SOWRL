init python:

    class OkiMachineController:
        def __init__(self):
            self.model = None


        # model:OkiStory
        def add_model(self, model):
            self.model = model


        # varname:str, value:any
        def add(self, varname, value):
            self.model.add(varname, value)


        # varname:str
        # вернёт dict or False or varname value
        def get(self, varname=None):
            if varname is None:
                output = self.model.get_all()
            else:
                output = self.model.get(varname)
            return output


        # varname:str, value:any
        def set(self, varname, value):
            machine = self.model.get_all()
            if varname in machine:
                machine[varname] = value


        # cfname:str
        def remove(self, cfname):
            self.model.remove(cfname)
