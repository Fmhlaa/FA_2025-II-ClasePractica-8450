def ejer1():#
    nombre=input("Ingrese su nombreP: ")
    carrera=input("Ingrese su carreraP: ")

    print(f"{nombre}, \ndBienvenido a Fa de {carrera}")

def ejer2():
    print("\"\"Fa\"\"")
   
def ejer3():
    x = int(input("Ingrese el valor de x: "))
    y = int(input("Ingrese el valor de y: "))

    print("Suma: ", (x+y))
    print("Resta: ", (x-y))
    print("Multiplicacion: ",(x*y))
    print("DIvision: ",(x/y))

import math #importando la libreria math(Las operaciones)
def ejer4():
    num = float(input("Ingrese un numero decimal: "))
    print("Raiz 2: ",math.sqrt(num))
    print("Redondeado: ", round(num,0))
    print("al cubo: ", math.pow(num,3))
    print("Raiz 3: " , num ** (1/3))

def ejer5():
    num = input("Ingrese su numero: ")

    entero= int(num)
    deci= float(num)

    print("Resto: ", (entero%2))
    print("division: ", (deci/3))



ejer5()