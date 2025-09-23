sumap=sumai=0
while True :
    num=int(input("Ingrese un numero positivo (0 salir): "))
    if num<0:
        print("Numero invalido. Ingrese nuevamente")
        continue
    if num == 0:
        break
    if num%2==0:
        sumap+=num
    else: 
        sumai += num
print("\nSuma pares: ",sumap)
print("Suma impares: ",sumai)