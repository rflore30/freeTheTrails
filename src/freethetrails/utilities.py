
class Trail:
    def __init__(self, name, length, rating):
        self.name = name
        self.length = length
        self.rating = rating


def parse_trails(page: str) -> list{trails}:
    """
    Given a page of info from AllTrails, return a list of Trails"""
