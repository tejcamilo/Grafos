from os import replace
import pandas
from unidecode import unidecode

df = pandas.read_csv('poblacion.csv',header = None)
df.columns = ['Municipio','Población total','Población']
df.sort_values(by=['Municipio'])
municipios = df.sort_values(by=['Municipio'])['Municipio'].tolist()
poblacion = df.sort_values(by=['Municipio'])['Población'].tolist()
count = 0
for n in poblacion:
    if " " in n:
        poblacion[count] = n.replace(" ","")
    count += 1
poblacion = list(map(int,poblacion))
total_personas = df['Población'].sum()
#print(poblacion)
#print(municipios)
#print(df.to_string())

# df2 = pandas.read_csv('Grafos - Sheet4.csv')
# #print(df2)
# df2.rename(columns={'Unnamed: 0':'Municipio'}, inplace=True)
# municipios2 = df2['Municipio'].tolist()
# index = 0
# for str in municipios2:
#     if 'Á' in str:
#         municipios2[index] =str.replace("Á","A")
#     if 'É' in str:
#          municipios2[index]=str.replace('É','E')
#     if 'Í' in str:
#         municipios2[index]=str.replace('Í','I')
#     if 'Ó' in str:
#         municipios2[index]=str.replace('Ó','O')
#     if 'Ú' in str:
#         municipios2[index]=str.replace('Ú','U')
#     index +=1

#print(municipios2)
# dff = pandas.DataFrame(municipios,municipios2)
# print(dff.to_string())
# print(municipios2==municipios)