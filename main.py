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
    print("jatekosVesztettTeszt:")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()

def jatekosVesztettTobbLappalTeszt():
    jatekos = [1, 2, 3, 4, 5, 12]
    gep = [1, 2, 3, 4]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekosVesztettTobbLappalTeszt:")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def jatekosVesztettUgyannanyiLapTeszt():
    jatekos = [9, 10, 12]
    gep = [1, 2, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekosVesztettUgyannanyiLapTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def gepVesztettTeszt():
    print("gepVesztettTeszt")
    jatekos = [1, 2, 3, 4]
    gep = [12, 11]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()

def gepVesztettTobbLappalTeszt():
    jatekos = [1, 2, 3, 4]
    gep = [1, 2, 3, 4, 5, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gepVesztettTobbLappalTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def gepVesztettUgyannanyiLapTeszt():
    jatekos = [1, 2, 3]
    gep = [9, 10, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gepVesztettUgyannanyiLapTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def dontetlenUgyanannyiLapTeszt():
    jatekos = [12, 11]
    gep = [12, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen"
    print("dontetlenUgyanannyiLapTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def dontetlenJatekosTobbLapTeszt():
    jatekos = [6, 6, 11]
    gep = [12, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen"
    print("dontetlenJatekosTobbLapTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()

def dontetlenGepTobbLapTeszt():
    jatekos = [12, 11]
    gep = [6, 6, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen"
    print("dontetlenGepTobbLapTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()
def jatekFolytatodikTeszt():
    jatekos = [1, 5]
    gep = [4, 2]
    kapott = eredmeny(jatekos, gep)
    vart = ""
    print("jatekFolytatodikTeszt")
    if kapott == vart:
        print("sikeres")
    else:
        print("teszt megbukott")
    print()

def tesztek():
    jatekosVesztettTeszt()
    jatekosVesztettTobbLappalTeszt()
    jatekosVesztettUgyannanyiLapTeszt()

    gepVesztettTeszt()
    gepVesztettTobbLappalTeszt()
    gepVesztettUgyannanyiLapTeszt()

    dontetlenUgyanannyiLapTeszt()
    dontetlenJatekosTobbLapTeszt()
    dontetlenGepTobbLapTeszt()

    jatekFolytatodikTeszt()

tesztek()