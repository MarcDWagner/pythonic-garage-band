class Band:
    def __init__(self, name="unknown", members=None, solos=None):
        self.name = name or []
        self.members = members or []
        self.solos = solos or []

    # def play_solos(self):
    #     return


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

    def play_solo(self):
        return f"face melting guitar solo"

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

    def play_solo(self):
        return f"rattle boom crash"


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

    def play_solo(self):
        return f"bom bom buh bom"
