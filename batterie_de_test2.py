



from Implementation002 import *
if  __name__ == '__main__':
    import time
    start = time.time()

    Le_Rectangle = Rectangle(6,10)
print("Le périmètre du Rectangle est ",Le_Rectangle.périmètre(),"mètres")
print("La surface du Rectangle est ",Le_Rectangle.surface(),"mètres carré")

Le_Cercle = Cercle(7)
print("Le périmètre du Cercle est",Le_Cercle.périmètre(),"mètres")
print("La surface du Cercle",Le_Cercle.surface(),"mètres carré")

Le_Triangle = Triangle(4,6,6,6)
print("Le périmètre du Triangle est ",Le_Triangle.périmètre(),"mètres")
print("La surface du Triangle est ",Le_Triangle.surface(),"mètres carré")

Le_Carré = Carré(9)
print("Le périmètre du Carré est ",Le_Carré.périmètre(),"mètres")
print("La surface du Carré est ",Le_Carré.surface(),"mètres carré")

Le_TriangleRectangle = TriangleRectangle(5,8)
print("Le périmètre du TriangleRectangle est ",Le_TriangleRectangle.périmètre(),"mètres")
print("La surface du TriangleRectangle est ",Le_TriangleRectangle.surface(),"mètres carré")

