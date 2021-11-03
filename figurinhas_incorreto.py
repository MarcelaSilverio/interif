# **** Alunas *************************
# Bruna C. Sanches ------(201811130054)
# Izabela A. Andrade ---- (20192004795)
# Marcela P. Silvério ----(20192020028)
# Tássyla L. Lima ------- (20192001990)
# Turma: INF3A
# *************************************
import math

custo_figurinha = float(input()[2:])

moedas = list(map(int, input().split()))
val_moedas = [0.25,0.10,0.05,0.01]
dinheiro_contado = []
for i in range(len(val_moedas)):
    dinheiro_contado.append(val_moedas[i]*moedas[i])
dinheiro = sum(dinheiro_contado)

pacotes_comprados = math.floor(dinheiro/custo_figurinha)


gasto = pacotes_comprados*custo_figurinha

aux = 0
contagem_moedas = 0
moedas_usadas = 0

while gasto > 0:
    moedas_usadas = math.ceil(gasto / val_moedas[aux])
    if moedas_usadas == moedas[aux]:
        gasto = 0
        moedas[aux] = 0
    elif moedas_usadas < moedas[aux]:
        moedas[aux] = moedas[aux] - moedas_usadas
        gasto = 0
    else:
        gasto = gasto - moedas[aux] * val_moedas[aux]
        moedas[aux] = 0
    aux += 1
    if aux == 4:
        break

print(int(pacotes_comprados))
print(int(sum(moedas)))
