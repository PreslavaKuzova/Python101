def gas_stations(distance, tank_size, stations):

    gas_stations_in_route = []
    distance_travelled = 0

    while distance_travelled + tank_size < distance:

        gas_station = max([station for station in stations if station <= distance_travelled + tank_size])
        gas_stations_in_route.append(gas_station)
        distance_travelled = gas_station

    return gas_stations_in_route