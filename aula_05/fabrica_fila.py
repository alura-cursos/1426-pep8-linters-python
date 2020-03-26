from typing import Union

from constants import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria

class FabricaFila:
	@staticmethod
	def pega_fila(tipo_fila) -> Union[TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA]:
		if tipo_fila == TIPO_FILA_NORMAL:
			return FilaNormal()
		elif tipo_fila == TIPO_FILA_PRIORITARIA:
			return FilaPrioritaria()
		else:
			raise NotImplementedError('Tipo não cadastrado')
