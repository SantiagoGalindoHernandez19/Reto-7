

def es_primo(numero): # Funcion numero primero 
    if numero < 2: 
        return False    # verificamos si el número es divisible por cualquier entero entre 2 y la raíz cuadrada
    for i in range(2, int(numero ** 0.5) + 1): 
        if numero % i == 0:
            return False
    return True


def mostrar_primos(inicio, fin): # Funcion para mostrar Num en un rando dado
    print(f"Los números primos entre {inicio} y {fin} son:")
    for numero in range(inicio, fin + 1):
        if es_primo(numero):
            print(numero)

# Mostrar los números primos del 1 al 100
mostrar_primos(1, 100)  


