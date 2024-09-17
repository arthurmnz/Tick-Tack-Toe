from random import choice
from time import sleep


def menu():

	#nome do jogo
	print("""   ___                         _                   _ _            
  |_  |                       | |                 | | |           
    | | ___   __ _  ___     __| | __ _  __   _____| | |__   __ _  
    | |/ _ \ / _` |/ _ \   / _` |/ _` | \ \ / / _ | | '_ \ / _` | 
/\__/ | (_) | (_| | (_) | | (_| | (_| |  \ V |  __| | | | | (_| | 
\____/ \___/ \__, |\___/   \__,_|\__,_|   \_/ \___|_|_| |_|\__,_| 
              __/ |                                               
             |___/                                               """)
	
	#menu principal
	print(f"""{"+="*15}
[ 1 ] JOGAR
[ 2 ] CONFIGURACOES
[ 3 ] ESTATISTICAS
[ 4 ] SAIR
{"+="*15}
""")
	
def printar_linha(tamanho):
    for k in range(tamanho):
        print("---",end="")
        if k != (tamanho-1):
            print("+", end='')
    print()
    

def printar_linha_numerica(linha,tamanho,matrix):
    for j in range(tamanho):
        print(f" {matrix[linha][j]} ",end='')
        if j != (tamanho - 1):
            print("|", end='')
    print()


def layout_jogo(matrix, tamanho):

	#layout jogo da velha
	for i in range(tamanho):
		printar_linha_numerica(i, tamanho, matrix)
		if i != (tamanho - 1):
			printar_linha(tamanho)


def mostrarJogo(velha, jogada, jogador, player01, player02, tamanho_jogo):

	#definir aleatoriamente o primeiro a jogar
	if jogada == 0:
		jogador = choice(["player01","player02"])

	#mostra quem esta jogando
	if jogador == "player01":
		print(f"VEZ DO {player01['nome']}")
	elif jogador == "player02":
		print(f"VEZ DO {player02['nome']}")
	
	layout_jogo(velha, tamanho_jogo)
	
	#adiciona o numero de jogadas e impreme em qual jogada esta
	jogada += 1
	print(f"Jogada Número: {jogada}")
	return jogada, jogador

	
def deuVelha(velha, tamanho_jogo):

	layout_jogo(velha, tamanho_jogo)
	print("""
           _ _           
          | | |          
__   _____| | |__   __ _ 
\ \ / / _ | | '_ \ / _` |
 \ V |  __| | | | | (_| |
  \_/ \___|_|_| |_|\__,_|	                          
\n""")
	

def o_ganhou(velha, tamanho_jogo):

    layout_jogo(velha, tamanho_jogo)
    print("""
 _____                        _                 
|  _  |                      | |                
| | | |      __ _  __ _ _ __ | |__   ___  _   _ 
| | | |     / _` |/ _` | '_ \| '_ \ / _ \| | | |
\ \_/ /    | (_| | (_| | | | | | | | (_) | |_| |
 \___/      \__, |\__,_|_| |_|_| |_|\___/ \__,_|
             __/ |                              
            |___/                               	                                 
\n""")

	

def x_ganhou(velha, tamanho_jogo):

	layout_jogo(velha, tamanho_jogo)
	print("""
__   __                       _                 
\ \ / /                      | |                
 \ V /       __ _  __ _ _ __ | |__   ___  _   _ 
 /   \      / _` |/ _` | '_ \| '_ \ / _ \| | | |
/ /^\ \    | (_| | (_| | | | | | | | (_) | |_| |
\/   \/     \__, |\__,_|_| |_|_| |_|\___/ \__,_|
             __/ |                              
            |___/                                                                
\n""")

