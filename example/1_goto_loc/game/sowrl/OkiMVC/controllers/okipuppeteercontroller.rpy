init python:

    class OkiPuppeteerController:
        def __init__(self):
            self.model = None


        # model:OkiPuppeteer
        def add_model(self, model):
            self.model = model


        # kind:str, cfname:str, id_:str, status:str, location:str, x:int, y:int, day:int or [int], interval:str, arts:str=None
        def add(self, kind, cfname, id_, status, location, x, y, day, interval, arts=None):
            self.model.add(kind.lower(), cfname, id_, status, location, x, y, day, interval, arts)


        # kind:str, cfname:str, id_:str=None, keyname:str=None
        # вернёт dict or False or keyname value
        def get(self, kind, cfname, id_=None, keyname=None):
            puppet = self.model.get(kind, cfname)
            output = False
            if keyname is not None:
                try:
                    output = puppet[id_][keyname]
                finally: 
                    return output
            if id_ is not None:
                try:
                    output = puppet[id_]
                finally:
                    return output
            return puppet


        # kind:str, cfname:str, id_:str, keyname:str, val:any
        def set(self, kind, cfname, id_, keyname, val):
            puppet = self.model.get(kind, cfname)
            if puppet:
                if id_ in puppet:
                    if keyname in puppet[id_]:
                        puppet[id_][keyname] = val


        # kind:str, location:str, day_minutes:int, month_day:int
        def process(self, kind, location, day_time, month_day):
            keyname = None
            puppetdict = False
            delete_list = []
            
            if kind.lower() == 'place':
                keyname = 'place'
                puppetdict = self.model.store.places

            if kind.lower() == 'unclicky':
                keyname = 'unclicky'
                puppetdict = self.model.store.unclickies

            if kind.lower() == 'clicky':
                keyname = 'clicky'
                puppetdict = self.model.store.clickies

            if kind.lower() == 'person':
                keyname = 'person'
                puppetdict = self.model.store.persons

            if keyname is not None:
                puppets = self.model.get_all()
                if puppets:
                    if keyname in puppets:
                        for cfname in puppets[keyname]:
                            if cfname not in puppetdict:
                                delete_list.append(cfname)
                            else:
                                for id_ in puppets[keyname][cfname].values():
                                    if id_['isActive']:
                                        if location in id_['location'] and month_day in id_['day'] and self.model.extra.is_in_interval(day_time, id_['interval']):
                                            puppetdict[cfname]['location'] = id_['location']
                                            puppetdict[cfname]['arts'] = id_['arts']
                                            puppetdict[cfname]['x'] = id_['x']
                                            puppetdict[cfname]['y'] = id_['y']
                                            puppetdict[cfname]['status'] = id_['status']
                                            break
                                        else:
                                            puppetdict[cfname]['location'] = self.model.store.nowhere # nowhere
                        if delete_list:
                            for i in delete_list:
                                self.remove(keyname, i)


        # kind:str, puppetdict:dict
        def clean(self, kind, puppetdict):
            puppets = self.model.get_all()
            k = kind.lower()
            delete_key_list = []
            if k in puppets:
                for p in puppets[k]:
                    if p not in puppetdict:
                        delete_key_list.append(p)
            if delete_key_list:
                for i in delete_key_list:
                    self.remove(k, i)


        # kind:str, cfname:str=None, id_:str=None
        def remove(self, kind, cfname=None, id_=None):
            self.model.remove(kind, cfname, id_)
                        