def saludar():
    print("buenos dias")

saludar()

def saludar_persona(persona):
    print ("buenos dias", persona)
    print (f"buenos dias {persona}")
    print ("buenos dias " + persona)

saludar_persona("tlacoyo")


def cubico(num):
    return num * num * num
valor = cubico(5)

print(cubico(5))
print(valor)

def sumar(a, b):
    return a + b
print(sumar(2, 3))

def sumar(a: int, b: int)->int:
    return a + b
print(sumar(2, 3))

def saludar_persona(persona="mundo"):
    print ("buenos dias", persona)

saludar_persona("tlacoyo")
   

def multiplicar(a, b):
    return a * b

print(multiplicar(2, 3))

def multiplicar(a: int, b: int)->int:
    return a * b
print(multiplicar(2, 3))

multiplicar = lambda a,b: a*b 
print(multiplicar(2, 3))


#calcular el volumen de un cilindro
def volumen_cilindro(radio, altura):
    volumen = 3.1416 * radio**2 * altura
    return volumen
print(volumen_cilindro(2, 3))


volumen_cilindro = lambda radio, altura: 3.1416 * radio**2 * altura
print(volumen_cilindro(2, 3))


def volumen_cilindro(radio:float, altura:float)-> float:
    return(3.1416 * radio**2 * altura)
print(volumen_cilindro(2, 3))


