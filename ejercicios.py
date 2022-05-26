# escribir una funcion a la que se le pase una cadena/variable
#<nombre> y muestre por pantalla el saludo 
#¡hola <nombre> !. 

#escriba un programa que pregunte al usuario su edad y
#muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)


#escribir un programa que muestre por pantalla la tabla 
#de multiplicar del 1  al 12. el usuario ingresa el numero de la tabla

# def main():
#     nombre = input ("ingrese nombre:")
#     print( "¡ hola " + nombre + " !")

# if __name__ == '__main__':
#     main()

#desarrollo profe
 
# def saludo (nombre):
#     frase_saludo ="hola "+ nombre + " !"
#     return frase_saludo

# def main():
#     name = saludo ( input("ingrese su nombre:"))
#     print(name)

# if __name__== '__main__':
#     main()

#ejercicio 2

# def main():
#     edad = int(input( " ingrese su edad : "))
#     for numero in range(1, edad + 1 ):
#         print(numero)
# if __name__ == '__main__':
#     main()

#ejercicio 3

def main():
    tabla = int(input("ingrese la tabla que desea :"))
    for contador in range (1 , 13):
        frase = str(tabla) + 'x' + str(contador)+ 'es: ' + str (contador*tabla)
        print(frase)

if __name__ == '__main__':
    main()
