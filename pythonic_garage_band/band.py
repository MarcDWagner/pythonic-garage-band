class Band:
    def __init__(self, musicians=None):
        self.musicians = musicians or []


# base class
class Musician:
    def __init__(self, name):
        self.name = name


# Derived class
class Guitarist(Musician):
    def __init__(self, name="unknown"):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


# Derived class
class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


# Derived class
class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


