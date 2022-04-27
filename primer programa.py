#transformar pesos chilenos a dolares

#el programa debe pedir una cantidad  de pesos y mostrar el resultado en dolares

pesos = input("ingrese la cantidad de pesos chilenos")
pesos = float(pesos)
#int para entero, float datos decimales

valor_dolar = 806
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
#para que salga un texto
print("usted  tiene $"+ dolares +" dolares")
# ++ concanetacion

#tarea programa que transforma de dolares a pesos chilenos