import math
def overeni_telefonniho_cisla(cislo):
    cislo_bez_mezer = cislo.replace(" ", "")
    if len(cislo_bez_mezer) == 9:
        return True
    elif len(cislo_bez_mezer) == 13:
        prvni_ctyri_znaky = cislo_bez_mezer[:4]
        if prvni_ctyri_znaky == "+420":
            return True
        else: return False
    else: return False

def cena_zpravy(pocet_znaku):
    cena = 0
    delka = math.ceil(len(pocet_znaku)/180)
    cena = 3*delka
    return cena



zadane_cislo = input("Zadej telefonni cislo, kam chces poslat SMS: ")
if overeni_telefonniho_cisla(zadane_cislo) == True:
    text_zpravy = input(" Zadej text zpravy: ")
    print(f"Cena zpravy je {cena_zpravy(text_zpravy)} Kc")
else: print("Cislo ma chybny format!")
#print(overeni_telefonniho_cisla(zadane_cislo))