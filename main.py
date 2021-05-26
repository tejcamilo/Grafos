from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from poblacion_data import poblacion
from minutos import lista_minutos
import math

cap_camiones = 10000  # Capacidad de vacunas de los camiones
num_camiones = 17   # Número de camiones a utilizar
vacunas_disponibles = 80000  # Vacunas disponibles en el centro principal

# El problema se resuelve como si el camión saliera vacío, recogiera vacunas y
#  volviera con una capacidad menor a la máxima. Es análogo a que saliera con
# menos de la capacidad máxima, reparta y vuelva vacío


def create_data():  # Se crea un diccionario con la información que necesita el problema
    data = {}
    data['distance_matrix'] = lista_minutos
    data['num_vehicles'] = num_camiones
    data['truck_capacities'] = []
    for i in range(num_camiones):
        data['truck_capacities'].append(cap_camiones)
    data['demanda'] = [0]
    for pob_municipio in poblacion:  # Se calcula las vacunas que necesita cada municipio como una proporción de la población a vacunar y las vacunas disponibles
        data['demanda'].append(math.floor(
            pob_municipio/sum(poblacion)*vacunas_disponibles))
    data['depot'] = 0
    return data

def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    total_distance = 0
    total_load = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data['demands'][node_index]
            plan_output += ' {0} Load({1}) -> '.format(node_index, route_load)
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += ' {0} Load({1})\n'.format(manager.IndexToNode(index),
                                                 route_load)
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        plan_output += 'Load of the route: {}\n'.format(route_load)
        print(plan_output)
        total_distance += route_distance
        total_load += route_load
    print('Total distance of all routes: {}m'.format(total_distance))
    print('Total load of all routes: {}'.format(total_load))

def main():
    data = create_data()  # Traemos la info
    manager = pywrapcp.RoutingIndexManager(  # Objeto para indexar adecuadamente los nodos
        len(data['distance_matrix']), data['num_vehicles'], data['depot'])
    routing = pywrapcp.RoutingModel(manager)

    # Retorna el tiempo en minutos que hay entre 2 municipios
    def tiempo2municipios(index1, index2):
        # Convertir de índice a nodo
        nodo1 = manager.IndexToNode(index1)
        nodo2 = manager.IndexToNode(index2)
        return data['distance_matrix'][nodo1][nodo2]

    # Registramos esta función como un nuevo atributo que el solver necesitará
    time_callback_index = routing.RegisterTransitCallback(tiempo2municipios)
    # Definimos el peso de cada arista
    routing.SetArcCostEvaluatorOfAllVehicles(time_callback_index)

    # Función para saber la demanda de 1 municipio
    def demanda1municipio(index):
        nodo = manager.IndexToNode(index)
        return data['demanda'][nodo]

    # Registramos la función como atributo que el solver necesita
    demanda_municipio_index = routing.RegisterUnaryTransitCallback(
        demanda1municipio)

    # Se añade una dimensión para que cada camión verifique qué capacidad lleva para no sobrepasarla
    routing.AddDimensionWithVehicleCapacity(
        demanda_municipio_index,0,
        data['truck_capacities'],
        True,  # Hace que la capacidad inicial sea 0
        'Capacity')  # Nombre

    # Búsqueda de la primera solución factible
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    #Busca un circuito comenzando desde el punto inicial que va escogiendo la arista con el menor coste
    search_parameters.first_solution_strategy = ( 
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)
    # Utiliza métodos heurísticos para encontrar una mejor solución
    search_parameters.local_search_metaheuristic = (routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH)
    search_parameters.time_limit.FromSeconds(86400)

    #Solucionar el problema
    solucion = routing.SolveWithParameters(search_parameters)

    print_solution(data,manager, routing,solucion)
main()

