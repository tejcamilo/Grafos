from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from poblacion_data import poblacion
import math

cap_camiones = 10000
num_camiones = 15
vacunas_disponibles = 80000


def create_data():
    data = {}
    data['distance_matrix'] = []
    data['num_vehicles'] = 4
    data['truck_capacities'] = []
    for i in range(num_camiones):
        data['truck_capacities'].append(cap_camiones)
    data['demanda'] = []
    for pob_municipio in poblacion:
        data['demanda'].append(math.floor(
            pob_municipio/sum(poblacion)*vacunas_disponibles))
    data['depot'] = []
    return data


def main():
    data = create_data()
    manager = pywrapcp.RoutingIndexManager(
        len(data['distance_matrix']), data['num_vehicles'], data['depot'])


data = create_data()
print(sum(data['demanda']))
# print(sum(poblacion))
