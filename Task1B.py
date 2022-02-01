import floodsystem.geo as geo


def run():
    """Requirements for Task 1B"""

    # Returns list of stations and their distance from p
    p = (0.,0.)
    from floodsystem.stationdata import build_station_list
    # Build list of stations
    stations = build_station_list()
    stations = geo.stations_by_distance(stations,p)

     # Returns list of closest ten stations
    stations = geo.stations_by_distance(stations[:10])

     # Returns list of furthest ten stations
    stations = geo.stations_by_distance(stations[-10:])