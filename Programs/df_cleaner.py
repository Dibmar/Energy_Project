# This Python program is aimed at working with Gapminder csv files

# Imports of custom libraries
from src.titan_class import Titan as EDA
import src.use_plotly as graphics
import src.settings_reader as reader
import os

# Extraction of settings
dirname = os.path.dirname(__file__)
filename = dirname + '\src\settings.json'

settings = reader.read_config(path= filename)
# print(settings)

# Cleaning and plotting of the data

## Cleaning
files = settings['files']
names = settings['names']
print(files)

for a_file in range(len(files)):
    
    df = EDA(path= files[a_file])
    df.create_df()
    df.general_info()

    df.nan_manager(fill_na= True, all_of= True, value= 0)
    df.general_info()

    if list(files[a_file].split("\\"))[-1] != "electricity_generation_total.csv":
        df.new_df(position_1=26)
    
    df.store_csv(name= names[a_file], parent_directory= settings['parent_directory'])