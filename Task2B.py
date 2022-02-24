# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    for i in stations_level_over_threshold(stations,0.8):
        print(" %s , %s %i[0].name, %i[1]")

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()