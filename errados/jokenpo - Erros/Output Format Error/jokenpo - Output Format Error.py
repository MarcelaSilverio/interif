# ** Alunas ****************************
# Bruna C. Sanches ------(201811130054)
# Izabela A. Andrade ---- (20192004795)
# Marcela P. Silvério ----(20192020028)
# Tássyla L. Lima ------- (20192001990)
# Turma: INF3A
# **************************************
jogador1=str(input())
jogador2=str(input())

if(jogador1 == jogador2):
    print("Empate")
elif((jogador1=="pedra" and jogador2=="tesoura") or (jogador1=="papel" and jogador2=="pedra") or (jogador1=="tesoura" and jogador2=="papel")):
    print("jogador 1") #Output Format Error
elif((jogador1=="tesoura" and jogador2=="pedra") or (jogador1=="pedra" and jogador2=="papel") or (jogador1=="papel" and jogador2=="tesoura") ):
    print("jogador 2") #Output Format Error
