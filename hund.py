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



########## MAIN ################
hund1 = Hund("Hundi", 7, True, 5, "Dackel")
katze1 = Katze("Tiggi", 5, True, 5, "braun")

#print(hund1.name)
#print(katze1.name)

hund1.stoeckchen_holen()
katze1.kratzbaum_kratzen()
hund1.essen()
katze1.essen()