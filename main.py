import interface as inter
import arquivo as arqui
from time import time
import config
import jogo

tamanho_jogo = 3
adversario = False
player01 = {"nome": "jogador 1", "icone": "X"}
player02 = {"nome": "jogador 2", "icone": "O"}
jogador = "X"
jogadas = 0
max_jogadas = 9
velha = []

arqui.criar_arquivo("vitorias.txt")
arqui.criar_arquivo("tempo.txt")

pc_win, player_win, draw = arqui.pegar_info("vitorias.txt")
pc_time, player_time, draw_time = arqui.pegar_info("tempo.txt")

while True:
    inter.menu()
    escolha = jogo.pergunta_max_min("Digite sua escolha: ", 1, 4)

    # jogar
    if escolha == 1:
        inicio = time()
        velha = jogo.resetar_matrix(velha, tamanho_jogo)

        while True:
            jogadas, jogador = inter.mostrarJogo(
                velha, jogadas, jogador, player01, player02, tamanho_jogo
            )

            jogador = jogo.jogada(
                velha, jogador, player01, player02, adversario, tamanho_jogo
            )

            if jogadas == max_jogadas or jogo.alguem_ganhou(velha, tamanho_jogo):

                pc_win, player_win, draw, pc_time, player_time, draw_time = (
                    jogo.finalizar(
                        velha,
                        jogador,
                        player01,
                        player02,
                        tamanho_jogo,
                        adversario,
                        pc_win,
                        player_win,
                        draw,
                        inicio,
                        pc_time,
                        player_time,
                        draw_time,
                    )
                )

                arqui.atualizar_arquivo("vitorias.txt", pc_win, player_win, draw)
                arqui.verificar_tempo("tempo.txt", pc_time, player_time, draw_time)

                if jogo.jogar_novamente():
                    velha, jogadas = jogo.resetar(velha, jogadas, tamanho_jogo)
                    inicio = time()
                    continue

                else:
                    velha, jogadas = jogo.resetar(velha, jogadas, tamanho_jogo)
                    break

    # configuracoes
    elif escolha == 2:
        while True:
            config.menu_config()
            escolha_config = jogo.pergunta_max_min("Digite sua escolha: ", 1, 5)

            if escolha_config == 1:
                # icon
                player01, player02 = config.mudar_icon(player01, player02)

            elif escolha_config == 2:
                # nome
                player01, player02 = config.mudar_nome(player01, player02)

            elif escolha_config == 3:
                # adversario
                adversario = config.mudar_adv(adversario)

            elif escolha_config == 4:
                # tamanho
                tamanho_jogo, max_jogadas = config.mudar_tam(
                    velha, tamanho_jogo, max_jogadas
                )

            elif escolha_config == 5:
                break

                # estatisticas
    elif escolha == 3:
        arqui.mostrar_arquivo("vitorias.txt", "tempo.txt")

    # sair
    elif escolha == 4:
        break
