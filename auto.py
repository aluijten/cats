class Auto:

    ANZAHL_REIFEN = 4                           # Klassenvariable
    winterreifen_noetig = False                 # Klassenvariable
    anzahl_autos = 0

    def __init__(self, marke, farbe, sitze, kilometerstand):
        #print("Init methode")
        self.marke = marke                      # Instanzvariable
        self.farbe = farbe                      # Instanzvariable
        self.sitze = sitze                      # Instanzvariable
        self.kilometerstand = kilometerstand    # Instanzvariable
        Auto.anzahl_autos += 1
    
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
auto3 = Auto("Audi", "grün", 6 , 10)

print("Anzahl Reifen",Auto.ANZAHL_REIFEN)
print("Winterreifen notwendig",Auto.winterreifen_noetig)
Auto.winterreifen_noetig = True
print("Winterreifen notwendig",Auto.winterreifen_noetig)
auto1.winterreifen_noetig = False
auto1.ANZAHL_REIFEN = 6
print(auto1,auto1.ANZAHL_REIFEN,auto1.winterreifen_noetig)
print(auto2,auto2.ANZAHL_REIFEN,auto2.winterreifen_noetig)
auto2.kilometerstand_ausgeben()
auto2.fahren(30)
print("Es gibt",Auto.anzahl_autos,"Autos")
