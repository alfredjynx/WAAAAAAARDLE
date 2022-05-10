import unicodedata

# função que recebe a plavra sorteada e o "chute" do jogador e retorna uma string colorida que representa o que o jogador acertou ou não
def checa_letra(chute,palavra_sort):
    palavra_cores = ["","","","",""]

    letras_unicas_chute = {}
    for letra in palavra_sort:
        if letra not in letras_unicas_chute:
            letras_unicas_chute[letra]=1
        else:
            letras_unicas_chute[letra]+=1
    
    i = 0
    for letra in chute:
        if letra == palavra_sort[i] and letras_unicas_chute[letra]>0:
            palavra_cores[i]="🟩"
            
        else:
            if letra in letras_unicas_chute and letras_unicas_chute[letra]>0:
                palavra_cores[i]="🟨"
            else:
                palavra_cores[i]="⬜"

        if letra in letras_unicas_chute:
            letras_unicas_chute[letra]-=1
        
        
        i+=1

    palavra = ""

    for cor in palavra_cores:
        palavra+=cor
    
    return palavra


# Função originária do Quiz 4, de dicionários, que vem do stackoverflow
def remove_acentos(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


def print_teclado(chute,colorido,dicio_alfabeto):
    
    i = 0
    for letra in chute:
        cor = colorido[i]
        cor_dicio = dicio_alfabeto[letra]
        if cor_dicio == " ":
            dicio_alfabeto[letra] = cor
        elif cor_dicio == "⬜":
            dicio_alfabeto[letra] = cor
        else:
            if cor_dicio == "🟨" and cor == "🟩":
                dicio_alfabeto[letra] = cor
        i+=1

    print('''

 _            _           _       
| |_ ___  ___| | __ _  __| | ___  
| __/ _ \/ __| |/ _` |/ _` |/ _ \ 
| ||  __/ (__| | (_| | (_| | (_) |
 \__\___|\___|_|\__,_|\__,_|\___/ 
                                  
                                  
    ''')
    
    print(f'''
    [Q]{dicio_alfabeto["q"]}  [W]{dicio_alfabeto["w"]}  [E]{dicio_alfabeto["e"]}  [R]{dicio_alfabeto["r"]}  [T]{dicio_alfabeto["t"]}  [Y]{dicio_alfabeto["y"]}  [U]{dicio_alfabeto["u"]}  [I]{dicio_alfabeto["i"]}  [O]{dicio_alfabeto["o"]}  [P]{dicio_alfabeto["p"]}  

         [A]{dicio_alfabeto["a"]}  [S]{dicio_alfabeto["s"]}  [D]{dicio_alfabeto["d"]}  [F]{dicio_alfabeto["f"]}  [G]{dicio_alfabeto["g"]}  [H]{dicio_alfabeto["h"]}  [J]{dicio_alfabeto["j"]}  [K]{dicio_alfabeto["k"]}  [L]{dicio_alfabeto["l"]}  

            [Z]{dicio_alfabeto["z"]}  [X]{dicio_alfabeto["x"]}  [C]{dicio_alfabeto["c"]}  [V]{dicio_alfabeto["v"]}  [B]{dicio_alfabeto["b"]}  [N]{dicio_alfabeto["n"]}  [M]{dicio_alfabeto["m"]}   
    
    
    ''')

    return dicio_alfabeto
    
    



