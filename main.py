# megoldás


def eredmeny(jatekosLapok: list, gepLapok: list):
    szoveg = ""
    jatekos = pontszamitas(jatekosLapok)
    gep = pontszamitas(gepLapok)

    if jatekos > 21 and gep > 21:
        szoveg = "döntetlen"
    elif jatekos > 21:
        szoveg = "vesztettél"
    elif gep > 21:
        szoveg = "nyertél"
    return szoveg


def pontszamitas(lista: list):
    sum = 0
    for ix in lista:
        sum += ix
    return sum
    # return sum(lista)


# teszesetek

def jatekosVesztettTeszt():
    jatekos = [12, 11]
    gep = [1, 2, 3, 4]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")


jatekosVesztettTeszt()

print("sus"*69)