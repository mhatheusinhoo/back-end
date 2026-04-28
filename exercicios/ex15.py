import random
n1 = input('Primeiro aluno:jose ')
n2 = input('Segundo aluno: enzo')
n3 = input('Terceiro aluno:josue ')
n4 = input('Quarto aluno:whz_psico ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')
