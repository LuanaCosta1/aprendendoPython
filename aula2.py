a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
# a = 10
# b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {soma}. \n'
      'Subtração: {subtracao}. \n'
      'Multiplicação: {multiplicacao}. \n'
      'Divisão: {divisao}. \n'
      'Resto: {resto}'
      .format(soma=soma,
              subtracao=subtracao,
              multiplicacao=multiplicacao,
              divisao=divisao,
              resto=resto))
print(resultado)
# print('soma: ' + str(soma))
# print('soma: {}' .format(soma))
# print('subtracao: ' + str(subtracao))
# print('multiplicacao: ' + str(multiplicacao))
# print('divisao: ' + str(int(divisao)))
# print('resto: ' + str(resto))
# x = '1'
# soma2 = int(x) + 1
# print(soma2)