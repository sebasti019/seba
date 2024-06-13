def factorial(num):
    if num == 1:
        return num 
    else:
        return num*factorial(num-1)
    
num = int(input("ingrese uun numero entero positivo para calcular el factorial: "))
print(factorial(num))