'''[LPIA-A06]  Crie um programa em Python que simule um sistema de login. O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.



Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.
'''
# Definindo as credenciais corretas
usuario_correto = "admin"
senha_correta = "1234"

# Número de tentativas permitidas
tentativas = 3

# Loop para permitir ao usuário tentar fazer login
while tentativas > 0:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Credenciais incorretas. Você tem mais {tentativas} tentativa(s).")
        else:
            print("Acesso bloqueado.")
            for _ in range(3):
                print("Acesso bloqueado.")