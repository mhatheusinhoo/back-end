import random
n1 = input('Primeiro aluno:seu barriga ')
n2 = input('Segundo aluno: natan ')
n3 = input('Terceiro aluno:chaves ')
n4 = input('Quarto aluno:kiko ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
