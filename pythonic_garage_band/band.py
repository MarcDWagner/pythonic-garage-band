class Band:
    def __init__(self, musicians=None):
        self.musicians = musicians or []

class Musician:
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

        def __str__(self):
            return "My name is {self.name} and I play guitar"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name



class Drummer(Musician):
    def __init__(self, name):
        self.name = name
