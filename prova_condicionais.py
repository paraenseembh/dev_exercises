## Crie um programa em Python para verificar se um número é positivo, negativo ou zero. O programa deve solicitar ao usuário que insira um número e, em seguida, imprimir uma mensagem indicando a natureza do número. 
## Se o número for maior que zero, exiba a mensagem "O número é positivo." Se for menor que zero, exiba "O número é negativo." Caso seja zero, a mensagem deve ser "O número é zero."
## Utilize estruturas condicionais e formatação com F-string para criar o programa de forma clara.

numero_escolhido = int(input('Digite um numero para verificar se ele eh positivo, negativo, ou igual a zero.'))

if numero_escolhido >  0 : 
    print(f'O numero {numero_escolhido} eh positivo.')
elif numero_escolhido < 0 :
    print(f'O numero {numero_escolhido} eh negativo.')
else:
    print(f'O numero eh igual a zero.') 
