class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostupne = True):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = dostupne

    def get_info(self):
        return f"Registrační značka vozidla: {self.registracni_znacka}, typ vozidla: {self.typ_vozidla}"
    
    def pujc_auto(self):
        if self.dostupne == True:
            print("Potvrzuji zapůjčení vozidla")
            self.dostupne = False
        else: print("Vozidlo není k dispozici")

    def vrat_auto(self, stav_tachometru, doba_zapujcky):
        self.stav_tachometru = stav_tachometru
        self.doba_zapujcky = doba_zapujcky
        self.najete_km += stav_tachometru
        self.dostupne = True
        cena = 0
        if doba_zapujcky < 7:
            cena = doba_zapujcky * 400
            return F"Cena za zapůjčení vozidla je {cena} Kč"
        else:
            cena = doba_zapujcky * 300
            return F"Cena za zapůjčení vozidla je {cena} Kč"

    
peugeot = Auto("4A2 3020","Peugeot 403 Cabrio", 47534, True )
skoda = Auto("1P3 4747","Škoda Octavia", 41253, True )

print(skoda.vrat_auto(1000,5))
print(skoda.najete_km)
print(peugeot.vrat_auto(2000, 8))
print(peugeot.najete_km)

while True:
    vybrane_vozidlo = input("Na výběr je značka Peugeot nebo Škoda. Zadej značku vozidla, které chceš půjčit: ")

    if vybrane_vozidlo == "Peugeot":
        print(peugeot.get_info())
        peugeot.pujc_auto()
    elif vybrane_vozidlo == "Škoda":
        print(skoda.get_info())
        skoda.pujc_auto()
    else: print("Takové vozidlo nemáme k dispozici.")

