from random import randint
import interface as inter
from time import time


#validacao ---

def eh_s_ou_n(entrada):

	if entrada == 'n' or entrada == 's':
		return True
	return False


def input_s_ou_n(pergunta):
    saida = input(pergunta).strip().lower()
    
    while not eh_s_ou_n(saida):
        print("Valor digitado não eh s/n.")
        saida = input(pergunta).strip().lower()
        
    return saida

def input_int(pergunta):
    
    while True:
        try:
            saida = int(input(pergunta))
        except ValueError:
            print("entrada não numerica")
        else:
            return saida


def input_in_range(entrada, min, max):

	if min <= entrada <= max:
		return True
	
	return False


def pergunta_max_min(str, min, max):
	
	saida = input_int(str)
	while not input_in_range(saida, min, max):
		print("numero fora do intervalo.")
		saida = input_int(str)
	return saida


def escolha_player(max_coluna, max_linha, min_coluna, min_linha):


	#verifica o valor da linha
	linha_play = pergunta_max_min("Digite a linha: ", min_linha, max_linha)

	#verifica o valor da coluna
	coluna_play = pergunta_max_min("Digita a coluna: ", min_coluna, max_coluna)

	return (int(linha_play) - 1), (int(coluna_play) - 1)


def casa_ocupada(velha, player, linha, coluna, eh_jogador):

	
	if velha[linha][coluna] == " ":
		velha[linha][coluna] = player['icone']
		return False
	
	if eh_jogador:
		print("ERROR! Voce digitou uma casa ocupada.")
	return True


def jogada_player(velha, player, tamanho):
	
	while True:
		
		linha_play, coluna_play = escolha_player(tamanho,tamanho,1,1)
	
		#verifica se a casa ta ocupada
		if not casa_ocupada(velha, player, linha_play, coluna_play, True):
			return velha


def jogada_PC(velha, player,tamanho):

	while True:
		linha_PC = randint(0,tamanho-1)
		coluna_PC = randint(0,tamanho-1)
		
		if not casa_ocupada(velha, player, linha_PC, coluna_PC, False):
			print(f"Joguei na linha {linha_PC + 1} coluna {coluna_PC + 1}.")
			return velha


def jogada(velha, jogador, player01, player02, adversario, tamanho):
	
	if adversario:
		if jogador == "player01":
			velha = jogada_player(velha, player01, tamanho)
			return "player02"
		
		elif jogador == "player02":
			velha = jogada_player(velha, player02, tamanho)
			return "player01" 
	else:
		if jogador == "player01":
			velha = jogada_player(velha, player01, tamanho)
			return "player02"
		
		elif jogador == "player02":
			velha = jogada_PC(velha, player02,tamanho)
			return "player01"
	

def jogar_novamente():
	
	condicao = input("Deseja jogar novamente? [s/n] ").strip().lower()
	
	while not eh_s_ou_n(condicao):
		condicao = input("Deseja jogar novamente? [s/n] ").strip().lower()

		if not eh_s_ou_n(condicao):
			print("Valor digitado não eh s/n.")

	if condicao == 's':
		return True
	return False

def resetar_matrix(matrix, tamanho):
	
    matrix = []
    while len(matrix) < tamanho:
        linha = []
        for i in range(tamanho):
            linha.append(' ')
        matrix.append(linha)
    return matrix


def resetar(velha, jogadas, tamanho_jogo):
    
	jogadas = 0
	velha = resetar_matrix(velha, tamanho_jogo)
	
	return velha, jogadas


def linha_eh_completa(velha,tamanho):
	for i in range(tamanho):
		if velha[i][0] != " " and (len(set(velha[i])) == 1):
			return True
	return False



def coluna_eh_completa(velha, tamanho):
    for j in range(tamanho):
        verificador = []
        for i in velha:
            verificador.append(i[j])
        if verificador[0] != " " and (len(set(verificador)) == 1):
            return True
    return False



def dp_eh_completa(velha,tamanho):
    verificador = []
    for i in range(tamanho):
        for j in range(tamanho):
            if i == j:
                verificador.append(velha[i][j])
    if verificador[0] != " " and (len(set(verificador)) == 1):
            return True
    return False 



def ds_eh_completa(velha, tamanho):
    verificador = []
    for i in range(tamanho):
        for j in range(tamanho):
            if i + j == tamanho - 1:
                verificador.append(velha[i][j])
    if verificador[0] != " " and (len(set(verificador)) == 1):
            return True
    return False   



def alguem_ganhou(velha,tamanho):
	#linha completa
	if linha_eh_completa(velha, tamanho):
		return True

	#coluna completa
	if coluna_eh_completa(velha, tamanho):
		return True
	
	#diagonal principal
	if dp_eh_completa(velha, tamanho):
		return True
	
	#diagonal secundaria
	if ds_eh_completa(velha, tamanho):
		return True
	return False


def deu_velha(velha, tamanho):

	if alguem_ganhou(velha, tamanho):
		return False
	return True


def finalizar(velha, jogador, player01, player02, tamanho_jogo, adv, pc_win, player_win, draw, inicio, pc_time, player_time, draw_time):
	
	#draw
	if deu_velha(velha,tamanho_jogo):
		if not adv:
			draw += 1
			draw_time =  time() - inicio

		inter.deuVelha(velha, tamanho_jogo)

	#player 2
	elif jogador == "player01":
		if not adv:
			pc_win += 1
			pc_time =  time() - inicio

		if player02['icone'] == "X": 
			inter.x_ganhou(velha, tamanho_jogo)
		else:
			inter.o_ganhou(velha, tamanho_jogo)

	#player 1
	else:
		if not adv:
			player_win += 1
			player_time = time() - inicio

		if player01['icone'] == "X":
			inter.x_ganhou(velha, tamanho_jogo)
		else:
			inter.o_ganhou(velha, tamanho_jogo)	

	return pc_win, player_win, draw, pc_time, player_time, draw_time