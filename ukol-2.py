sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod = input("Zadej kod soucastky: ")
mnozstvi = int(input("Zadej pocet soucastek: "))
if kod in sklad:
    if mnozstvi <= sklad[kod]:
        print(f"Soucastka {kod} je skladem v pozadovanem mnozstvi.")
        sklad[kod] -= mnozstvi
        #print(sklad)
    else:
        print(f"Lze prodat pouze omezene mnozstvi kusu - {sklad[kod]}")
        odebrana_soucastka = sklad.pop(kod)
        #print(sklad)
else:
    print("Soucastka neni skladem.")


#Bonus 1
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
text = input("Zadej text, ktery chces napsat v Morseove abecede: ")

    
for znak in text:
    if znak == " ":
        print("/", end=" ")
    else: print(morse_code[znak], end=" ")