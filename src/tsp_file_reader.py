
import re
from src.cities import CaminhoDoCaixeiro


def reader(path: str) -> tuple[dict, CaminhoDoCaixeiro] :
    caminho: CaminhoDoCaixeiro = []
    cordenadas_re = re.compile('\d+ (\d+\.\d+) (\d+\.\d+)\n')
    with open(path, 'rt') as f:
        lines = f.readlines()

    for linha_com_cordenada in lines[7:-1]: 
        match_obj = cordenadas_re.fullmatch(linha_com_cordenada)
        if match_obj:
            x, y = match_obj.groups()
            caminho.append((float(x), float(y)))
        else:
            raise Exception(f'Linha com erro de sintaxe: {linha_com_cordenada}')
    return {}, caminho

