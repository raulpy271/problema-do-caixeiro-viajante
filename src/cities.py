
from array import array
from math import sqrt

class Cities:

    def __init__(self, cordenadas):
        if len(cordenadas) % 2 == 0:
            self.cordenadas_array: array = array('f', cordenadas)
            self.cities_quantidade =  len(cordenadas) / 2
        else:
            raise Exception('A quantidade de cordenadas deve ser um número par')
    
    def obtem_distancia(self, origem_indice: int, destino_indice: int) -> int:
        origem_x, origem_y = self.cordenadas_array[origem_indice * 2],  self.cordenadas_array[(origem_indice * 2) + 1]
        destino_x, destino_y = self.cordenadas_array[destino_indice * 2],  self.cordenadas_array[(destino_indice * 2) + 1]
        return sqrt(
            ((destino_x - origem_x) ** 2) + ((destino_y - origem_y) ** 2)
        )
    
    def obtem_quantidade_de_cidades(self):
        return self.cities_quantidade
