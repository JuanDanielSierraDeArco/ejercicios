'''''
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama. listo
'''

def anagrama(palabra1, palabra2):

    if palabra1.lower() == palabra2.lower():
        return False
    
    if len(palabra1) != len(palabra2):
        return False

    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    if len(palabra1) == len(palabra2):
        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()

    comparacion1 = {}
    comparacion2 = {}
        
    for a in palabra1:
        comparacion1[a] = comparacion1.get(a, 0) + 1

    for b in palabra2:
        comparacion2[b] = comparacion2.get(b, 0) + 1

    return comparacion1 == comparacion2


def is_anagram(palabra1, palabra2):
    
    if palabra1.lower() == palabra2.lower():
        return False
    
    # Convertir a minúsculas, ordenar los caracteres y comparar
    return sorted(palabra1.lower()) == sorted(palabra2.lower())




palabra1 = input('Ingresa la primera palabra =>')
palabra2 = input('Ingresa la segunda palabra =>')
print()
print('Forma 1',anagrama(palabra1,palabra2))
print('Forma 2',is_anagram(palabra1,palabra2))
print()
print(palabra1)
print(palabra2)