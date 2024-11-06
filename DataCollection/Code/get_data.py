import json 
import requests

def get_data(city_name, country_code):

    with open('../Data/world_cities.csv') as file:

            lines = file.read().split('\n')
        
    dict_list = []

    for line in lines:
        line_elements = line.split(',')
        if len(line_elements) != 4: 
             pass 
        else:
            current_dictionary = {
            'cities_name': line_elements[1],
            'country_code': line_elements[0],
            'latitude': line_elements[2],
            'longitude': line_elements[3]
            }
            dict_list.append(current_dictionary)
    for dict in dict_list:
        if dict['cities_name'] == str(city_name) and dict['country_code'] == str(country_code):
            latitude = dict['latitude']
            longitude = dict['longitude'] # define valuables used for codes to follow

    base_historic_url =  "https://archive-api.open-meteo.com/v1/era5?"
    params_lat_long = "latitude=" + str(latitude) + "&longitude="  + str(longitude)
    params_date = "&start_date=2023-01-01&end_date=2024-01-01"

    params_others = "&hourly=&daily=weather_code,precipitation_sum,rain_sum,showers_sum,precipitation_hours"

    final_url = base_historic_url + params_lat_long + params_date + params_others

    response = requests.get(final_url)

    data = response.json()

    raininess = {
         'Date': data['daily']['time'],
         'Weather code': data['daily']['weather_code'],
         'Precipitation sum': data['daily']['precipitation_sum'],
         'Rain sum': data['daily']['rain_sum'],
         'Shower sum': data['daily']['showers_sum'],
         'Precipitation hours': data['daily']['precipitation_hours']
    }
    return raininess

london_data = get_data('London', 'GB')
porto_novo_data = get_data('Porto Novo', 'CV')
kigali_data = get_data('Kigali', 'RW')
apia_data = get_data('Apia', 'WS')
tiraspol_data = get_data('Tiraspol', 'MD')
dublin_data = get_data('Dublin', 'IE')
ljubljana_data = get_data('Ljubljana', 'SI')
kuwait_city_data = get_data('Kuwait City', 'KW')
bangkok_data = get_data('Bangkok', 'TH')
santo_domingo_data = get_data('Santo Domingo', 'CO')
brasileia_data = get_data('Brasiléia', 'BR')

mega_dict = {
    'London': london_data,
    'Porto Novo': porto_novo_data,
    'Kigali': kigali_data,
    'Apia': apia_data,
    'Tiraspol': tiraspol_data,
    'Dublin': dublin_data,
    'Ljubljana': ljubljana_data,
    'Kuwait City': kuwait_city_data,
    'Bangkok': bangkok_data,
    'Santo Domingo': santo_domingo_data,
    'Brasiléia': brasileia_data
}

with open("../Data/all_data.json", "w") as file:
    json.dump(mega_dict, file)