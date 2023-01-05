"""Création d'une classe de base des formes géométriques"""
from abc import ABCMeta, abstractmethod
from math import pi, sqrt

class Geometric_form(metaclass=ABCMeta):
    #La classe Geometric_form est une classe abstraite
    @abstractmethod
    def perimeter():
        pass
        #Méthode abstraite pour le calcul du périmètre
    @abstractmethod
    def surface():
        pass
        #Méthode abstraite pour le calcul de la surface

# Maintenant, nous allons créer des classes qui héritent de Geometric_form

class Rectangle(Geometric_form):
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    def perimeter(self):
        return 2*((self.__longueur)+(self.__largeur))
    def surface(self):
        return self.__longueur*self.__largeur

class Cercle(Geometric_form):
    def __init__(self, rayon):
        self.__rayon = rayon
    def perimeter(self):
        return pi*(self.__rayon)*2
    def surface(self):
        return pi*(self.__rayon)**2
    
class Triangle(Geometric_form):
    def __init__(self, hauteur, coté1, coté2, coté3):  #Le coté1 est la base du triangle
        self.__hauteur = hauteur
        self.__coté1 = coté1
        self.__coté2 = coté2
        self.__coté3 = coté3
    def perimeter(self):
        return self.__coté1 + self.__coté2 + self.__coté3
    def surface(self):
        return (self.__coté1*self.__hauteur)/2

# Nous allons maintenant créé une classe pour les carrées
"""Pour ce faire, nous allons utiliser 
la classe Rectangle car le carré est
un cas particulier du rectangle, ce
n'est rien d'autre qu'un rectangle de 
longueur et largeur égales"""

class Carré(Rectangle):
    def __init__(self, coté):
        Rectangle.__init__(self,coté,coté)

# Créeons maintenant une classe pour les triangles rectangles
"""Nous allons considéré notre triangle rectangle
comme un triangle dont la hauteur est égale à l'un des cotés
elle n'aura pour paramètres que sa hauteur, sa base et
le troisième coté qui est l'hypoténuse"""

class RecTriangle(Triangle):
    def __init__(self, baset, hauteurt):
        Triangle.__init__(self,hauteurt,baset,hauteurt,coté3=sqrt(baset**2+hauteurt**2))


myRectangle = Rectangle(6,9)
print("Le périmètre du rectangle est ",myRectangle.perimeter(),"mètres")
print("La surface du rectangle est ",myRectangle.surface(),"mètres carré")

myCircle = Cercle(6)
print("Le périmètre du cercle est",myCircle.perimeter(),"mètres")
print("La surface du cercle",myCircle.surface(),"mètres carré")

myTriangle = Triangle(5,8,8,8)
print("Le périmètre du triangle est ",myTriangle.perimeter(),"mètres")
print("La surface du triangle est ",myTriangle.surface(),"mètres carré")

mySquare = Carré(11)
print("Le périmètre du carré est ",mySquare.perimeter(),"mètres")
print("La surface du carré est ",mySquare.surface(),"mètres carré")

myRectangleTriangle = RecTriangle(5,7.5)
print("Le périmètre du triangle rectangle est ",myRectangleTriangle.perimeter(),"mètres")
print("La surface du triangle rectangle est ",myRectangleTriangle.surface(),"mètres carré")


B = Rectangle(6,9)
print(B)
C = Cercle(6)
print(C)
D = Triangle(5,8,8,8)
print(D)
E = Carré(11)
print(E)
F = RecTriangle(5,7.5)
print(F)
