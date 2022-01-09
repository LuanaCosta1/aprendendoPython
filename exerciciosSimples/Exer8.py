##Crie um programa que receba várias idades e que calcule e mostre a média
##das idades digitadas. Finalize digitando a idade igual a zero

idade = 1
totalIdades = 0
qtdPessoas = 0

while(idade != 0):
    idade = int(input('Digite o valor da idade.\nOu digite 0 para finalizar a contagem.\n'))
    totalIdades = totalIdades + idade
    qtdPessoas = qtdPessoas + 1

print('Soma das idades: ', totalIdades)
print('Quantidade de pessoas: ', qtdPessoas)
print('Média das idades: ', totalIdades / qtdPessoas)
print('Fim do programa! ================================')
