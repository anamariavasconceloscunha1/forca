#Este comando de import serve para importar uma lista de estilos para seu progama.
import random
#Aqui embaixo temos as palavras nas quais vão fazer parte do progama.
palavras = [ ]
# Letras erradas e certas estão em branco porque na hora do progama ele vai acrescentar o que a pessoa escreveu.
letrasErradas = ''
letrasCertas = ''
#Ele mostra as imagens que vão ser impressas na tela na hora do progama.
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def receberpalavras():
    global palavras
    while True:
        p=input('Digite as palavras desejadas:') 
        palavras.append(p)
        if p =="":
            break
#O def serve para criar uma função.
def principal():
    """
    Função Princial do programa
    """
    print('F O R C A')
    receberpalavras()
#O print serve para que apareça na tela o que você deseja,geralmente o resultado final.No caso para dizer o nome do jogo.
    palavraSecreta = sortearPalavra()
    #Este comando sortea uma das palavras,para ser a palavra na qual a pessoa tem que adivinhar.
    palpite = ''
    #O palpite te da a chance de você falar uma letra.
    desenhaJogo(palavraSecreta,palpite)
#While True é um looping feito para que você diga uma letra e ele te fala se está certo ou errado.
    while True:
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo():
            #O if significa 'Se'.
            print('Voce Perdeu!!!')
            #Se você errou o palpite ele dirá 'Você perdeu'.
            break
        #Com o break você paralisa o progama.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            #Se você acertar o palpite ele dirá que você 'Você ganhou'.
            break            
        
def perdeuJogo():
    #Aqui com este def você criou uma função.
    global FORCAIMG
    #O global é uma variavel na qual pode chamar outra variavel de qualquer lugar do progama.
    if len(letrasErradas) == len(FORCAIMG):
        #O len é para falar quantos itens tem na lista.
        return True
    #O return True ele retorna para quem lhe chamou,em verdade. 
    else:
        return False
    #O return False retorna para quem lhe chamou,em falso.
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True
    for letra in palavraSecreta:
        #Se a letra este na palavra secreta você acertou.
        #O for é para falar que um item está dentro da lista.
        if letra not in letrasCertas:
            ganhou = False
            #Se a letra não tiver na palvra você errou.
    return ganhou        
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    #Você poderá falar uma letra.
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
        receberPalpite()
        #Aqui o progama te avisa de que só pode falar uma palvra por vez.
    elif palpite in letrasCertas or palpite in letrasErradas:
        print('Voce ja disse esta letra.')
        receberPalpite()
        #Aqui o comando te avisa se você está falando uma letra,na qual você ja falou.
        #O elif é  para o comando de 'Se não se'.
    elif not "A" <= palpite <= "Z":
        print('Por favor escolha apenas letras')
        receberPalpite()
        #Neste caso é se você escrever um número ou outra coisa que não seja uma letra.
    else:
        #O else é um comando de 'Se não'.
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite):
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)])
    
     
    vazio = len(palavraSecreta)*'-'
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas )
    print('Erros: ',letrasErradas)
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper()

    
principal()
