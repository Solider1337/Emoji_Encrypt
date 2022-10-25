#odszyfrowywanie
def odszyfrowanie(x):
    message = x
    hashwiadomosc = '#'.join(message[i:i + 1] for i in range(0, len(message), 1))
    words = hashwiadomosc.split('#')

    emotki = {
        "😀": "a", "😁": "A",
        "😂": "b", "🤣": "B",
        "😃": "c", "😄": "C",
        "😅": "d", "😆": "D",
        "😉": "e", "😊": "E",
        "😋": "f", "😎": "f",
        "😍": "g", "😘": "G",
        "🥰": "h", "😗": "H",
        "😙": "i", "🥲": "I",
        "😚": "j", "🤥": "J",
        "🙂": "k", "🤗": "K",
        "🤩": "l", "🤔": "L",
        "🤨": "m", "😐": "M",
        "😑": "n", "😶": "N",
        "🤑": "o", "🙄": "O",
        "😏": "p", "😣": "P",
        "😥": "r", "😮": "R",
        "🤐": "s", "😯": "S",
        "😪": "t", "😫": "T",
        "🥱": "u", "😴": "U",
        "😌": "v", "😛": "V",
        "😜": "w", "😝": "W",
        "🤤": "x", "😒": "X",
        "😓": "y", "😔": "Y",
        "😕": "z", "🙃": "Z",
        "❤": "0",
        "🧡": "1",
        "💛": "2",
        "💚": "3",
        "💙": "4",
        "💜": "5",
        "🤎": "6",
        "🖤": "7",
        "🤍": "8",
        "💔": "9",
        "🌞": " ",
        "😺": ".",
        "😸": ",",
        "😹": "!",
        "😻": "?",
        "😼": "@",
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
        "a": "😀", "A": "😁",
        "b": "😂", "B": "🤣",
        "c": "😃", "C": "😄",
        "d": "😅", "D": "😆",
        "e": "😉", "E": "😊",
        "f": "😋", "F": "😎",
        "g": "😍", "G": "😘",
        "h": "🥰", "H": "😗",
        "i": "😙", "I": "🥲",
        "j": "😚", "J": "🤥",
        "k": "🙂", "K": "🤗",
        "l": "🤩", "L": "🤔",
        "m": "🤨", "M": "😐",
        "n": "😑", "N": "😶",
        "o": "🤑", "O": "🙄",
        "p": "😏", "P": "😣",
        "r": "😥", "R": "😮",
        "s": "🤐", "S": "😯",
        "t": "😪", "T": "😫",
        "u": "🥱", "U": "😴",
        "v": "😌", "V": "😛",
        "w": "😜", "W": "😝",
        "x": "🤤", "X": "😒",
        "y": "😓", "Y": "😔",
        "z": "😕", "Z": "🙃",
        "0": "❤",
        "1": "🧡",
        "2": "💛",
        "3": "💚",
        "4": "💙",
        "5": "💜",
        "6": "🤎",
        "7": "🖤",
        "8": "🤍",
        "9": "💔",
        " ": "🌞",
        ".": "😺",
        ",": "😸",
        "!": "😹",
        "?": "😻",
        "@": "😼",
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
x = int(input("Wybierz opcję z menu: "))

if x == 1:
    szyfrowanie()
elif x == 2:
    bezpieczny_text = input("Wpisz tekst do odzaszyfrowania: ")
    odszyfrowanie(bezpieczny_text)