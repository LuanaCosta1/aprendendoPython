##Faça um programa em Python que calcula e escreva a
##seguinte soma: soma = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
##USE FOR

k = -1
resul = 0
for x in range (1, 50):
    k = k +2
    z = x
    resul = resul +k/z
    print ('k/z + ...:',round(k/z, 2), '<--> Res. parcial: ',round(resul, 2))
    print('Resposta Final: ',resul)
