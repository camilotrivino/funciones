import calculo
menu=True
print("ELIJA UNA OPCION")
while menu:
    print("1.- Calcular iva de un producto")
    print("2.- Calcular el descuento de un producto")
    print("3.- Calcular el imc")
    print("4.- Salir")
    opc=int(input("Ingrese una opcion: "))
    if opc==1:
        iva=calculo.iva()
        print(iva)
    elif opc==2:
        descuento=calculo.descuento()
        print()
    elif opc==3:
        imc=calculo.imc()
        print(imc)
    elif opc==4:
        menu=False
        print("HAS SALIDO")