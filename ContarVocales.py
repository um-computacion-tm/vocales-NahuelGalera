
#Funcion contar cada vocal
def contar_vocales(palabra):
    contador_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}
    
    for letra in palabra:
        if letra in contador_vocales:
            contador_vocales[letra] += 1

    return contador_vocales

#Funcion contar mayus y minus (vocales)
def contar_total_vocales(palabra):
    contador_minus = 0
    contador_mayus = 0

    vocales_minusculas = ['a', 'e', 'i', 'o', 'u']
    vocales_mayusculas = ['A', 'E', 'I', 'O', 'U']
    
    for letra in palabra:
        if letra in vocales_minusculas:
            contador_minus += 1
        elif letra in vocales_mayusculas:
            contador_mayus += 1

    return contador_minus, contador_mayus

#Ingresar palabra
palabra = input("Por favor, ingrese una palabra: ")

#Funcion cada vocal
resultado = contar_vocales(palabra)
print("Cantidad de cada vocal en la palabra: ", resultado)

#Mostrar cantidad de vocales en mayusculas y minusculas
for vocal, cantidad in resultado.items():
    print("{0}: {1}".format(vocal, cantidad))

#Funcion por separado total de mayus y minus
vocales_minusculas, vocales_mayusculas = contar_total_vocales(palabra)
print("Cantidad de vocales en minusculas: ", vocales_minusculas)
print("Cantidad de vocales en mayusculas: ", vocales_mayusculas)
