
x=int(input("Ingresa un numero del 1 al 100: "))
print("Después de cada intento, dime si el número que piensas es mayor (ingresa 'mayor'), menor  o igual al que yo te propongo.")

min_num = 1
max_num = 100
adivinado = False

while not adivinado:
    
    num_adivinado = (min_num + max_num) // 2 #Promedio minimo y maximo posible
    respuesta = input(f"¿Es {num_adivinado} tu número? (m/n/s): ")

    if respuesta == 'igual':
        print("¡Adivinamos tu numero!")
        adivinado = True
    elif respuesta == 'mmayor':
      
        
        min_num = num_adivinado + 1
    elif respuesta == 'menor':
        
        max_num = num_adivinado - 1
    else:
        print("Respuesta no válida. Ingresa 'm' si es mayor, 'n' si es menor o 's' si es igual.")