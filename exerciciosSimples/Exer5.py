##) Faça um programa que represente três alunos, de uma turma com 10
##alunos, pelos números 1, 2 e 3. Esses três alunos são candidatos a
##uma eleição de líder da turma. Simule os 10 votos da turma, para um
##desses 3 alunos e apresente o ganhador da eleição

import random
import time
print ('Programa para eleição do representante da classe.')


aluno1 = 0
aluno2 = 0
aluno3 = 0

i = 1

while(i <= 10):
    n = int(random.randrange(1,4))
    print('O aluno', i, 'votou no candidato', n)
    time.sleep(1)
    if(n == 1):
        aluno1 = aluno1 + 1
    elif(n == 2):
        aluno2 = aluno2 + 1
    else:
        aluno3 = aluno3 + 1
    i = i+1

if(aluno1>aluno2 and aluno1>aluno3):
    print('O aluno 1 ganhou a eleição da turma.')
elif(aluno2>aluno1 and aluno2>aluno3):
    print('O aluno 2 ganhou a eleição da turma.')
elif(aluno3>aluno1 and aluno3>aluno2):
    print('O aluno 3 ganhou a eleição da turma.')
else:
    print('Houve algum empate, teremos 2° turno.')
    
time.sleep(1)
print('Quantidade de votos por candidato:')
print('Aluno 1: ', aluno1, 'Aluno 2: ', aluno2, 'Aluno 3: ', aluno3)
