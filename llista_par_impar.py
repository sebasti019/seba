def validar_lista_numeros(num):
    while True:
        try:
            i = [int(x) for x in num.split()]
            print(i)
            return i
        except ValueError:
            print("error a colocado un valor que no coincide con lo pedido ")

def num_par_e_impar(num):
    num_par = []
    num_impar = []
    for x in num:
        if x % 2 == 0 :
            num_par.append(x)
        else:
            num_impar.append(x)
    print(f"cantidad de numeros impares:{num_impar}")
    print(f"cantidad de numeros par:{num_par}")

num = input("ingrese una lista de numeros separados por espacios: ")
lista_numeros = validar_lista_numeros(num)
num_par_e_impar(lista_numeros)