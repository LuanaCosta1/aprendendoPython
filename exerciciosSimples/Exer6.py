##6) Escreva um programa que sorteie uma velocidade para um carro
##de 10 a 120 km/h. Caso a velocidade ultrapasse 80km/h,
##exiba uma mensagem dizendo que o usuário foi multado. Nesse caso,
##Exiba o valor da multa, cobrando R$ 5 por km/h acima de 80 km/h

import random

print ('======Programa para fazer o calculo de multas======')

vel = int(random.randrange(10, 121))
print ('A velocidade registrada é de: ', vel)

if(vel > 80):
    print('Você recebeu uma multa por ultrapassar a velocidade limite de 80 km/h.')
    print('Você está a', (vel - 80),'km/h da velocidade permitida')
    mul = (vel - 80)*5
    print('O valor da multa é de', mul,'R$')
else:
    print('Sem multa, continue assim :)')

print('FIM =================================================')
    
