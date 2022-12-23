class Band:
    def __init__(self, musicians=None):
        self.musicians = musicians or []


# base class
class Musician:
    def __init__(self, name):
        self.name = name


# Derived class
class Guitarist(Musician):
    def __init__(self, name="unknown", instrument="guitar"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

# Derived class
class Drummer(Musician):
    def __init__(self, name,instrument="drums"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument


# Derived class
class Bassist(Musician):
    def __init__(self, name, instrument="bass"):
        self.name = name
        self.instrument = instrument

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument
