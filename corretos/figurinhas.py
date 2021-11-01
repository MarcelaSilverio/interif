# **** Alunas *************************
# Bruna C. Sanches ------(201811130054)
# Izabela A. Andrade ---- (20192004795)
# Marcela P. Silvério ----(20192020028)
# Tássyla L. Lima ------- (20192001990)
# Turma: INF3A
# *************************************

from decimal import Decimal

valor = Decimal(input()[2:])
moedas = [int(num) for num in input().split()]
total = Decimal(moedas[0]*Decimal(0.25) + moedas[1]*Decimal(0.10) + moedas[2]*Decimal(0.05) + moedas[3]*Decimal(0.01))

num_pacotes = int(total//valor)

for pacote in range(0, num_pacotes):
    aux_val = Decimal(valor)

    while Decimal(aux_val) >= Decimal(0.25) and moedas[0] > 0:
        aux_val = Decimal(aux_val) - Decimal(0.25)
        moedas[0] -= 1

    while Decimal(aux_val) >= Decimal(0.10) and moedas[1] > 0:
        aux_val = Decimal(aux_val) - Decimal(0.10)
        moedas[1] -= 1
  
    while Decimal(aux_val) >= Decimal(0.05) and moedas[2] > 0:
        aux_val = Decimal(aux_val) - Decimal(0.05)
        moedas[2] -= 1

    while Decimal(aux_val) >= Decimal(0.01) and moedas[3] > 0:
        aux_val = Decimal(aux_val) - Decimal(0.01)
        moedas[3] -= 1


print(num_pacotes)
print(moedas[0]+moedas[1]+moedas[2]+moedas[3])