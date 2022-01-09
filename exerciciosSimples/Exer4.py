##Faça um programa para um jogo de dados onde dois jogadores
##podem jogar um dado em duas jogadas seguidas.
##
##A soma das duas
##jogadas deve ser maior que a soma das duas jogadas do oponente.
##O jogador que tiver a soma maior, ganha. Use if e else

import random
import time

print ('Jogo dos dados.')

dado1 = 0
dado2 = 0

soma1 = 0
soma2 = 0
temp = 2

i=1
print("Jogador 1 começa o jogo.")
while(i <= 2):
    dado1 = random.randrange(1,7)
    print('O dado deu o número:', dado1)
    soma1=soma1+dado1
    i=i+1
    time.sleep(temp)

print('\n')

print('A soma das duas jogadas do Jogador 1  é: ', soma1)
time.sleep(temp)


print ('Agora é a vez do jogador 2...')

i=1
while(i <= 2):
    dado2 = random.randrange(1,7)
    print('O dado deu o número:', dado2)
    soma2=soma2+dado2
    i=i+1
    time.sleep(temp)

print('\n')

print('A soma das duas jogadas do Jogador 2 é: ', soma2)

print('\n')
print('Resultado...\n')
time.sleep(temp)

if(soma1 > soma2):
    print('Jogador 1 venceu!!')
elif(soma1 < soma2):
    print('Jogador 2 venceu!!')
else:
    print ('Empate.')
