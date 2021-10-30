# Base
import pandas as pd
import numpy as np
import sqlite3

# Data
path=('C:/Users/guillermo.mgarcia/Documents/GitHub/Seminario_9273/Tarea 1/Bases/')
bd1 = 'base_ini_interna.csv'
bd2 = 'base_ini_parte1.csv'
bd3 = 'base_ini_externa.txt'
bd4 = 'base_inversion.txt'
bd5 = 'base_comportamiento_2.txt'
bd6 = 'base_comportamiento_3.csv'
bd7 = 'bd_inicio_parte1.txt'

ini_interna = pd.read_csv(path + bd1)
ini_parte_1 = pd.read_csv(path + bd2)
ini_externa = pd.read_csv(path + bd3, sep=' ')
inversion = pd.read_csv(path + bd4, sep =' ')
comportamiento_2 = pd.read_csv(path + bd5, sep =' ')
comportamiento_3 = pd.read_csv(path + bd6)
inicio_parte_1 = pd.read_csv(path + bd7, sep =' ')

# Missing values
missing_data=ini_externa.isnull()

for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")
