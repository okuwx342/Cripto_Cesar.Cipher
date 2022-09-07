def cripto(frase):
    tradutor = ""
    for letra in frase:
        if letra in "Aa":
            tradutor = tradutor + "T"
        elif letra in "Bb":
            tradutor = tradutor + "U"
        elif letra in "Cc":
            tradutor = tradutor + "V"
        elif letra in "Dd":
            tradutor = tradutor + "W"
        elif letra in "Ee":
            tradutor = tradutor + "X"
        elif letra in "Ff":
            tradutor = tradutor + "Y"
        elif letra in "Gg":
            tradutor = tradutor + "Z"
        elif letra in "Hh":
            tradutor = tradutor + "A"
        elif letra in "Ii":
            tradutor = tradutor + "B"
        elif letra in "Jj":
            tradutor = tradutor + "C"
        elif letra in "Kk":
            tradutor = tradutor + "D"
        elif letra in "Ll":
            tradutor = tradutor + "E"
        elif letra in "Mm":
            tradutor = tradutor + "F"
        elif letra in "Nn":
            tradutor = tradutor + "G"
        elif letra in "Oo":
            tradutor = tradutor + "H"
        elif letra in "Pp":
            tradutor = tradutor + "I"
        elif letra in "Qq":
            tradutor = tradutor + "J"
        elif letra in "Rr":
            tradutor = tradutor + "K"
        elif letra in "Ss":
            tradutor = tradutor + "L"
        elif letra in "Tt":
            tradutor = tradutor + "M"
        elif letra in "Uu":
            tradutor = tradutor + "N"
        elif letra in "Vv":
            tradutor = tradutor + "O"
        elif letra in "Ww":
            tradutor = tradutor + "P"
        elif letra in "Xx":
            tradutor = tradutor + "Q"
        elif letra in "Yy":
            tradutor = tradutor + "R"
        elif letra in "Zz":
            tradutor = tradutor + "S"
        else:
            tradutor = tradutor + letra
    return tradutor

print(cripto(input("Digite sua frase: ")))