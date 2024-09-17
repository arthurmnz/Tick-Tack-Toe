#open("caminho","mode")

# modes
# r read
# a append adiciona ao arquivo
# w write reescre o arquivo
# x create
# r+ read and write

#.readable() se pode ser lido
#.read() ler o arquivo todo
#.readline() ler a linha do arquivo
#.readlines() transforma o arquivo em uma lista

#.write() adiciona ao final do arquivo
#.writelines() adiciona listas

def criar_arquivo(nome_arquivo):
    try:
        arqui = open(f"{nome_arquivo}","x")
    except:
        pass
    else:
        arqui.close()
        arqui = open(f"{nome_arquivo}","w")
        arqui.write("0\n0\n0\n")
        arqui.close()
     

def pegar_info(nome_arquivo):    
    arqui = open(f"{nome_arquivo}","r")

    lista = arqui.readlines()
    pc = float(lista[0].replace("\n",""))
    player = float(lista[1].replace("\n",""))
    draw = float(lista[2].replace("\n",""))

    arqui.close()
    return pc, player, draw


def atualizar_arquivo(nome_arquivo, pc, player, draw):
    arqui = open(f"{nome_arquivo}","w")

    arqui.write(f"{pc}\n{player}\n{draw}\n")

    arqui.close()


def mostrar_arquivo(nome_arquivo01,nome_arquivo02):
    pc_win, player_win, draw = pegar_info(nome_arquivo01)

    pc_time, player_time, draw_time = pegar_info(nome_arquivo02)
    
    arquivo_vit = open(f"{nome_arquivo01}","r")
    arquivo_time = open(f"{nome_arquivo02}","r")
    
    print ("       | Vitorias | Tempo ")
    print ("==========================")
    print(f"Pc     |{pc_win:^10.0f}|{pc_time:^7.2f}")
    print(f"Player |{player_win:^10.0f}|{player_time:^7.2f}")
    print(f"Draw   |{draw:^10.0f}|{draw_time:^7.2f}")
   
    arquivo_vit.close()
    arquivo_time.close()


def verificar_tempo(nome_arquivo, pc_time, player_time, draw_time):
    pc, player, draw = pegar_info(nome_arquivo)
    if pc > pc_time or pc == 0:
        pc = pc_time
        
    if player > player_time or player == 0:
        player = player_time
        
    if draw > draw_time or draw == 0:
        draw = draw_time
    atualizar_arquivo('tempo.txt',pc, player, draw)