# This Python program is aimed at working with Gapminder csv files
# This program plots the data as stated in the settings file.


# Imports of custom libraries
import src.use_plotly as graphics
import src.settings_reader as reader

# Import of libraries
import pandas as pd
import os

# Extraction of settings
dirname = os.path.dirname(__file__)
filename = dirname + '\src\settings.json'

settings = reader.read_config(path= filename)



# Get the clean data
names = settings['names']
paths = []

print('Extracting paths...')
for name in names:
    full_path = dirname + '\\Output\\' + name + '.csv'
    print(full_path)
    paths.append(full_path)
    print('-'*3)

electricity = pd.read_csv(paths[0])
hydro = pd.read_csv(paths[1])
nuclear = pd.read_csv(paths[2])

# Merging and filtering by country
country_of_choice = settings['country_of_choice']
print(f'\nCountry chosen for filtering: {country_of_choice}')

whole_data = pd.concat([electricity, hydro, nuclear])

data = whole_data.loc[whole_data.country == country_of_choice]
data = data.rename(columns={'country': 'Date'})
data['Date'] = settings['columns_of_choice']

data = data.transpose()
data.columns = data.iloc[0,:]
data = data.drop('Date', axis = 0)

# Plotting
title = f"Evolution of {country_of_choice}'s energy production in oil tonns"
name = f'{country_of_choice}_energy_production'

graphics.create_line_plot(data_frame= data, 
                        x=data.index, 
                        y=settings['columns_of_choice'], 
                        title= title, 
                        save= True,
                        name=name,
                        parent_directory= dirname,
                        destination= 'Images')