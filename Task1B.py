from floodsystem.geo import stations_by_distance


def run():
    """Requirements for Task 1B"""

    # Returns list of stations and their distance from p
    stations = stations_by_distance(stations, p)

     # Returns list of closest ten stations
    stations = stations_by_distance(stations[:10])

     # Returns list of furthest ten stations
    stations = stations_by_distance(stations[-10:])