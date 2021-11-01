# **** Alunas *************************
# Bruna C. Sanches ------(201811130054)
# Izabela A. Andrade ---- (20192004795)
# Marcela P. Silvério ----(20192020028)
# Tássyla L. Lima ------- (20192001990)
# Turma: INF3A
# *************************************

import math

tamanho_percurso, velocidade_rogerinho, tempo_corrida = map(int, input().split())
tamanho_percurso_km = tamanho_percurso/1000
saida = (velocidade_rogerinho/tamanho_percurso_km)*tempo_corrida
print(saida) # Erro Induzido - Resultado não arredondado/truncado
