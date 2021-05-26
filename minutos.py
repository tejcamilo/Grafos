import pandas
import os
df = pandas.read_csv('minutos_def.csv')
lista_minutos = df.to_numpy().tolist()
#print(lista_minutos)