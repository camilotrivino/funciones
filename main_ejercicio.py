import calculo
menu=True
print("ELIJA UNA OPCION")
while menu:
    print("1.- Calcular iva de un producto")
    print("2.- Calcular el descuento de un producto")
    print("3.- Calcular el imc")
    print("4.- Salir")
    try:
        opc=int(input("Ingrese una opcion: "))
        if opc==1:
           precio=int(input("Ingrese el precio del producto: \n$"))
           iva=calculo.iva(precio)
           print(f"el iva es: ${iva} (precio: ${precio}") 
        elif opc==2:
            precio=int(input("Ingrese precio: \n$"))
            descuento=int(input("Ingrese el porcentaje de descuento"))
            total=calculo.descuento(precio,descuento)
            print(f"El valor total del producto es: ${total} (descuento: {descuento})")
        elif opc==3:
            peso=int(input("Ingrese su peso: "))
            altura=int(input("Ingrese su altura en metros: "))
            imc=calculo.imc(peso,altura)
            resultado=calculo.nivel_imc(imc)
            print()
        elif opc==4:
            menu=False
            print("HAS SALIDO")
    except:
        print("ERROR ELIGA UNA OPCION DE 1 A 4.")
        