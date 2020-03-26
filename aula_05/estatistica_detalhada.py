from typing import Dict, Union, List


class EstatisticaDetalhada:
    def __init__(self, agencia, dia):
        self.agencia = agencia
        self.dia = dia

    def roda_estatistica(self, clientes_atendidos: List[str]):
        estatistica: Dict[str, Union[int, str, List[str]]] = {}

        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['quantidade de clientes atendidos'] = (
            len(clientes_atendidos)
        )
        estatistica['clientes atendidos'] = clientes_atendidos
        
        return estatistica
