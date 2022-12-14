#odszyfrowywanie
def odszyfrowanie(x):
    message = x
    hashwiadomosc = '#'.join(message[i:i + 1] for i in range(0, len(message), 1))
    words = hashwiadomosc.split('#')

    emotki = {
        "๐": "a", "๐": "A",
        "๐": "b", "๐คฃ": "B",
        "๐": "c", "๐": "C",
        "๐": "d", "๐": "D",
        "๐": "e", "๐": "E",
        "๐": "f", "๐": "f",
        "๐": "g", "๐": "G",
        "๐ฅฐ": "h", "๐": "H",
        "๐": "i", "๐ฅฒ": "I",
        "๐": "j", "๐คฅ": "J",
        "๐": "k", "๐ค": "K",
        "๐คฉ": "l", "๐ค": "L",
        "๐คจ": "m", "๐": "M",
        "๐": "n", "๐ถ": "N",
        "๐ค": "o", "๐": "O",
        "๐": "p", "๐ฃ": "P",
        "๐ฅ": "r", "๐ฎ": "R",
        "๐ค": "s", "๐ฏ": "S",
        "๐ช": "t", "๐ซ": "T",
        "๐ฅฑ": "u", "๐ด": "U",
        "๐": "v", "๐": "V",
        "๐": "w", "๐": "W",
        "๐คค": "x", "๐": "X",
        "๐": "y", "๐": "Y",
        "๐": "z", "๐": "Z",
        "โค": "0",
        "๐งก": "1",
        "๐": "2",
        "๐": "3",
        "๐": "4",
        "๐": "5",
        "๐ค": "6",
        "๐ค": "7",
        "๐ค": "8",
        "๐": "9",
        "๐": " ",
        "๐บ": ".",
        "๐ธ": ",",
        "๐น": "!",
        "๐ป": "?",
        "๐ผ": "@",
    }
    output = ""

    for word in words:
        output += emotki.get(word, word) + ""

    print("Tekst odszyfrowany: ", output)
    koniec=input()

#szyfrowanie
def szyfrowanie():
    message = input("Wpisz tekst do zaszyfrowania: ")
    hashwiadomosc = '#'.join(message[i:i + 1] for i in range(0, len(message), 1))
    words = hashwiadomosc.split('#')

#baza szyfru (tajne)
    emotki = {
        "a": "๐", "A": "๐",
        "b": "๐", "B": "๐คฃ",
        "c": "๐", "C": "๐",
        "d": "๐", "D": "๐",
        "e": "๐", "E": "๐",
        "f": "๐", "F": "๐",
        "g": "๐", "G": "๐",
        "h": "๐ฅฐ", "H": "๐",
        "i": "๐", "I": "๐ฅฒ",
        "j": "๐", "J": "๐คฅ",
        "k": "๐", "K": "๐ค",
        "l": "๐คฉ", "L": "๐ค",
        "m": "๐คจ", "M": "๐",
        "n": "๐", "N": "๐ถ",
        "o": "๐ค", "O": "๐",
        "p": "๐", "P": "๐ฃ",
        "r": "๐ฅ", "R": "๐ฎ",
        "s": "๐ค", "S": "๐ฏ",
        "t": "๐ช", "T": "๐ซ",
        "u": "๐ฅฑ", "U": "๐ด",
        "v": "๐", "V": "๐",
        "w": "๐", "W": "๐",
        "x": "๐คค", "X": "๐",
        "y": "๐", "Y": "๐",
        "z": "๐", "Z": "๐",
        "0": "โค",
        "1": "๐งก",
        "2": "๐",
        "3": "๐",
        "4": "๐",
        "5": "๐",
        "6": "๐ค",
        "7": "๐ค",
        "8": "๐ค",
        "9": "๐",
        " ": "๐",
        ".": "๐บ",
        ",": "๐ธ",
        "!": "๐น",
        "?": "๐ป",
        "@": "๐ผ",
    }
    output = ""

    for word in words:
        output += emotki.get(word, word) + ""

    print("Tekst zaszyfrowany: ",output)
    odszyfrowanie(output)
    koniec=input()


print("[=========MENU=========]")
print("|----1. Szyfrowanie----|")
print("|--2. Odszyfrowywanie--|")
print("[======================] \n")
x = 1
x = int(input("Wybierz opcjฤ z menu: "))

if x == 1:
    szyfrowanie()
elif x == 2:
    bezpieczny_text = input("Wpisz tekst do odzaszyfrowania: ")
    odszyfrowanie(bezpieczny_text)