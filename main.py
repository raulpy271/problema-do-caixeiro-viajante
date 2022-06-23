
from src.cities import Cities
from src.tsp_file_reader import reader

if __name__ == '__main__':
    path = 'data-samples/wi29.tsp'
    _, cities = reader(path)
    print(cities.obtem_distancia(0, 1))