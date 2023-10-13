import json
hodnoceni = {}
with open("body.json", mode="r", encoding="utf8") as file:
    data = json.load(file)
#print(data)
for zak, body in data.items():
    #print(f"Zak {zak} ma {body} bodu.")
    if body >= 60:
        #print (f"Zak {zak} : Pass")
        body = "Pass"
        #print (f"Zak {zak} : {body}")
        hodnoceni[zak]=body
    else: 
        #print (f"Zak {zak} : Fail")
        body = "Fail"
        #print (f"Zak {zak} : {body}")
        hodnoceni[zak]=body
#print(hodnoceni)
with open('prospech.json', 'w', encoding="utf8") as file2:
    json.dump(hodnoceni, file2)
#with open('prospech.json', 'r', encoding="utf8") as file3:
#    nactena_data = json.load(file3)
#print(nactena_data)

#bonus
with open("bonusy.json", mode="r", encoding="utf8") as file4:
    data_bonusy = json.load(file4)
#print(data_bonusy)
slovnik_bonusaru = {}
for klic in set(data_bonusy) | set(data):
    body_test =data_bonusy.get(klic, 0)  # Pokud klíč neexistuje v slovníku 1, použijeme 0
    bonusove_body = data.get(klic, 0) # Pokud klíč neexistuje v slovníku 2, použijeme 0
    slovnik_bonusaru[klic] = body_test+ bonusove_body

#print(slovnik_bonusaru)
for zak, soucet in slovnik_bonusaru.items():
    if soucet >= 90:
        soucet = 1
        slovnik_bonusaru[zak] = soucet
    elif soucet >= 70:  
        soucet = 2
        slovnik_bonusaru[zak] = soucet
    elif soucet >= 50:  
         soucet = 3
         slovnik_bonusaru[zak] = soucet
    elif soucet >= 30:  
         soucet = 4
         slovnik_bonusaru[zak] = soucet
    else:  
         soucet = 5
         slovnik_bonusaru[zak] = soucet 
#print(slovnik_bonusaru)
with open('znamky.json', 'w', encoding="utf8") as file5:
    json.dump(slovnik_bonusaru, file5)
#with open('znamky.json', 'r', encoding="utf8") as file6:
#    nactene_znamky = json.load(file6)
#print(nactene_znamky)