#diccionarios

diccionario = {}

diccionario_capitales = {
    'chile': 'santiago',
    'españa': 'madrid',
    'argentina': 'mendoza'
}

print (diccionario_capitales['españa'].upper())

for pais, capital in diccionario_capitales:
    print (capital)