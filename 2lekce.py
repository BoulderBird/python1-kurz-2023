pekarna = {"houska":10, "rohlik":2, "chleba":40, "loupak":20}
#produkty = ["housky", "rohlik", "chleba", "loupak"]
#cena = [10,2,40,20]

#print(pekarna)
#print(pekarna["houska"])
#klic = "rohlik"
#print(f"klic:  {klic}, hodnota: {pekarna[klic]}")

"""
produkt = input("Zadej produkt: ")

if produkt in pekarna:

    print(f"{produkt} stoji {pekarna[produkt]} korun.")

else: 
    print(f"Bohuzel, produkt {produkt} neprodavame") """
"""""
pekarna["zavin"] = 30
pekarna["muffin"] =15
pekarna.pop("houska")
print(pekarna)"""


vysvedceni = {
    "CJ" : 1,
    "MA" : 2,
    "FY" : 3
}
print(vysvedceni)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

sales["Noc, ktera me zabila"] = 0
sales["Vrah zavolá v deset"]  = sales["Vrah zavolá v deset"] + 100

print(sales)

tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}

cislo_listku = int(input("Napis cislo listku:"))

if cislo_listku in tombola:
    print(f"Vyhral jsi {tombola[cislo_listku]} ")
else: print("Bohužel nevyhráváš nic.")

passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jmeno = input("Zadej jmeno: ")

if jmeno in passwords:
    heslo = input("Zadej heslo: ")
    if passwords[jmeno] == heslo:
        print("Vitej")
    else: print("spatne heslo")
else: print("nejsi zvany")
