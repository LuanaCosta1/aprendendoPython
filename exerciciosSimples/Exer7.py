##Crie um programa que receba a idade de 6 pessoas e calcule a média das idades. 
##USE FOR

print("Calcule a média de 6 idades!")

idade = 0
soma = 0
media = 0

if( idade <= 6):
    for i in range (1 ,7):
        idades =int(input("Digite a idade: "))
        idade = idades + 1
        soma = idades + soma
        media = soma / 6

print("A soma das idades é igual a: ", soma)     
print("A média das idades é igual a: ", media) 
