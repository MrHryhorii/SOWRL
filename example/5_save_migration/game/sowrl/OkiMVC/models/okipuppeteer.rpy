init python:

    class OkiPuppeteer:
        def __init__(self):
            self.store = None
            self.extra = None
            self.dictionary_store = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store
            self.dictionary_store = self.store.puppets

        
        # extra:OkiExtra
        def add_extra(self, extra):
            self.extra = extra


        # kind:str, cfname:str, id_:str, status:str, location:str, x:int, y:int, day:int or [int], interval:str, arts:str=None
        def add(self, kind, cfname, id_, status, location, x, y, day, interval, arts=None):
            puppet = {
                'type'     : kind,
                'cfname'   : cfname,
                'id'       : id_,
                'arts'     : cfname + '_' + status,
                'status'   : status,
                'location' : location,
                'x'        : x,
                'y'        : y,
                'day'      : day,
                'interval' : interval,
                'isActive' : True,
                'text'     : ''
            }
            if arts is not None:
                puppet['arts'] = arts

            if isinstance(location, str):
                puppet['location'] = [location]

            if isinstance(day, int):
                puppet['day'] = [day]

            if not isinstance(id_, str):
                puppet['id'] = str(id_)

            if not kind in self.dictionary_store:
                self.dictionary_store[kind] = {}

            if not cfname in self.dictionary_store[kind]:
                self.dictionary_store[kind][cfname] = {}

            self.dictionary_store[kind][cfname][id_] = puppet 


        # kind:str, cfname:str
        # вернёт dict или False
        def get(self, kind, cfname):
            puppets = self.get_all()
            output = False
            try:
                output = puppets[kind][cfname]
            finally:
                return output


        # вернёт dict или False
        def get_all(self):
            output = self.dictionary_store
            if output:
                return output
            else:
                return False


        # kind:str, cfname:str=None, id_:str=None
        def remove(self, kind, cfname=None, id_=None):
            puppets = self.get_all()
            if id_ is not None:
                try:
                    del puppets[kind][cfname][id_]
                finally:
                    return
            if cfname is not None:
                try:
                    del puppets[kind][cfname]
                finally:
                    return
            else:
                try:
                    del puppets[kind]    
                finally:
                    return  
