jmeno = "Dana"
print(jmeno + "@czechitas.cz")

jmeno_a_prijmeni = input("Zadej jmeno a prijmeni: ")
print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
#print(jmeno_a_prijmeni[0].upper()+jmeno_a_prijmeni[1:].lower())
jmeno_a_prijmeni = jmeno_a_prijmeni.split()
print(jmeno_a_prijmeni[0][0].upper() + jmeno_a_prijmeni[0][1:].lower() + " " +jmeno_a_prijmeni[1][0].upper() + jmeno_a_prijmeni[1][1:].lower())
print(jmeno_a_prijmeni[0][0].upper() +". " + jmeno_a_prijmeni[1][0].upper() + ".")
delka_jmena = len(jmeno_a_prijmeni[0][0:])
if delka_jmena >= 5:
    print(jmeno_a_prijmeni[0][0].upper()+" " + jmeno_a_prijmeni[1][0].upper() + jmeno_a_prijmeni[1][1:].lower())
else:
    print(jmeno_a_prijmeni[0][0].upper() + jmeno_a_prijmeni[0][1:].lower() + " " +jmeno_a_prijmeni[1][0].upper() + jmeno_a_prijmeni[1][1:].lower())