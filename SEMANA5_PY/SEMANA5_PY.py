def ejer1():
    edad=int(input("Ingrese su edad: "))
    
    if edad >=18:
        print("PUEDE VOTAR: ")
     
        if edad >=25:
            print("Candidato para un cargo politico")
        else:
            print("No es candidato para un cargo politico")
    else:
        print("NO PUEDE VOTAR")
        print("NO PUEDE EJERCER UN CARGO POLITICO")

def ejer2():
    lado1 = int(input("Ingresar lado1: "))
    lado2 = int(input("Ingresar lado2: "))
    lado3 = int(input("Ingresar lado3: "))

    if(lado1 == lado2 == lado3):
        print("EQUILATERO")
    elif lado1 == lado2 or lado1 == lado3:
        print("ISOCELES")
    else:
        print("ESCALENO")


ejer2()







