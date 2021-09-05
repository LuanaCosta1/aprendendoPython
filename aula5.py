# [] = lista
# () = tupla
# {} = conjunto

lista = [1, 30, 5, 77, 12, ]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()
# print(lista_animal)

lista_animal[0] = 'macaco'
print(lista_animal)

tupla = (1, 10, 12, 14)
print(tupla)
print(len(tupla))
print(len(lista_animal))
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

# nova_lista = lista_animal * 3
# print(nova_lista)
# # print(lista_animal[1])
#
# soma = 0
# for x in lista_animal:
#     print(x)
#     soma += 1
# print(soma)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
#
# print(max(lista_animal))
# print(min(lista_animal))
#
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista')
#
#
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista, será incluido...')
#     lista_animal.append('lobo')
#     print(lista_animal)
#
# # lista_animal.pop(1)
# # print(lista_animal)
#
# lista_animal.remove('elefante')
# print(lista_animal)