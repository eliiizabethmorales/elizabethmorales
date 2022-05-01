# Tarea 1
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete 
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y 
# muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado

#solucion 1:

# payasos = int(input("hola, cuantos payasos enviara?:"))
# muneca = int(input("cuantas muñecas enviara?:"))
# if payasos and muneca >= 0 :
#     pesopayaso = payasos * 112
#     pesomuneca = muneca * 75
#     valorenvio = pesopayaso + pesomuneca
#     valorenvio = str(valorenvio)
#     print("el valor del envio sera $" + valorenvio +" ")
# else: 
#     print("ingrese un valor entero o un numero positivo")
 


 # Tarea 2
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
# calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase 
# "Tu índice de masa corporal es <imc>" donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.

#solucion 2:
peso = input("hola, ingrese su peso en kg:")
peso = float (peso)
estatura = input("ahora ingrese su estatura en metros:")
estatura = float (estatura)

if peso and estatura >= 1:
    imc = (peso /( estatura * estatura))
    imc = round(imc , 2)
    imc = str(imc)
    print("tu indice de masa corporal es " + imc + " .")
else:
    print("ingrese valores correctos")


