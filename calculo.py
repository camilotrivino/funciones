def iva():
    precio=int(input("Ingrese el valor del producto:\n$"))
    total=precio+precio*0.19
    print(f"el precio del producto con iva es: ${total}")
    return total
def descuento():
    valor=int(input("Ingrese el precio a pagar: "))
    desc=float(input("Ingrese el descuento: "))
    total=valor-valor*(desc/100)
    print(f"TOTAL A PAGAR: ${total}")
    return total
def imc():
    peso=float(input("Ingrese su peso. \nkg: "))
    esta=float(input("Ingrese su estatura. \nmtr: "))
    resultado=peso/(esta**2)
    if resultado>18.5:
        print(f"Usted esta BAJO PESO kg.{resultado}")
    elif resultado>=18.5 or resultado<=24.9:
        print(f"Usted esta en peso ADECUADO kg.{resultado}")
    elif resultado>=25.0 or resultado<=29.9:
        print(f"Usted esta en peso SOBREPESO kg.{resultado}")
    elif resultado>=30.0 or resultado<=34.9:
        print(f"Usted esta en peso OBESIDAD GRADO 1 kg.{resultado}")
    elif resultado>=35.0 or resultado<=39.9:
        print(f"Usted esta en peso OBESIDAD GRADO 2 kg.{resultado}")
    elif resultado>40:
        print(f"Usted esta en peso OBESIDAD GRADO 3 kg.{resultado}")
    return resultado
