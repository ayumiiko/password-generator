import random

def password():
    laenge = int(input("laenge:"))
    alphabet = zahlen = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0" "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M" "q", "w", "e", "r", "t", "z", "u", "i", "o", "p", "ü", "a", "s", "d", "f", "g", "h", "j", "k", "l", "ö", "ä", "y", "x", "c", "v", "b", "n", "m" "^", "!", "\"", "§", "$", "%", "&", "/", "(", ")", "=", "?", "ß", "\\", "+", "*", "<", ">", "|", "'", "#", ",", ";", ":", "-", "_", "{", "}", "[", "]", "~")
    pwd = ''
    for i in range(laenge):
        pwd += ''.join(random.choice(alphabet))
    print(pwd) 

if __name__ == "__main__":
    password()
