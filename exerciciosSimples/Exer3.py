##Escreva um programa que calcule o dobro de um número caso ele seja Par e Positivo.
##Se o númeor cumprir com as duas exigências, mostre o resultado, senão escreva número inadequado.

num = int(input('Digite um valor: '))
dobro = num * 2

if (num % 2 == 0 and num > 0):
    print('O dobro de', num,'é igual a:', dobro)
else:
    print('Número inadequado')
