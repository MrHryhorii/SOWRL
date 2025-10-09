init python:

    class OkiDateController:
        def __init__(self):
            self.model = None


        # model:OkiDate
        def add_model(self, model):
            self.model = model


        # h:int = 0, m:int = 0
        def add(self, h=0, m=0):
            self.model.add(h, m)


        # cfname:str
        # вернёт dict or False or value from date
        def get(self, keyname=None):
            output = self.model.get(keyname)
            return output


        # keyname:str, val:any
        def set(self, keyname, val):
            date = self.model.get()
            if date:
                if keyname in date:
                    date[keyname] = val
                    self.model.edit(date)
                        

        # h:int, m:int
        def set_time(self, h, m):
            date = self.model.get()
            date['hour']   = h
            date['hour']   = self.model.limit(date, 'hour', self.model.dateLimits)
            date['minute'] = m
            date['minute'] = self.model.limit(date, 'minute', self.model.dateLimits)
            self.model.edit(date)
            #
            self.process_timetasks()


        # m:int
        def add_minutes(self, m):
            if m < 0:
                m *= -1
            date = self.model.get()
            date['minute'] += m
            self.model.edit(date)
            #
            self.process_timetasks()


        # h:int
        def add_hours(self, h):
            if h < 0:
                h *= -1
            date = self.model.get()
            date['hour'] += h
            self.model.edit(date)
            #
            self.process_timetasks()
        

        # d:int
        def add_days(self, d):
            if d < 0:
                d *= -1
            date = self.model.get()
            date['day']      += d 
            date['weekday']  += d 
            date['monthday'] += d 
            self.model.edit(date)        
            #
            self.process_timetasks()


        # t:string, i:string
        def is_in_interval(self, t, i):
            output = self.model.extra.is_in_interval(t, i)
            return output


        # t:string ,d:int   ("08:30", 0)
        def time_to(self, t, d=0):
            t = self.model.extra.parse_time(t)
            if t:
                hour = t[0]
                minute = t[1]
                target_day_minutes = self.model.extra.time_to_minutes(hour, minute)
                #
                current_day_minutes = self.get('dayMinutes')
                max_hour = self.model.store.dateLimits['hour'][1]
                max_minute = self.model.store.dateLimits['minute'][1]
                max_day_minutes = self.model.extra.time_to_minutes(max_hour, max_minute + 1)
                diff = 0
                #
                if current_day_minutes < target_day_minutes:
                    diff = target_day_minutes - current_day_minutes
                    self.add_minutes(diff)
                if current_day_minutes > target_day_minutes:
                    diff = max_day_minutes - (current_day_minutes - target_day_minutes)
                    self.add_minutes(diff)
                if current_day_minutes == target_day_minutes:
                    diff = max_day_minutes
                    self.add_minutes(diff)
                #
                if d > 0:
                    self.add_days(d)
                #
                return diff + (max_day_minutes * d) # дополнительно вернём результат, чтото бы узнать сколько прошло минут


        #########################################################################################################
                                                        #Timer#
        #########################################################################################################

        # cfname:str, do:str, timepiece: int, sort:str
        def do_in(self, cfname, do, timepiece=0, sort='minutes'):
            day = 1
            dayMinutes = 0
            #
            date = self.model.get()
            if date:
            #
                if sort == 'minutes':
                    data       = self.model.extra.correct_day_by_dayminutes(date['day'], date['dayMinutes'] + timepiece)
                    day        = data[0]
                    dayMinutes = data[1]

                if sort == 'hours':
                    data       = self.model.extra.correct_day_by_dayminutes(date['day'], self.model.extra.time_to_minutes(timepiece, 0))
                    day        = data[0]
                    dayMinutes = data[1]

                if sort == 'days':
                    day        = date['day'] + timepiece
                    dayMinutes = date['dayMinutes']

            self.model.add_timetask('do_in', cfname, do, day, dayMinutes)


        # cfname:str, do:str, when:str, days:int
        def do_at(self, cfname, do, when, days=0):
            day = 1
            dayMinutes = 0
            #
            date = self.model.get()
            if date:
            #
                timedata   = self.model.extra.parse_time(when)
                data       = self.model.extra.correct_day_by_dayminutes(date['day'] + days, self.model.extra.time_to_minutes(timedata[0], timedata[1]))
                day        = data[0]
                dayMinutes = data[1]

            self.model.add_timetask('do_at', cfname, do, day, dayMinutes)


        def process_timetasks(self):
            date = self.model.get()
            if date:
                timetasks = self.model.get_all_timetasks()
                remove_list = []
                task = None
                #
                if timetasks:
                    #
                    timetasks = timetasks.values() # преобразование словаря словарей в список словарей
                    timetasks = sorted(timetasks, key=lambda d: (d['day'], d['dayMinutes']), reverse=False) # сортировка по дням и минутам дня
                    #
                    for i in timetasks:
                        if i['executed']:
                            remove_list.append(i['cfname'])
                        #
                        elif i['day'] > date['day']:
                            break # прерываем дальнейшую проверку
                        #
                        else:
                            if i['day'] < date['day']:
                                task = i['do']
                                i['executed'] = True
                                break
                            elif i['day'] == date['day']:
                                if i['dayMinutes'] <= date['dayMinutes']:
                                    task = i['do']
                                    i['executed'] = True
                                    break
                #
                if remove_list:
                    for i in remove_list:
                        self.model.remove_timetask(i)
                #
                if task is not None:
                    exec(task)
                    # рекурсия для проверки всего списка
                    self.process_timetasks()


        # cfname:str, keynama:str, value:any
        def set_timetask(self, cfname, keyname, value):
            task = self.model.get_timetask(cfname)
            if task:
                if keyname in task:
                    task[keyname] = value


        # cfname:str
        def remove_timetask(self, cfname):
            self.model.remove_timetask(cfname)
                    
