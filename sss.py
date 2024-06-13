def factorial(num):
    acumulador = 1 
    if num < 0:
        print("tiene q ser un numero entero poditivo ")
    elif num  == 0:
        print("el resultado es : 1 ")
    else:
        for i in range(1, num+1):
            acumulador = acumulador*i 
    return acumulador

num = int(input("ingrese uun numero entero positivo para calcular el factorial: "))
print("el resultado es: ", factorial(num))
