"""from floodsystem.geo import rivers_with_station
rivers_with_station.sort()
print(rivers_with_station[:10])"""

from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo
#hi

def run():
    """Requirements for Task 1D"""

    # Build list of stations
    stations = build_station_list()

    rivers = geo.rivers_with_station(stations)
    #put it back here orla ok! print("There are " + len(rivers) + " rivers.") was the problem. issue was it couldnt conenctate an 'int' only a string. i tred str-ing the rivers list but it didn't like that either. let me knwow aht u wanna do elisabeth xx
    print(rivers[:10])

    riversandstations = geo.stations_by_river(stations)
    print(riversandstations["River Thames"])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()