
class DJK_ELEMENT:
    def __init__(self, start, distance) -> None:
        self.path = list()
        self.path.append(start)
        self.distance_sum = distance

    def add_vertice(self, vertice):
        self.path.append(vertice)

    def add_distance(self, distance):
        self.distance_sum += distance