def resta(a,b):
    return a-b
resta(30,10)
resta(b=30,a=10)
def funcion():
    return "Bienvenido a Python"
frase=funcion()
print(frase)
def restar(a=None, b=None):
    if a==None or b==None:
        print("Error, faltan parametros a la funcion")
        return
    return a-b
restar()
