init python:

    class OkiDate:
        def __init__(self):
            self.store = None
            self.extra = None


        # store:OkiStore
        def add_store(self, store):
            self.store = store


        # extra:OkiExtra
        def add_extra(self, extra):
            self.extra = extra


        # h:int = 0, m:int = 0
        def add(self, h=0, m=0):
            date = {
                'hour'      : h,
                'minute'    : m,
                'dayMinutes': 0,
                'time'      : "00:00",
                'dayPart'   : 0,
                'day'       : 1,
                'monthday'  : 1,
                'weekday'   : 1,
                'weekname'  : 'Monday',
                'week'      : 1,
                'month'     : 1
            }

            date['hour']       = self.limit(date, 'hour', self.store.dateLimits)
            date['minute']     = self.limit(date, 'minute', self.store.dateLimits)
            date['dayMinutes'] = self.extra.time_to_minutes(date['hour'], date['minute'])
            date['time']       = str(date['hour']).zfill(2) + ":" + str(date['minute']).zfill(2)
            date['dayPart']    = self.gen_daypart(date['dayMinutes'], self.store.dayPartsList)
            date['weekname']   = self.store.weekdayNames[date['weekday'] - 1]
            self.store.date = date


        # keyname:str
        # возвращает словарь с датой(dict) или False или значение свойства даты
        def get(self, keyname=None):
            if keyname is not None:
                output = False 
                try:
                    output = self.store.date[keyname]
                finally:
                    return output
            else:
                if self.store.date:
                    return self.store.date
                else:
                    return False


        # d:dict
        def edit(self, d):
            if isinstance(d, dict):
                date = self.corrected_date(d)
                self.store.date = date


        # d:dict
        # вернёт обновлённое время(dict)
        def corrected_date(self, d):
            # dct:dict, name:str, limit:list, other:list(or str) = None
            def correction(dct, name, limit, other = None):
                while(dct[name] > limit[1]):
                    if limit[0] != 0:
                        dct[name] -= limit[1]
                    else:
                        dct[name] -= limit[1] + 1

                    if other is not None:
                        if isinstance(other, list):
                            for i in other:
                                dct[i] += 1
                        else:
                            dct[other] += 1

            if d['minute'] > self.store.dateLimits['minute'][1]:
                correction(d, 'minute', self.store.dateLimits['minute'], 'hour')
            
            if d['hour'] > self.store.dateLimits['hour'][1]:
                correction(d, 'hour', self.store.dateLimits['hour'], ['day', 'weekday', 'monthday'])

            if d['weekday'] > self.store.dateLimits['weekday'][1]:
                correction(d, 'weekday', self.store.dateLimits['weekday'], 'week')

            if d['week'] > self.store.dateLimits['week'][1]:
                correction(d, 'week', self.store.dateLimits['week'], 'month')

            if d['monthday'] > self.store.dateLimits['monthday'][1]:
                correction(d, 'monthday', self.store.dateLimits['monthday'])

            d['dayMinutes'] = self.extra.time_to_minutes(d['hour'], d['minute'])
            d['time']       = str(d['hour']).zfill(2) + ":" + str(d['minute']).zfill(2)
            d['dayPart']    = self.gen_daypart(d['dayMinutes'], self.store.dayPartsList)
            d['weekname']   = self.store.weekdayNames[d['weekday'] - 1]
            return d


        # d:dict, k:str, limiter:dict
        # вернёт значение в пределах лимитов(int)
        def limit(self, d, k, limiter):
            output = d[k]
            if d[k] > limiter[k][1]:
                output = limiter[k][1]
            if d[k] < limiter[k][0]:
                output = limiter[k][0]
            return output


        # dm:int, parts:list
        # вернёт часть суток(int)
        def gen_daypart(self, dm, parts):
            output = 0
            if parts:
                currentMinutes = dm
                i = 0
                # перебираем список с частями дня
                while i < len(parts):
                    pod_hours   = parts[i][0]
                    pod_minutes = parts[i][1]
                    podMinutes  = self.extra.time_to_minutes(pod_hours, pod_minutes)
                    # если наше время больше или равно, то пока сохраняем (номер части суток) и проверяем дальше
                    if(currentMinutes >= podMinutes):
                        output = i
                        i += 1
                    else:
                        break
            return output

        #########################################################################################################
                                                        #Timer#
        #########################################################################################################

        # tasktype:string, cfname:str ,do:string, day:int, dayMinutes:int
        def add_timetask(self, tasktype, cfname, do, day=1, dayMinutes=0):
            tt = {
                'cfname'    : cfname,
                'typetask'  : tasktype,
                'do'        : do,
                'executed'  : False,
                'day'       : day,
                'dayMinutes': dayMinutes,
                'text'      : ''
            }
            self.store.timetasks[cfname] = tt

        
        # cfname:str
        # вернёт dict or False
        def get_timetask(self, cfname):
            dictionary = self.get_all_timetasks
            output = False 
            try:
                output = dictionary[cfname]
            finally:
                return output


        # вернёт dict or False
        def get_all_timetasks(self):
            if self.store.timetasks:
                return self.store.timetasks
            else:
                return False


        # cfname:str
        def remove_timetask(self, cfname):
            dictionary = self.get_all_timetasks()
            try:
                del dictionary[cfname]
            finally:
                return