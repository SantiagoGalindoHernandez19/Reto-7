
X =int(input("ingrese un número: ")) #Solicitamos ingresar numero
X : int 
factorial = 1 #Definicion variable en 1 
i = 1
while i <= X:
    factorial *= i #Dentro del ciclo multiplicamos valor factorial
    i += 1
print("El factorial de", X, "es", factorial)
