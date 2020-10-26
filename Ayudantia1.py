#area del triangulo o la de un circulo
#librerias: Math, numpy
import numpy

def areaCirculo():
    pi = numpy.pi
    radio = float(input("Ingrese el radio del circulo:"))
    ac = 2* pi * (radio)**2
    print("El area del circulo es " +  str(ac))
    return ac

def areaTriangulo():
    base = float(input('Ingrese la base del triangulo:'))
    altura = float(input('Ingrese la altura del triangulo:'))
    at = (base*altura)/2 
    print("El area del triangulo es " + str(at))

def perimetroCirculo():
    pi = numpy.pi
    radio = float(input("Ingrese el radio del circulo:"))
    print("El perimetro del circulo es ",2*pi*radio)


while True:
    respuesta = input('A que figura desea calcular el area, T o C, ingresa 0 si deseas finalizar:')
    if respuesta == 'T':
        #calcular el area del triangulo
        areaTriangulo()
    elif respuesta == 'C':
        #calcular el area de un circulo
        areaCirculo()
        perimetroCirculo()
    elif respuesta == '0':
        break