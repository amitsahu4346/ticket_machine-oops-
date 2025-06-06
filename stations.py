class Station:
    '''Models each station'''
    def __init__(self, name, distance, cost):
        self.name = name
        self.distance = distance 
        self.cost = cost


class Stations:
    '''Models the stations'''
    def __init__(self):
        self.stations = [
            Station(name="Sanchi", distance=10, cost=20),
            Station(name="Bhopal", distance=15, cost=25),
            Station(name="Makshi", distance=25, cost=40),
            Station(name="Ujjain", distance=30, cost=45),
            Station(name="Indore", distance=40, cost=60)
        ]


    def get_stations(self):
        '''Return all the stations'''
        options = ""
        for station in self.stations:
            options = options + f"\n{station.name}, Cost: {station.cost}"
        return options

    def find_station(self, station_name):
        '''Searches the station and return it, if not found return None'''
        for station in self.stations:
            if station.name == station_name:
                return station
        