class Haustier:

    def __init__(self, name, alter, hunger, zufriedenheit):
        self.name = name
        self.alter = alter
        self.hunger = hunger
        self.zufriedenheit = zufriedenheit

    def print_zufriedenheit(self):
        return f"Zufriedenheit steigt auf {self.zufriedenheit}"
    
    def essen(self):
        self.hunger = False
        self.zufriedenheit += 10
        print(self.name,"Lecker",self.print_zufriedenheit())

    def streicheln(self):
        self.zufriedenheit += 8
        print(self.name,"Ich werde gestreichelt!")    
    
    def schlafen(self):
        print(self.name,"Ich schlafe")


class Hund(Haustier):

    def __init__(self, name, alter, hunger, zufriedenheit, rasse):
        super().__init__(name, alter, hunger, zufriedenheit)
        self.rasse = rasse
        
    def stoeckchen_holen(self):
        self.zufriedenheit += 10
        self.hunger = True
        print(self.name,"Stöckchen holen",self.print_zufriedenheit())

class Katze(Haustier):

    def __init__(self, name, alter, hunger, zufriedenheit, augenfarbe):
        super().__init__(name, alter, hunger, zufriedenheit)
        self.augenfarbe = augenfarbe

    def kratzbaum_kratzen(self):
        self.zufriedenheit += 5
        self.hunger = True
        print(self.name,"Kratz!",self.print_zufriedenheit())

class Buch():

    def __init__(self, titel, autor, anzahl_seiten):
        self.titel = titel
        self.autor = autor
        self.anzahl_seiten = anzahl_seiten
    
    def __len__(self):
        return self.anzahl_seiten
    
    def __str__(self):
        return self.titel
    
    def __add__(self, other):
        return self.anzahl_seiten + other.anzahl_seiten
    
    def __eq__(self, other):
        return self.autor == other.autor and self.titel == other.titel
    
    def ueber_tausend_seiten(self):
        return self.anzahl_seiten > 1000



########## MAIN ################
hund1 = Hund("Hundi", 7, True, 5, "Dackel")
katze1 = Katze("Tiggi", 5, True, 5, "braun")

#print(hund1.name)
#print(katze1.name)

hund1.stoeckchen_holen()
katze1.kratzbaum_kratzen()
hund1.essen()
katze1.essen()

titel1= "Harry Potter und der Feuerkelch"
titel2= "Harry Potter und der Halbblutprinz"
autor = "J.K. Rowling"

feuerkelch = Buch(titel1, autor, 767)
feuerkelch2 = Buch(titel1, autor, 167)
halbblutprinz = Buch(titel2, autor, 767)

print("Seitenanzahl:",len(feuerkelch))
print(str(feuerkelch))
print(feuerkelch + halbblutprinz)
print(feuerkelch == feuerkelch2)
print(type(5))
print(type("a, b"))
print(type([1, 2]))