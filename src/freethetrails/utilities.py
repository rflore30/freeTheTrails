
class Trail:
    def __init__(self, name: str, length: int, rating):
        self.name = name
        self.length = length
        self.rating = rating

    def __str__(self):
        return f"{self.name} is {self.length} miles long and has a {self.rating} star rating"


def parse_trails(page: str) -> list[Trail]:
    """
    Given a page of info from AllTrails, return a list of Trails"""
