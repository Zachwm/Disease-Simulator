# Disease model
class Disease:
    def __init__(self, movement, transmission, illness_length, lethality):
        self.movement = movement
        self.transmission = transmission
        self.illness_length = illness_length
        self.lethality = lethality