init python:

    class OkiExtra:
        def __init__(self):
            self.store  = None
            self.master = None
            self.okiScreenBeforeShow = True


        # store:OkiStore
        def add_store(self, store):
            self.store = store


        # master:OkiMaster
        def addMaster(self, master):
            self.master = master


        # округляет результат деления в большую сторону
        # a:int, b:int
        def ceil(self, a, b):
            return int((a / b) + ((a % b) != 0));


        # округляет число в меньшую сторону
        def floor(self, n):
            return int(n // 1)


        # принимает массив чисел, вернёт среднее арифметичское значение
        def mean(self, numbers):
            return float(sum(numbers)) / max(len(numbers), 1)


        # нахождение косинуса между векторами
        def cos2D(self, ax, ay, bx, by):
            numerator   = ax * bx + ay * by
            denominator = ((ax ** 2 + ay ** 2) ** 0.5) * ((bx ** 2 + by ** 2) ** 0.5)
            res = numerator / denominator
            return res
        
        # функция арккосинуса
        def arccos(self, x):
            if x >= 0:
                res = 90 * ((1 - x) ** 0.5) * (1 - x/10)
            else:
                res = 180 - (90 * ((1 - abs(x)) ** 0.5) * (1 - abs(x)/10))
            return res
        

        # расстояние между точками в 1D пространстве
        def distance(self, x1, x2):
            d = abs(x2 - x1)
            return d
            

        # расстояние между точками в 2D пространстве
        def distance2D(self, x1, y1, x2, y2):
            x = (x2 - x1) ** 2
            y = (y2 - y1) ** 2
            d = (x + y) ** (0.5)
            return d

        ###############################################################################

        # h:int, m:int
        # вернёт int
        def time_to_minutes(self, h, m):
            return ((self.store.dateLimits['minute'][1] + 1) * h) + m


        def minutes_to_time(self, m):
            max_minutes_in_hour = self.store.dateLimits['minute'][1] + 1
            result = '{:02d}:{:02d}'.format(*divmod(m, max_minutes_in_hour))
            return result


        # day:int, dayMinutes:int
        # вернёт list
        def correct_day_by_dayminutes(self, day, dayMinutes):
            maxHours   = self.store.dateLimits['hour'][1] + 1
            maxMinutes = self.store.dateLimits['minute'][1] + 1
            maxMinutes = maxHours * maxMinutes
            while(dayMinutes >= maxMinutes):
                dayMinutes -= maxMinutes
                day += 1
            return [day, dayMinutes]


        # tm:str
        # вернёт list(int)
        def parse_time(self, tm):
            # "01:20"
            tm = tm.strip()
            fh = int(tm[:2])
            fm = int(tm[3:])
            # [1, 20]
            return [fh, fm]


        # tm:str
        # вернёт list(int)
        def parse_intervals(self, tm):
            # "01:20-14:45"
            tm = tm.strip()
            fh = int(tm[:2])
            fm = int(tm[3:5])
            lh = int(tm[6:8])
            lm = int(tm[9:])
            # [1, 20, 14, 45]
            return [fh, fm, lh, lm]


        # dm:int, dms:int, dme:int
        # вернёт True/False
        def is_minutes_between(self, dm, dms, dme):
            if dms < dme:
                if dms <= dm and dm < dme:
                    return True
            if dms == dme:
                if dm == dms:
                    return True
            if dms > dme:
                if dms <= dm or dm < dme:
                    return True
            return False


        # t:string, i:string
        def is_in_interval(self, t, i):
            time_parsed = self.parse_time(t)
            time_in_minutes = self.time_to_minutes(time_parsed[0], time_parsed[1])
            #
            interval_parsed = self.parse_intervals(i)
            interval_start = self.time_to_minutes(interval_parsed[0], interval_parsed[1])
            interval_end = self.time_to_minutes(interval_parsed[2], interval_parsed[3])
            #
            output = self.is_minutes_between(time_in_minutes, interval_start, interval_end)
            return output


        def list_to_string(self, l, divider=None): 
            # initialize an empty string
            string = "" 
            #
            if divider is not None:
                if not isinstance(divider, str):
                    divider = str(divider)
            # traverse in the string  
            if l:
                items = len(l)
                item = 1
                for i in l: 
                    string += i
                    if item != items:
                        if divider is not None:
                            string += divider
                    item += 1
            # return string  
            return string

        ##############################################################      

        def show_schedule(self, kind, cfname):
            try:
                puppet_item = False
                #
                if kind.lower() == 'place':
                    puppet_item = self.master.place_controller.get(cfname)

                if kind.lower() == 'unclicky':
                    puppet_item = self.master.unclicky_controller.get(cfname)

                if kind.lower() == 'clicky':
                    puppet_item = self.master.clicky_controller.get(cfname)

                if kind.lower() == 'person':
                    puppet_item = self.master.person_controller.get(cfname)

                renpy.show_screen('Schedule', kind.lower(), cfname, puppet_item) 
            finally:
                return

        def hide_schedule(self):
            renpy.hide_screen('Schedule')


        def start_minutes_from_interval(self, interval):
            intervals = self.parse_intervals(interval)
            start = self.time_to_minutes(intervals[0], intervals[1])
            return start

        def end_minutes_from_interval(self, interval):
            intervals = self.parse_intervals(interval)
            end = self.time_to_minutes(intervals[2], intervals[3])
            return end

        ###############################################################

    # класс для инкапсуляции ColorMatrix
    class OkiColorMatrix(ColorMatrix):
        def __init__(self, matrix = None):
            if matrix is None:
                self.matrix = [ 1,0,0,0,
                                0,1,0,0,
                                0,0,1,0,
                                0,0,0,1 ]
            else:
                self.matrix = matrix
            

        # принимаем ColorMatrix и вернём готовую цветовую матрицу
        def __call__(self, other, done):
            #if type(other) is not type(self):          # old check
            if not isinstance(other, OkiColorMatrix):   # new check
                if self.checkColorMatrixClass(self.matrix):
                    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h = self.matrix(other, done) # используем внутренний метод __call__
                else:
                    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h = self.matrix
            else:
                if self.checkColorMatrixClass(other.matrix):
                    old_q, old_w, old_e, old_r, old_t, old_y, old_u, old_i, old_o, old_p, old_a, old_s, old_d, old_f, old_g, old_h = other.matrix(other, done) # используем внутренний метод __call__
                else:
                    old_q, old_w, old_e, old_r, old_t, old_y, old_u, old_i, old_o, old_p, old_a, old_s, old_d, old_f, old_g, old_h = other.matrix
                
                if self.checkColorMatrixClass(self.matrix):
                    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h = self.matrix(other, done) # используем внутренний метод __call__
                else:
                    q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h = self.matrix

                q = old_q + (q - old_q) * done
                w = old_w + (w - old_w) * done
                e = old_e + (e - old_e) * done
                r = old_r + (r - old_r) * done
                t = old_t + (t - old_t) * done
                y = old_y + (y - old_y) * done
                u = old_u + (u - old_u) * done
                i = old_i + (i - old_i) * done
                o = old_o + (o - old_o) * done
                p = old_p + (p - old_p) * done
                a = old_a + (a - old_a) * done
                s = old_s + (s - old_s) * done
                d = old_d + (d - old_d) * done
                f = old_f + (f - old_f) * done
                g = old_g + (g - old_g) * done
                h = old_h + (h - old_h) * done

            return Matrix([ q, t, o, d,
                            w, y, p, f,
                            e, u, a, g,
                            r, i, s, h ])


        def checkColorMatrixClass(self, matrix):
            for base in matrix.__class__.__bases__:
                if base.__name__ == "ColorMatrix":
                    return True
            return False
                

        

            