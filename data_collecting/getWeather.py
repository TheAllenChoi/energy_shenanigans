import pandas as pd
import numpy as np
from herbie import FastHerbie
import xarray

# Get hourly weather data for all of 2024
date_range = pd.date_range(
    start = "2024-01-01 00:00",
    end = "2025-01-01 00:00",
    freq = "1h"
)
FH = FastHerbie(date_range, model = "hrrr", fxx = range(0, 1))

data = FH.xarray(":TMP:2 m", remove_grib = False, verbose = True)

coords = pd.read_csv("All_Power_Plants.csv")[["x", "y"]].rename({"x":"longitude", "y":"latitude"}, axis = 1)
unique_coords = coords.drop_duplicates().reset_index(drop = True)
power_plant = pd.read_csv("All_Power_Plants.csv")

# Get Weather for each location
weather = data.herbie.pick_points(points = unique_coords)

weather.to_netcdf("weather_data.nc")

weather = xarray.open_dataset("weather_data.nc")

df_power = power_plant[["OBJECTID", "Plant_Code", "Plant_Name", "Utility_Name", "PrimSource", "Total_MW", "Longitude", "Latitude"]].rename({"Longitude":"longitude", "Latitude":"latitude"}, axis = 1)

df = weather.to_dataframe().reset_index()[["time", "t2m", "point_longitude", "point_latitude"]].rename({"point_longitude":"longitude", "point_latitude":"latitude"}, axis = 1)

output = df_power.merge(df, on = ["longitude", "latitude"], how = "left")

output.to_csv("fullWeatherData.csv", index=False)

