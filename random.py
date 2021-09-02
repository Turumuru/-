import time


class PseudoRandom(object):
    def __init__(self):
        self.m = 0.0
        self.x0 = 0.0

    def seed(self):
        n = 100 + int((time.time() % 1) * 100)
        for i in range(0, n, 1):
            self.m = self.calc_m()
            self.x0 = self.calc_x0()

    def calc_m(self):
        while 1 == 1:
            m1 = round((time.time() % 0.001) * 10000, 5)
            if (m1 >= 3.56992) & (m1 < 3.81543):
                return m1

            if (m1 > 3.87214) & (m1 <= 4.0):
                return m1

    def calc_x0(self):
        while 1 == 1:
            x = round(time.time() % 1, 5)
            if (x > 0) & (x < 0.5):
                return x

    def random(self):
        self.x0 = self.m * self.x0 * (1 - self.x0)
        print(self.x0)


Random = PseudoRandom()
Random.seed()
Random.random()
