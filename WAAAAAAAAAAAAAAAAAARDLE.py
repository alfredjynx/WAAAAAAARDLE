import random
from palavras import palavras
from funções import *
continuar = True
dicio_rodadas = {1:0,2:0,3:0,4:0,5:0,6:0,"não acertou":0}
rodadas = 0
# grande repetição que pergunta ao jogador se ele gostaria de jogar novamente
while continuar == True:
  # reseta o número de tentativas e dá as boas-vindas ao jogador toda vez que ele reinicia ou inicia o jogo (incluind o alfabeto que guarda o valor de cor associado a cada letra)
  tentativas = 6
  tentativas_necessarias = 0
  dicio_alfabeto = {"a":" ","b":" ","c":" ","d":" ","e":" ","f":" ","g":" ","h":" ","i":" ","j":" ","k":" ","l":" ","m":" ","n":" ","o":" ","p":" ","q":" ","r":" ","s":" ","t":" ","u":" ","v":" ","w":" ","x":" ","y":" ","z":" ","ç":" "}
  print(f"bem vindo...")
  print("")
  print("")
  # fonte: Bloody    texto: waaaaaardle   site: https://patorjk.com/software/taag/#p=display&f=3D%20Diagonal&t=obrigado%20por%20jogar
  print('''

  █     █░ ▄▄▄      ▄▄▄      ▄▄▄      ▄▄▄      ▄▄▄      ▄▄▄       ██▀███  ▓█████▄  ██▓    ▓█████ 
  ▓█░ █ ░█░▒████▄   ▒████▄   ▒████▄   ▒████▄   ▒████▄   ▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▓██▒    ▓█   ▀ 
  ▒█░ █ ░█ ▒██  ▀█▄ ▒██  ▀█▄ ▒██  ▀█▄ ▒██  ▀█▄ ▒██  ▀█▄ ▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒██░    ▒███   
  ░█░ █ ░█ ░██▄▄▄▄██░██▄▄▄▄██░██▄▄▄▄██░██▄▄▄▄██░██▄▄▄▄██░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒██░    ▒▓█  ▄ 
  ░░██▒██▓  ▓█   ▓██▒▓█   ▓██▒▓█   ▓██▒▓█   ▓██▒▓█   ▓██▒▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░██████▒░▒████▒
  ░ ▓░▒ ▒   ▒▒   ▓▒█░▒▒   ▓▒█░▒▒   ▓▒█░▒▒   ▓▒█░▒▒   ▓▒█░▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▓  ░░░ ▒░ ░
    ▒ ░ ░    ▒   ▒▒ ░ ▒   ▒▒ ░ ▒   ▒▒ ░ ▒   ▒▒ ░ ▒   ▒▒ ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░ ░ ░  ░
    ░   ░    ░   ▒    ░   ▒    ░   ▒    ░   ▒    ░   ▒    ░   ▒     ░░   ░  ░ ░  ░   ░ ░      ░   
      ░          ░  ░     ░  ░     ░  ░     ░  ░     ░  ░     ░  ░   ░        ░        ░  ░   ░  ░
                                                                            ░                     
                                                                            
                                                                            ''')
  print("")
  print("")
  # rápida e sucinta explicação das regras, copiada (literalmente) da explicação providenciada pelos professores nas regras do projeto
  print('''
  🟩 Correto: Letra está presente na palavra e se encontra na posição correta;
  🟨 Presente: Letra está presente na palavra, porém não se encontra na posição correta;
  ⬜ Ausente: Letra não está presente na palavra
  ''')
  print("")
  print("")
  print("")
  print("")
  colorido = ""
  num_palavra = random.randint(0,len(palavras)-1)
  palavra = palavras[num_palavra]
  lista_chutes = []
  lista_coloridos = []
  # servia para eu testar com palavras que eu já conhecia ou com as palavras da lista (por isso o print(palavra))
  # palavra = "mengo"
  # print(palavra)

  # retiro os acentos da palavra sem acento, mas mantenho eles na palavra original que vai no print final
  palavra_sem_acento = remove_acentos(palavra)
  # while do jogo em si, ele roda se o número de tentativas for maior que 0 e se o "colorido" (união de cores que representam o que o jogador acertou em cada rodada) for diferente do que tudo certo (5 quadrados verdes)
  while tentativas>0 and colorido!="🟩🟩🟩🟩🟩":
      print(f"você tem {tentativas} tentativas restando")
      print("")
      player_chute = ""
      # verifica a entrada do jogador, validando-a
      while len(player_chute) != 5:
          player_chute = input("Escolhe uma palavra ae: ").lower()
          if len(player_chute) != 5 or player_chute not in palavras:
          # if len(player_chute) != 5:
              print("Sua escolha não tinha 5 letras ou não estava na lista de palavras oficiais, escolha uma outra palavra")
              player_chute = ""
      print("")
      print(f"você tem {tentativas-1} tentativas, agora")
      print("")
      # esse print serve para que as letra fiquem mais centralizadas com cada quadrado colorido que a representa
      print(f" {player_chute[0]} {player_chute[1]} {player_chute[2]} {player_chute[3]} {player_chute[4]}")
      lista_chutes.append(player_chute)
      player_chute = remove_acentos(player_chute)
      # devolve esses quadrados coloridos, recebendo o chute do jogador e a palavra sorteada sem acentos
      colorido = checa_letra(player_chute,palavra_sem_acento)
      lista_coloridos.append(colorido)
      print(colorido)
      print("")
      print("")
      # utiliza o colorido, o chute e um dicionário de letras para devolver informações sobre cada letra jogada para o jogador
      dicio_alfabeto = print_teclado(player_chute,colorido,dicio_alfabeto)
      print("")
      print("")
      tentativas-=1
      tentativas_necessarias+=1
  # se o jogador acertar tudo, ele ganha o jogo
  if colorido == "🟩🟩🟩🟩🟩":
    print("Parabéns!!!")
    print(f"Você acertou a palavra em {tentativas_necessarias} tentativas!!!")
    dicio_rodadas[tentativas_necessarias]+=1
  # qualquer coisa que não seja a vitória é derrota
  else:
    print("Sua tentativas se esgotaram...")
    print("")
    print(f"A palavra era {palavra}")
    dicio_rodadas["não acertou"]+=1
  print("")
  print("")
  resposta = ""
  rodadas+=1
  while resposta!="n" and resposta!="s":
    resposta = input("Deseja jogar novamente? Responda com [n] para NÃO ou [s] para SIM: ").lower()
    resposta = resposta.strip()
    if resposta!="n" and resposta!="s":
      print("")
      print("Responda adequadamente, por favor, eu estou preso dentro desse jogo, SOCOOOOOOORROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
      print("")
    elif resposta == "n":
      continuar = False
# fonte: 3d diagonal    texto: obrigado por jogar   site: https://patorjk.com/software/taag/#p=display&f=3D%20Diagonal&t=obrigado%20por%20jogar
print('''

                                                                                                                                                                                   
                                                                                                                                                                                   
            ,---,              ,--,                               ,---,                  ,-.----.                                                                                  
   ,---.  ,---.'|     __  ,-.,--.'|                             ,---.'|   ,---.          \    /  \    ,---.    __  ,-.              .--.   ,---.                           __  ,-. 
  '   ,'\ |   | :   ,' ,'/ /||  |,     ,----._,.                |   | :  '   ,'\         |   :    |  '   ,'\ ,' ,'/ /|            .--,`|  '   ,'\   ,----._,.            ,' ,'/ /| 
 /   /   |:   : :   '  | |' |`--'_    /   /  ' /   ,--.--.      |   | | /   /   |        |   | .\ : /   /   |'  | |' |            |  |.  /   /   | /   /  ' /   ,--.--.  '  | |' | 
.   ; ,. ::     |,-.|  |   ,',' ,'|  |   :     |  /       \   ,--.__| |.   ; ,. :        .   : |: |.   ; ,. :|  |   ,'            '--`_ .   ; ,. :|   :     |  /       \ |  |   ,' 
'   | |: :|   : '  |'  :  /  '  | |  |   | .\  . .--.  .-. | /   ,'   |'   | |: :        |   |  \ :'   | |: :'  :  /              ,--,'|'   | |: :|   | .\  . .--.  .-. |'  :  /   
'   | .; :|   |  / :|  | '   |  | :  .   ; ';  |  \__\/: . ..   '  /  |'   | .; :        |   : .  |'   | .; :|  | '               |  | ''   | .; :.   ; ';  |  \__\/: . .|  | '    
|   :    |'   : |: |;  : |   '  : |__'   .   . |  ," .--.; |'   ; |:  ||   :    |        :     |`-'|   :    |;  : |               :  | ||   :    |'   .   . |  ," .--.; |;  : |    
 \   \  / |   | '/ :|  , ;   |  | '.'|`---`-'| | /  /  ,.  ||   | '/  ' \   \  /         :   : :    \   \  / |  , ;             __|  : ' \   \  /  `---`-'| | /  /  ,.  ||  , ;    
  `----'  |   :    | ---'    ;  :    ;.'__/\_: |;  :   .'   \   :    :|  `----'          |   | :     `----'   ---'            .'__/\_: |  `----'   .'__/\_: |;  :   .'   \---'     
          /    \  /          |  ,   / |   :    :|  ,     .-./\   \  /                    `---'.|                              |   :    :           |   :    :|  ,     .-./         
          `-'----'            ---`-'   \   \  /  `--`---'     `----'                       `---`                               \   \  /             \   \  /  `--`---'             
                                        `--`-'                                                                                  `--`-'               `--`-'                        
                                        
                                        ''')
print("resumo por rodada")
print("")
print("")
print(f"Você jogou {rodadas} rodadas no total")
print("")
print("")
for num_tentativas in dicio_rodadas:
  if num_tentativas != "não acertou":
    print(f"Em {num_tentativas} tentativas: {((dicio_rodadas[num_tentativas])/rodadas)*100:.2f}%")
  else:
    print(f"Não acertou em nenhuma tentativa: {((dicio_rodadas[num_tentativas])/rodadas)*100:.2f}%")
