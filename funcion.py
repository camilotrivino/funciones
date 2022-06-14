# sin argumentos(entrada) y sin retorno(salida)
def saludar():
    return "Bienvenido a Python"

#sin argumentos(entrada) y con retorno(salida)
def suma():
    valor1=int(input("ingrese valor 1: "))
    valor2=int(input("ingrese valor 2: "))
    total=valor1+valor2
    return total
#con argumentos(entrada) y sin retorno(salida)
def resta(a,b):
    return a-b
    
#con argumentos(entrada) y con retorno(salida)
def multiplicar(valor1,valor2):
    total=valor1*valor2
    print(total)
    return total
    
def descuento():
    valor=int(input("Ingrese el precio a pagar: "))
    desc=float(input("Ingrese el descuento: "))
    total=valor-valor*(desc/100)
    print(f"TOTAL A PAGAR: {total}")
    return total

