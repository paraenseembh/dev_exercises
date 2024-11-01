'''Crie um programa em Python que simule um sistema de login. 
O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam.
 Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.



Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.
'''

def main():
    usuario = "admin"
    senha = "admin123"
    tentativas = 3

    while tentativas > 0:
        usuario_input = input("Digite o nome de usuário: ")
        senha_input = input("Digite a senha: ")

        if usuario_input == usuario and senha_input == senha:
            print("Bem-vindo!")
            break
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"Usuário ou senha incorretos. Você tem {tentativas} tentativas restantes.")
            else:
                for _ in range(3):
                    print("Acesso bloqueado")