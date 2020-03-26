from typing import Dict, List


class EstatisticaResumida:
    def __init__(self, agencia, dia):
        self.agencia = agencia
        self.dia = dia
        
    def roda_estatistica(self, clientes_atendidos: List[str]):
        estatistica: Dict[str, Union[int, str, List[str]]] = {}

        estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)

        return  estatistica
