import jogo
import interface as inter
from math import inf


def mostrar_jogadores(player01, player02):

    print(f"01 -> jogador: {player01['nome']}  icone: {player01['icone']}")
    print(f"02 -> jogador: {player02['nome']}  icone: {player02['icone']}")


def menu_config():

    print(
        f"""
{"+="*15}
[ 1 ] ICON
[ 2 ] NOME
[ 3 ] ADVERSARIO
[ 4 ] TAMANHO
[ 5 ] SAIR
{"+="*15}
"""
    )


# mudar icon
def icone_eh_O(player):

    if player["icone"] == "O":
        return True
    return False


def mudar_icon(player01, player02):

    while True:
        print("Disposicao de icones atual:")
        mostrar_jogadores(player01, player02)

        trocar = jogo.input_s_ou_n("Trocar icone: [s/n] ")

        if trocar == "s":
            if icone_eh_O(player01):
                player01["icone"] = "X"
                player02["icone"] = "O"
                print("Disposicao de icones atual:")
                mostrar_jogadores(player01, player02)
                return player01, player02
            else:
                player01["icone"] = "O"
                player02["icone"] = "X"
                print("Disposicao de icones atual:")
                mostrar_jogadores(player01, player02)
                return player01, player02
        else:
            return player01, player02


# mudar nome
def player_escolhido():

    player = jogo.input_int("Qual sera o player: [1/2] ")

    while not jogo.input_in_range(player, 1, 2):
        player = jogo.input_int("Qual sera o player: [1/2] ")

    return int(player)


def mudar_nome(player01, player02):

    while True:
        print("Disposicao de nomes atual:")
        mostrar_jogadores(player01, player02)

        trocar = jogo.input_s_ou_n("Trocar nome: [s/n] ")

        if trocar == "s":
            if player_escolhido() == 1:
                player01["nome"] = input("Novo nome: ")
                print("Disposicao de nomes atual:")
                mostrar_jogadores(player01, player02)
                return player01, player02
            else:
                player02["nome"] = input("Novo nome: ")
                print("Disposicao de nomes atual:")
                mostrar_jogadores(player01, player02)
                return player01, player02
        else:
            return player01, player02


# adversario
def mudar_adv(adv):

    # adv = True, outro jogador/ adv = False, computador
    while True:
        if adv:
            print("Voce esta jogando com outro jogador!")
        else:
            print("Voce esta jogando com a maquina!")

        trocar = jogo.input_s_ou_n("Trocar adversario: [s/n] ")

        if trocar == "s":
            if adv:
                print("Voce esta jogando com a maquina!")
                return False
            else:
                print("Voce esta jogando com outro jogador!")
                return True
        else:
            return adv


# tamanho
def mudar_tam(velha, tamanho, max):

    print(f"Tamanho atual: {tamanho}")
    velha = jogo.resetar_matrix(velha, tamanho)
    inter.layout_jogo(velha, tamanho)
    tamanho = jogo.pergunta_max_min("Qual tamanho deseja jogar: [min: 3] ", 3, inf)
    velha = jogo.resetar_matrix(velha, tamanho)
    inter.layout_jogo(velha, tamanho)
    max = tamanho**2

    return tamanho, max
