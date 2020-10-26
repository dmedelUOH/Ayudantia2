import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def cuadrante(self):
        x = self.x
        y = self.y
        #primer cuadrante 
        if (x > 0 and y > 0):
            print("{} pertenece al primer cuadrante".format(self))
        #segundo cuadrante
        elif (x<0 and y > 0):
            print("{} pertenece al segundo cuadrante".format(self))
        #tercer cuadrante
        elif (x<0 and y < 0):
            print("{} pertenece al tercer cuadrante".format(self))
        #cuarto cuadantre
        elif (x>0 and y < 0):
            print("{} pertenece al cuarto cuadrante".format(self))
        #se situa en el eje x
        elif ( x == 0 and y !=0):
            print("{} se situa en el eje X".format(self))
        #se situa en el eje y
        elif ( x != 0 and y ==0):
            print("{} se situa en el eje Y".format(self))
        #esta en el origen
        else:
            print("{} se encuentra en el origen".format(self))

    def vector(self, p):
        nuevo_x = p.x - self.x
        nuevo_y = p.y - self.y
        print("El vector entre {} y {} es ({},{})".format(self, p, nuevo_x, nuevo_y))

    def distancia(self, p):

        #funcion cubica
        d = math.sqrt((p.x - self.x)**3+(p.y - self.y)**3) #float
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))

class Rectangulo:
    #Rectangulo -> 2 puntos, calculo altiro los valores de  su base, su altura y su area.
    def __init__(self, pInicial= Punto(), pFinal = Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal
        
        #Hacer calculos.
        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    #Metodos get!  
    #Metodos que sobreescriben: SET .si queremos sobreescribir los valores, adentro del metodo.
    def base(self):
        print("La base del rectángulo es {}".format( self.vBase ))

    def altura(self):
        print("La altura del rectángulo es {}".format( self.vAltura ))

    def area(self):
        print("El área del rectángulo es {}".format( self.vArea ))

A = Punto(2,3)       
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

#AB
A.vector(B)
#BA
B.vector(A)

#distancias
A.distancia(B)
B.distancia(A)
#Distancia de cada punto al origen
print("---------------------------------------")
print("Distancia de cada punto al origen")
A.distancia(D)
B.distancia(D)
C.distancia(D)
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")
print("---------------------------------------")

R = Rectangulo(A,B)

R.base()
R.altura()
R.area()