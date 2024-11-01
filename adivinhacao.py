'''Você está criando um programa em Python para simular um jogo simples de adivinhação. O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
O jogador terá até 3 tentativas para acertar o número.

Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas tentativas até acertar ou
 atingir o limite de tentativas. Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte e 
 uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.'''

numero_secreto = 7
tentativas = 3
while tentativas > 0:
    tentativa = int(input('Digite um número: '))
    if tentativa == numero_secreto:
        print('Parabéns! Você acertou!')
        break
    elif tentativas > 1:
        print('Que pena! Tente novamente!')
        tentativas -= 1
    else:
        print('Suas tentativas acabaram! O número era', numero_secreto)