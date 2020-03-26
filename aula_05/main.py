from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada


# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# print(fila_teste_2.chama_cliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

# teste_fabrica = FabricaFila.pega_fila('normal')
# teste_fabrica.atualizafila()
# teste_fabrica.atualizafila()
# teste_fabrica.atualizafila()
# print(teste_fabrica.chama_cliente(10))

fila = FabricaFila.pega_fila('prioritaria')
fila.atualizafila()
fila.atualizafila()
fila.atualizafila()
print(fila.chama_cliente(5))
print(fila.estatistica(EstatisticaResumida('20/03/2025', 1245)))
