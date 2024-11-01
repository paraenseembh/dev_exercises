'''[LPIA-A05]Desenvolva um programa em Python para calcular a média de notas de alunos em uma disciplina. O programa deve solicitar ao usuário o número de alunos e, em seguida, para cada aluno, pedir o nome e três notas. Utilize um loop 'for' para iterar sobre os alunos e suas notas.

Além disso, implemente uma estrutura condicional para verificar se cada aluno foi aprovado ou reprovado, considerando que a média mínima para aprovação é 7.0. Exiba o nome do aluno, suas notas, média e a indicação de aprovação ou reprovação.

Ao final, exiba a média geral da turma.'''

def main():
    num_alunos = int(input("Digite o número de alunos: "))
    alunos = []

    for _ in range(num_alunos):
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Digite a nota {i} do aluno {nome}: "))
            notas.append(nota)
        media = sum(notas) / len(notas)
        status = "Aprovado" if media >= 7.0 else "Reprovado"
        alunos.append((nome, notas, media, status))

    print("\nResultados:")
    for aluno in alunos:
        nome, notas, media, status = aluno
        print(f"Aluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
        print()

    media_geral = sum(aluno[2] for aluno in alunos) / num_alunos
    print(f"Média geral da turma: {media_geral:.2f}")

if __name__ == "__main__":
    main()