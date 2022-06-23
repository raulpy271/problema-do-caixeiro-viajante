
import re
from src.cities import Cities


def reader(path: str) -> "tuple[dict, Cities]" :
    cities_arr = []
    cordenadas_re = re.compile('\d+ (\d+\.\d+) (\d+\.\d+)\n')
    with open(path, 'rt') as f:
        lines = f.readlines()

    for linha_com_cordenada in lines[7:-1]: 
        match_obj = cordenadas_re.fullmatch(linha_com_cordenada)
        if match_obj:
            x, y = match_obj.groups()
            cities_arr.append(float(x))
            cities_arr.append(float(y))
        else:
            raise Exception(f'Linha com erro de sintaxe: {linha_com_cordenada}')
    return {}, Cities(cities_arr)

