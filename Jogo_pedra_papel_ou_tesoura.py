import random
print("Jogo Pedra, papel ou tesoura")
print("""para pedra clique em p
      para papel clique em o
      para tesoura clique em k
      para rever as regras clique em n""")
dicionario = {
    "p": {"p":0, "k":-1, "o":1},
    "o": {"p":-1, "k":1, "o":0},          
    "k": {"p":1, "k":0, "o":-1}        
              }
def regras(): 
    print("""para pedra clique em p
      para papel clique em o
      para tesoura clique em k
      para rever as regras clique em n""")
pontuação_jogador = 0
pontuação_computador = 0
while True: 
    resposta = input ("Escolha a sua jogada: ")
    lista_de_respostas = ["p", "o", "k"]
    if resposta == "n":
        regras()
    if resposta in lista_de_respostas:
        tratratratretretre = random.choice(lista_de_respostas)
        ganhou = dicionario [resposta] [tratratratretretre]
        if ganhou == 0:
            print("Empate!")
        if ganhou == 1:
            print("Ganhaste!")
            pontuação_jogador +=1
        if ganhou == -1:
            print("Eu ganhei! ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha ha")
            pontuação_computador +=1
    else:
        print("Artista, escreve uma coisa que se perceba!")
    print(f"pontuação do computador: {pontuação_computador}, pontuação do artista: {pontuação_jogador}")