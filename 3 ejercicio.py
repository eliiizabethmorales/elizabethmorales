#ejercicio 3
#escribir en un programa que lea un entero positivo n
#introducido por el usuario y despues muestre por pantalla
#la suma de todos los enteros desde 1 hasta n
#la sumas de los n primeros positivos puede ser calculada
# de la siguiente forma  
#suma= (n(n+1))/2

#solucion mia
# numero = int(input("ingrese un numero entero positivo"))
# resultado = ((numero * (numero + 1 )) / 2 )
# resultado = str(resultado)
# print(""+ resultado +"")

# #solucion profe
# n = int(input("ingrse un numero positivo:"))
# suma = (n * (n + 1 )) / 2 
# suma = str(suma)
# n= str(n)

#esto se hace para que no alla problema y transformar a texto con str

# print("la suma de los primeros numeros enteros desde 1 hasta "+ n +" es " + suma +"")

#solucion con positivo y negativo

n = int(input("ingrese un numero positivo:"))

if n>= 1:
    suma = ( n + (n + 1 ))/ 2 
    suma = str(n)
    print("la suma de los primeros numeros enteros desde 1 hasta " + n + " es " + suma +"")
else:
    print("el numero no es mayor o igual a 1")