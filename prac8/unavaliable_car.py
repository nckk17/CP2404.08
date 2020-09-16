from prac8.car import Car
import random

class UnavaliableCar(Car):

    def __int__(self, name, fuel,reliability):
        super().__init__(name, fuel)
        self.reliability=reliability


    def drive (self, distance):
        self.distance = distance

        distance = random.randint(1,100)
        return distance

        if distance < self.reliability:
            return self.distance
        else:
            return 'over ride'






