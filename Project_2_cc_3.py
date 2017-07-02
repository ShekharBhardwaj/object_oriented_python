class RaceCar:
    def __init__(self, color="Yellow", fuel_remaining="0%", **kwargs):

        for key, value in kwargs.items():
            setattr(self, key, value)


racecar = RaceCar("Black", "100%", speed="1000 m/h")