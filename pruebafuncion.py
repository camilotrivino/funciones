def descuento():
    valor=int(input("Ingrese el precio a pagar: "))
    desc=float(input("Ingrese el descuento: "))
    total=valor-valor*(desc/100)
    print(f"TOTAL A PAGAR: {total}")
    return total
descuento()
