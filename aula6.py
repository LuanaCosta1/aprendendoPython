
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
conjunto_interseccao = conjunto.intersection(conjunto2)
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B? {}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é superconjutno de A? {}'.format(conjunto_superset))


lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)

print('União: {conjunto_uniao}'
      '\nIntersecção: {conjunto_interseccao} '
      '\nDiferença entre 1 e 2: {conjunto_diferenca} '
      '\nDiferença entre 2 e 1: {conjunto_diferenca2}'
      '\nDiferença simétrica: {conjunto_diff_simetrica}'
      .format(conjunto_uniao=conjunto_uniao,
              conjunto_interseccao=conjunto_interseccao,
              conjunto_diferenca=conjunto_diferenca,
              conjunto_diferenca2=conjunto_diferenca2,
              conjunto_diff_simetrica=conjunto_diff_simetrica))


# conjunto = {1,2,3,4,4,6,3}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto)
# print(type(conjunto))