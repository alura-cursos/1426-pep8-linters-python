from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from fabrica_fila import FabricaFila


# fila_teste = filanormal()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# fila_teste.atualizafila()
# print(fila_teste.chamacliente(5))
# print(fila_teste.chamacliente(10))

# fila_teste_2 = FilaPrioritaria()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# fila_teste_2.atualizafila()
# print(fila_teste_2.chamacliente(10))
# print(fila_teste_2.estatistica('10/01/1993', 198, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualizafila()
teste_fabrica.atualizafila()
teste_fabrica.atualizafila()
print(teste_fabrica.chamacliente(10))
