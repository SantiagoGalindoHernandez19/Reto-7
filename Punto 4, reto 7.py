#Definicion de variables 
x = 25  #Pais poblacion A 
c = 18.9  #Pais poblacion B
TasaCrecimiento1 = 0.02  # tasa de crecimiento anual del país A (2%)
TasaCrecimiento2 = 0.03  # tasa de crecimiento anual del país B (3%)

año = 2022  # Año inicial

while c <= x:
    año += 1  #Incremento año
    x *= (1 + TasaCrecimiento1)  # Nueva población del país A
    c *= (1 + TasaCrecimiento2)  # Nueva población del país B

print("En el año,", año , "La poblacion del pais A sera superada por la poblacion del pais B")
