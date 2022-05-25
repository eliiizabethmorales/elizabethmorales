#palindromo

#escribir un programa que identifique
#si una palabra es palindromo o no
#luz azul
#ana
#anita lava la tina
#yo hago yoga hoy

# nombre= input("ingrese la palabra para ver si es polidromo:    ")

# nombre1 = nombre[::-1]

# if nombre == nombre1:
#     print("la palabra si es palindromo")

# else:
#     print("ingrese una palabra palindroma")


#desarrollo del profe

def palindromo(palabra): 
    palabra = palabra.replace('','')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

#funcion principal main/run

def main():
    palabra=input("ingrese una frase:  ")
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print("es palindromo")
    else:
        print("no es palindromo")

#punto de entrada
# buena practica

if __name__=="__main__":
    main()



