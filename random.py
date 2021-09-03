import time


class PseudoRandom(object):
    def __init__(self):
        self.m = 0.0
        self.x0 = 0.0
        self.n = 0
        self.is_first_generation = True

    def calc_seed(self):
        time_seed = time.time()
        time_entropy_m = int((time_seed % 1) * 1_000)
        time_entropy_x0 = int((time_seed % 1) * 100)
        time_entropy_n = int((time_seed % 1) * 10)

        # расчёт m
        if time_entropy_m % 2 == 0:
            self.m = 3.56992 + time_entropy_m % (3.81542 - 3.56992)
        else:
            self.m = 3.87215 + time_entropy_m % (4.0 - 3.87215)

        # расчёт x0
        self.x0 = 0.1 + time_entropy_x0 % (0.4 - 0.1)

        # расчёт n
        self.n = 100 + int(time_entropy_n * 100)

    def random(self):
        if self.is_first_generation:
            Random.calc_seed()
            for i in range(self.n):
                self.x0 = self.m * self.x0 * (1 - self.x0)
        else:
            self.x0 = self.m * self.x0 * (1 - self.x0)
            
        return self.x0
