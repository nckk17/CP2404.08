from pra8.car import Car

class New_taxi(Car):

    def _init_(self, name, fuel, price_per_km):
        """Initialise a Taxi instance, based on parent class Car."""
        super()._init_(name, fuel)
        self.price_per_km = price_per_km
        self.current_fare_distance = 0


    def _str_(self):
        """Return a string like a Car but with current fare distance."""
        print ("{}, {}km on current fare, ${:.2f}/km".format(super()._str_(),
                                                             self.current_fare_distance,
                                                             self.price_per_km))

    def get_fare(self):
        """Return the price for the taxi trip."""
        print ("Get fare:",self.price_per_km * self.current_fare_distance)


    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0


    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        print ( 'Distance driven:',distance_driven )

x = New_taxi('Prius 1', 100, 1.23)
x.drive(40)
x.get_fare()
x.start_fare()
x._str_()