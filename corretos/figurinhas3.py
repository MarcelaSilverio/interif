# **** Alunas *************************
# Bruna C. Sanches ------(201811130054)
# Izabela A. Andrade ---- (20192004795)
# Marcela P. Silvério ----(20192020028)
# Tássyla L. Lima ------- (20192001990)
# Turma: INF3A
# *************************************

valor = float(input()[2:])
moedas = [int(num) for num in input().split()]
total = moedas[0]*(0.25) + moedas[1]*(0.10) + moedas[2]*(0.05) + moedas[3]*(0.01)

num_pacotes = int(total/valor)

aux_val = valor * num_pacotes

q = int(aux_val/0.25) if int(aux_val/0.25) <= moedas[0] else moedas[0]
aux_val -= q * 0.25
moedas[0] -= q

q = int(aux_val/0.1) if int(aux_val/0.1) <= moedas[1] else moedas[1]
aux_val -= q * 0.1
moedas[1] -= q

q = int(aux_val/0.05) if int(aux_val/0.05) <= moedas[2] else moedas[2]
aux_val -= q * 0.05
moedas[2] -= q

q = int(aux_val/0.01) if int(aux_val/0.01) <= moedas[3] else moedas[3]
aux_val -= q * 0.01
moedas[3] -= q

print(num_pacotes)
print(moedas[0], moedas[1], moedas[2], moedas[3])