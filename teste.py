bandas_metal = ['Iron Maiden', 'Angra', 'Slayer', 'Megadeth', 'Krisiun']
nova_banda = 'Caetano Veloso'
if nova_banda not in bandas_metal:
  raise InputError('{} não é metal!'.format(nova_banda))