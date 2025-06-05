Supporting functions to clean/get data is in data_collecting folder <br>
Full data used is on [Kaggle](https://www.kaggle.com/datasets/allenychoi/energy-market-data)

Data:
- Interchange data was retrieved from [EIA](https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/balancing_authority/CISO)
    - Both halves of 2024 were downloaded from the EIA and merged using the data_collecting/interchange_data_set.qmd file
- DAM/RTM data was retrieved from [OASIS](https://oasis.caiso.com/mrioasis/logon.do)
    - Data was downloaded through the OASIS API by running data_collecting/RTM_AND_DAM_DATA_GET.qmd
- Outage data was manually merged from [CAISO](https://www.caiso.com/library/curtailed-and-non-operational-generator-reports)
- Power Plant Locations from [CEC](https://cecgis-caenergy.opendata.arcgis.com/datasets/california-power-plants/explore?filters=eyJSZXRpcmVkX1BsYW50IjpbMCwwXX0%3D&location=37.106048%2C-116.331096%2C6.80)
    - Data was downloaded and merged into weather data inside data_collecting/weather_data.ipynb
- Weather Data from [FastHerbie](https://herbie.readthedocs.io/en/stable/user_guide/tutorial/fast.html) and [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api?start_date=2024-02-02&end_date=2024-02-02&latitude=35.2956286090001&temperature_unit=fahrenheit&longitude=-119.592197855#hourly_weather_variables)
