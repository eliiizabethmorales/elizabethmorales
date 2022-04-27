#tipos de datos

#tipos de datos clasicos
# 1.- numeros enteros
# 2.- numeros flotantes (decimales) deben ser escrito con punto (.)
# 3.- cadenas de textos (string)
# 4.- booleanos

# cadenas de texto (strin)
#nombre = "juan"
#print(nombre)

#nombre2 = 'maria jose'
#print(nombre2)

#nombre3= """ este es mi 
#texto en 
#varias lineas
# """
# print(nombre3)

# #concatenasion 
# #une 2 o mas cadenas de variables 

# nombre4 = nombre + nombre2
# print(nombre4)

# print(nombre * 3)

# print(nombre + ", " + nombre2)

#booleanos
#tiene dos estados puede ser verdadero(true) o falso


# es_estudiante = True
# print(es_estudiante)

# trabaja = False
# print(trabaja)




#convertir tipo de datos

#convertir texto a numeros
numero1 = input("ingrese un numero:")
print(numero1)
numero2 = input("ingrese otro numero")
print(numero2)

print( numero1 + numero2 )
#esto no suma, lo interpreta como texto como contenacion

numero1 = int(numero1)
numero2 = int(numero2)
print(numero1 + numero2)

numero_decimal = 4.5
print(int(numero_decimal))

print(str(numero_decimal))
