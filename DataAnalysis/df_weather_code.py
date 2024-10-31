import json
import pandas as pd

with open('../DataCollection/Data/all_data.json') as file:
    data = json.load(file)

df = pd.DataFrame(data)


def weather_code_sort(list: list):

    moderate_rain = [51, 53, 56, 61, 63, 66, 80, 81]
    heavy_rain = [55, 57, 65, 67, 82, 95, 96]

    rain = moderate_rain + heavy_rain
    snow = [71, 73, 75, 77, 85, 86]
    others = [0, 1, 2, 3, 45, 48]

    moderate_rain_data = []
    heavy_rain_data = []
    snow_data = []
    others_data = []

    for i in list:
        if i in moderate_rain:
            moderate_rain_data.append(i)
        if i in heavy_rain:
            heavy_rain_data.append(i)
        if i in snow:
            snow_data.append(i)
        if i in others:
            others_data.append(i)
        else:
            pass

    rain_data = moderate_rain_data + heavy_rain_data
    
    dict = {
        'Light to Moderate Rain': len(moderate_rain_data),
        'Heavy Rain': len(heavy_rain_data),
        'Snow': len(snow_data),
        'Total Rain': len(rain_data),
        'Others': len(others_data)
    }
    
    return dict

WC = df.loc['Weather code'].apply(weather_code_sort)

dfWC = pd.DataFrame(WC.tolist(), index=WC.index)
