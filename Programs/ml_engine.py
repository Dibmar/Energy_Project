# This Python program is aimed at working with Gapminder csv files
# This program creates and evaluates a Machine Learning model.


# Imports of custom libraries
from src.modeler import Model_Maker as MM
import src.settings_reader as reader

# Import of libraries
import pandas as pd
import os

# Extraction of settings
dirname = os.path.dirname(__file__)
filename = dirname + '\src\settings.json'

settings = reader.read_config(path= filename)
path = dirname + '\\Output\\nuclear_engergy_sliced.csv'

# Creation of dataframe
df_to_read = pd.read_csv(path)

# Creation of model
manager = MM(dataframe= df_to_read)
manager.data_splitter(range_of_columns= [1,-1], index_test= -1)
manager.create_linear_or_logistic_model(kind= 'linear')