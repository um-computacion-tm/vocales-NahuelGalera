import unittest

# Función para contar las vocales en una cadena de texto
def contar_vocales(cadena):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for letra in cadena.lower():
        if letra in vocales:
            vocales[letra] += 1

    return vocales

# Pruebas unitarias
class TestContarVocales(unittest.TestCase):
    def test_contar_vocales(self):
        self.assertEqual(contar_vocales("Hola Mundo"),          {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1})
        self.assertEqual(contar_vocales("casa"),                {'a': 2, 'e': 0, 'i': 0, 'o': 0, 'u': 0})
        self.assertEqual(contar_vocales("1234567890"),          {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})
        self.assertEqual(contar_vocales("¡Hola, Mundo!"),       {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1})


# Ingresar palabras
palabra = input("Por favor, ingrese una palabra: ")

# Resultado de vocales
resultado = contar_vocales(palabra)
print(resultado)

unittest.main()