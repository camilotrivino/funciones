def iva(precio):
    iva=precio*0.19
    return iva
def descuento(precio, descuento):
    total=precio-precio*(descuento/100)
    return total
def imc(peso, altura):
    imc=peso/altura**2
    return imc
def nivel_imc(imc):
    if imc>18.5:
        estado="Bajo peso"
    elif imc>18.5 and imc<25:
        estado="adecuado"
    elif imc>25 and imc<30:
        estado="sobre peso"
    elif imc>30 and imc<35:
        estado="Obesidad grado 1"
    elif imc>35 and imc<40:
        estado="obesidad grado 2"
    else:
        estado="Obesidad grado 3"
    return estado   
        
