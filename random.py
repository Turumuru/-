import time


class PseudoRandom(object):
    def __init__(self):
        self.m = 3.56992
        self.x0 = 0.1
        self.n = 100 + (int(time.time()) % 1000)

    def seed(self):
        for i in range(0, self.n, 1):
            self.m = round(self.m + 0.00001, 5)
            if self.m == 3.81543:
                self.m = round(self.m + 0.05672, 5)
            elif self.m == 4.0:
                self.m = 3.56992

            self.x0 = round(self.x0 + 0.01, 1)
            if self.x0 == 0.5:
                self.m = 0.1

    def random(self):
        self.x0 = self.m * self.x0 * (1 - self.x0)
        print(self.x0)


Random = PseudoRandom()
Random.seed()
Random.random()
