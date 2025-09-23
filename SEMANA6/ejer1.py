num=(input("Ingrese un numero postivo: "))
print()
while num<=0:
    num=int(input("Error, ingrese un numero positivo: "))
i=1 
while i<=12:
    print(f"{i} x {num}={i*num} ")
    i+=1