class Conjuntos:

    def __init__(self):
        self.Equipo_1 = {"Jose", "Manuel", "Pedro", "Juan"}
        self.Equipo_2 =["Ernesto", "Rogelio", "Jose", "Juan"]
        self.Comun_employed = {"",}
        self.Ultimo_equipo = {"",}
    
    def Count(self):
        print("El tamaño del equipo 1 es de ",len(self.Equipo_1),"\ny del equipo dos es de ",len(self.Equipo_2))

    def Pertenece(self):
        if (len(self.Equipo_1) > len(self.Equipo_2)):
            for equipo1 in self.Equipo_1:
                for equipo2 in self.Equipo_2:
                    if (equipo1 == equipo2):
                        self.Comun_employed.add(equipo1)
        else:
            for equipo2 in self.Equipo_2:
                for equipo1 in self.Equipo_1:
                    if (equipo1 == equipo2):
                        self.Comun_employed.add(equipo1)
        
        print(self.Comun_employed)


    def add(self, name):
        self.Equipo_1.add(name)
    
    def delet(self, name):
        self.Equipo_1.remove(name)

    def comun(self):
        if (len(self.Equipo_1) > len(self.Equipo_2)):
            for equipo1 in self.Equipo_1:
                for equipo2 in self.Equipo_2:
                    if (equipo1 == equipo2):
                        self.Comun_employed.add(equipo1)
        else:
            for equipo2 in self.Equipo_2:
                for equipo1 in self.Equipo_1:
                    if (equipo1 == equipo2):
                        self.Comun_employed.add(equipo1)
        
        print(self.Comun_employed)
    
    def Crear(self):
        if (len(self.Equipo_1) > len(self.Equipo_2)):
            for equipo1 in self.Equipo_1:
                for equipo2 in self.Equipo_2:
                    if (equipo1 != equipo2):
                        self.Ultimo_equipo.add(equipo1)
        else:
            for equipo2 in self.Equipo_2:
                for equipo1 in self.Equipo_1:
                    if (equipo1 != equipo2):
                        self.Ultimo_equipo.add(equipo1)
        print(self.Ultimo_equipo)
        

C = Conjuntos()
"""C.Count()
C.add("Carlos")
C.Count()
C.delet("Jose")
C.Count()

equipo3 = C.Equipo_1.union(C.Equipo_2)"""
print(C.Crear())

