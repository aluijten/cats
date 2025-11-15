marke = "BMW"
farbe = "rot"
sitze = 5
kilometerstand = 30000
aktueller_tank = 30
max_tank = 40

def kilometerstand_anzeigen():
    print(kilometerstand)

def tank_auffuellen():
    global aktueller_tank
    global max_tank
    print(f"Tank mit {max_tank - aktueller_tank} Liter betankt")
    aktueller_tank = max_tank

kilometerstand_anzeigen()
tank_auffuellen()