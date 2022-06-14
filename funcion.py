# sin argumentos(entrada) y sin retorno(salida)
def saludar():
    saludo="bienvenidos a funciones"
    print(saludo)

#sin argumentos(entrada) y con retorno(salida)
def suma():
    valor1=int(input("ingrese valor 1: "))
    valor2=int(input("ingrese valor 2: "))
    total=valor1+valor2
    return total
#con argumentos(entrada) y sin retorno(salida)
def resta(num1,num2):
    total=num1-num2
    print(total)
    
def descuento():
    valor=int(input("Ingrese el precio a pagar: "))
    desc=float(input("Ingrese el descuento: "))
    total=valor-valor*(desc/100)
    print(f"TOTAL A PAGAR: {total}")
    return total
