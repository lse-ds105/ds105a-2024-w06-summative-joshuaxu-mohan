import random

def randomiser(number):
    with open("../Data/CapitalCitiesList.csv") as file:

        lines = file.read().split('\n')

        dict_list = []

        for line in lines[1:]: 
            line_elements = line.split(',')
            if len(line_elements) != 3: 
                pass
            else:
                dict = {
                    'Country': line_elements[0],
                    'Capital': line_elements[1]
                }
                dict_list.append(dict)

    sample_capitals = []
    for i in range(int(number)): 
        sample_capitals.append(random.choice(dict_list))
    
    for capitals in sample_capitals:
        print(capitals)

sample = randomiser(10)