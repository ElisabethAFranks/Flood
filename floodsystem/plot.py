from station import MonitoringStation
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station A")
    plt.tight_layout()
    plt.show()