class Auto:

    anzahl_reifen = 4                           # Klassenvariable

    def __init__(self, marke, farbe, sitze, kilometerstand):
        #print("Init methode")
        self.marke = marke                      # Instanzvariable
        self.farbe = farbe                      # Instanzvariable
        self.sitze = sitze                      # Instanzvariable
        self.kilometerstand = kilometerstand    # Instanzvariable
    
    def __str__(self):
        return f"Der {self.marke} ist {self.farbe} und hat {self.sitze} Sitze. Der Kilometerstand ist {self.kilometerstand}"

    def kilometerstand_ausgeben(self):
        print(f"Kilometerstand vom {self.marke} ist {self.kilometerstand}")

    def fahren(self, kilometer):
        self.kilometerstand += kilometer
        print(f"{self.marke} ist {kilometer} Kilometer gefahren")
        self.kilometerstand_ausgeben()



########## MAIN ################
auto1 = Auto("BMW", "rot", 5 , 30000)
#auto1.marke = "BMW" # Attribute gibt es nur in diesem Objekt

auto2 = Auto("VW", "blau", 3 , 100000)
#auto2.marke = "VW" # Attribute gibt es nur in diesem Objekt

print(Auto.anzahl_reifen)
print(auto1,auto1.anzahl_reifen)
print(auto2,auto2.anzahl_reifen)
auto2.kilometerstand_ausgeben()
auto2.fahren(30)
