class Road:
    _length = None
    _width = None
    _weight = None
    _asphalt_thickness = None

    def __init__(self, length, width):
        self.length = length
        self.width = width


    def roadway(self):
        self._weight = 25
        self._asphalt_thickness = 5
        roadway = self.length * self.width * self._weight * self._asphalt_thickness / 1000
        print(f'необходимость {roadway} тонна для здания ')

roadway_in = Road(5000, 20)
roadway_in.roadway()