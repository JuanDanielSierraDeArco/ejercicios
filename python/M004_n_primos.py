'''
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 '''

def primo():
    
    for i in range(1,101):
        contar = 0
        for a in range(1,i + 1):
            if i % a == 0:
                contar +=1
        
        if contar == 2:
            print(i)

primo()