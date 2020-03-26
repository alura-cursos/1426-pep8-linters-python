from typing import Dict, Union, List

from fila_base import FilaBase
from constantes import CODIGO_PRIORITARIO


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{CODIGO_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> None:
        display = []
		cliente_atual = self.fila.pop(0)
		display.append(f'Cliente: ]{cliente_atual} - Caixa {caixa}')

		if len(self.fila) >= 3:
			display.append(f'Próximo: {self.fila[0]}')
			display.append(f'Fique atento: {self.fila[1]}')

		self.clientes_atendidos.append(cliente_atual)

		return display
        
    def estatistica(self, dia: str, agencia: str, flag: str) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}

        if flag != 'detail':
            estatistica[f'{agencia} - {dia}'] = len(self.clientes_atendidos)
        else:
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes atendidos'] = self.clientes_atendidos
            estatistica['quantidade de clientes atendidos'] = (
                len(self.clientes_atendidos)
            )   
            
        return estatistica
