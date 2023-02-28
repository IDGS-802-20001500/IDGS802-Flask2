class ColoresResistencia():

    def __init__(self, c1, c2, c3, tol):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.tol = tol

    def banda1(self):
        if self.c1 == 0:
            color = "Negro"
        elif self.c1 == 10:
            color = "Cafe"
        elif self.c1 == 20:
            color = "Rojo"
        elif self.c1 == 30:
            color = "Naranja"
        elif self.c1 == 40:
            color = "Amarillo"
        elif self.c1 == 50:
            color = "Verde"
        elif self.c1 == 60:
            color = "Azul"
        elif self.c1 == 70:
            color = "Violeta"
        elif self.c1 == 80:
            color = "Gris"
        elif self.c1 == 90:
            color = "Blanco"
        
        return color
    
    def banda2(self):
        color = ""

        if self.c2 == 0:
            color = "Negro"
        elif self.c2 == 1:
            color = "Cafe"
        elif self.c2 == 2:
            color = "Rojo"
        elif self.c2 == 3:
            color = "Naranja"
        elif self.c2 == 4:
            color = "Amarillo"
        elif self.c2 == 5:
            color = "Verde"
        elif self.c2 == 6:
            color = "Azul"
        elif self.c2 == 7:
            color = "Violeta"
        elif self.c2 == 8:
            color = "Gris"
        elif self.c2 == 9:
            color = "Blanco"
        
        return color
    
    def banda3(self):
        color = ""

        if self.c3 == 1:
            color = "Negro"
        elif self.c3 == 10:
            color = "Cafe"
        elif self.c3 == 100:
            color = "Rojo"
        elif self.c3 == 1000:
            color = "Naranja"
        elif self.c3 == 10000:
            color = "Amarillo"
        elif self.c3 == 100000:
            color = "Verde"
        elif self.c3 == 1000000:
            color = "Azul"
        elif self.c3 == 10000000:
            color = "Violeta"
        elif self.c3 == 100000000:
            color = "Gris"
        elif self.c3 == 1000000000:
            color = "Blanco"
        
        return color
    
    def tolerancia(self):
        color = ""

        if self.tol == 0.02:
            color = "Rojo"
        elif self.tol == 0.05:
            color = "Oro"
        elif self.tol == 0.1:
            color = "Plata"
        
        return color