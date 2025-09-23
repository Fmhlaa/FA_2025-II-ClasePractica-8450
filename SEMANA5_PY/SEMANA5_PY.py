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

def ejer3():
    n=int(input("Ingrese un número: "))
    print()
    for i in range (1,n+1):
        print(i)
        if i%2 == 0:
            suma+= i
    print("\nSuma de pares: ",suma)

def ejer4():
    cant= int(input("Ingrese la cantidad de numeros: "))
    ceros = pares = impares = 0
    print()
    for i in range(1, cant+1):
        num= int(input(f"Ingrese el numero {i}: "))
        if num == 0:
            ceros+=1
        elif num % 2 ==0:
            pares+=1
        else: 
            impares+=1
    print("\n# de ceros: ",ceros)
    print("# de pares: ",pares)
    print("# de impares: ",impares)
 
            



















ejer4()







