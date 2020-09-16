from pra8.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flagfall = 4.5

    def __int__(self,name="",fuel=0,fancifulness=1.0):
        super().__init__(name,fuel)
        self.fancifulness = fancifulness
        self.price_per_km = Taxi.price_per_km * self.fancifulness

    def get_fare(self):
        return super().get_fare()+self.flagfall

    def __str__(self):
        pass
if __name__ == '__main__':
    silver_taxi = SilverServiceTaxi("Hummer", 200, 4)
    silver_taxi.drive(50)
    print("Current fare: $(:.2f)".format(silver_taxi.get_fare()))


