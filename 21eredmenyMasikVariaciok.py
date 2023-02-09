# megoldás
def eredmeny(jatekosLapok: list, gepLapok: list):
    try:
        gPont = pontszamitas(gepLapok)
        jPont = pontszamitas(jatekosLapok)

        gDb = len(gepLapok)
        jDb = len(jatekosLapok)

        if gPont > 21 and jPont > 21:
                szoveg = "döntetlen, a ház nyert"
        elif jPont == 21 and gPont == 21:
                szoveg = "döntetlen, osztoztok a nyereségen"
        elif jPont == 21:
                szoveg= "nyertél"
        elif gPont == 21:
                szoveg= "vesztettél"
        elif gPont > 21:
                szoveg = "nyertél"
        elif jPont > 21:
                szoveg = "vesztettél"
        elif jPont > gPont:
                szoveg = "nyertél"
        elif jPont < gPont:
                szoveg = "vesztettél"
        elif gDb > jDb:
                szoveg = "nyertél"
        elif gDb < jDb:
                szoveg = "vesztettél"
        else:
                szoveg = "döntetlen, osztoztok a nyereségen"
    except:
        return "hiba"
    return szoveg

def pontszamitas(lista: list):
    sum = 0
    for ix in lista:
        sum += ix
    return sum


# teszesetek
def jatekosNagyobb21Teszt():
    jatekos = [12, 10]
    gep = [1, 2, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Nagyobb 21 Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def gepNagyobb21Teszt():
    jatekos = [2, 3, 5]
    gep = [12, 10]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Nagyobb 21 Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def mindenkiVeszitTeszt():
    jatekos = [12, 11]
    gep = [12, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, a ház nyert"
    print("mindenki Veszit Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()









def jatekosNyerKevesebbLappalTeszt():
    jatekos = [12, 7]
    gep = [12, 4, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("jatekos Nyer Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def jatekosNyerTobbLappalTeszt():
    jatekos = [12, 2, 5]
    gep = [12, 6]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("jatekos Nyer Tobb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def jatekosNyer21PonttalTeszt():
    jatekos = [12, 8, 1]
    gep = [12, 6, 1]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("jatekos Nyer 21 Ponttal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()



def jatekosVeszitKevesebbLappalTeszt():
    jatekos = [12, 7]
    gep = [12, 4, 4]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Veszit Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def jatekosVeszitTobbLappalTeszt():
    jatekos = [12, 2, 5]
    gep = [12, 7]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Veszit Tobb Lappal Teszt")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def jatekosDontetlen21PonttalTeszt():
    jatekos = [12, 8, 1]
    gep = [12, 8, 1]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, osztoztok a nyereségen"
    print("jatekos Dontetlen 21 Ponttal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()







def gepNyerKevesebbLappalTeszt():
    jatekos = [12, 4, 3]
    gep = [12, 7]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("gep Nyer Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def gepNyerTobbLappalTeszt():
    jatekos = [12, 6]
    gep = [12, 2, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("gep Nyer Tobb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def gepNyer21PonttalTeszt():
    jatekos = [12, 6, 1]
    gep = [12, 8, 1]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("gep Nyer 21 Ponttal Teszt")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()



def gepVeszitKevesebbLappalTeszt():
    jatekos = [12, 4, 4]
    gep = [12, 7]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Veszit Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def gepVeszitTobbLappalTeszt():
    jatekos = [12, 7]
    gep = [12, 2, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Veszit Tobb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
def gepDontetlen21PonttalTeszt():
    jatekos = [12, 8, 1]
    gep = [12, 8, 1]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, osztoztok a nyereségen"
    print("gep Dontetlen 21 Ponttal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()







def dontetlen():
    print("\n\n\ndöntetlen tesztek:\n")
    mindenkiVeszitTeszt()
    jatekosDontetlen21PonttalTeszt()
    gepDontetlen21PonttalTeszt()

def jatekosNyer():
    print("\n\n\njátékos nyer tesztek:\n")
    gepNagyobb21Teszt()

    jatekosNyerKevesebbLappalTeszt()
    jatekosNyerTobbLappalTeszt()
    jatekosNyer21PonttalTeszt()

    gepVeszitKevesebbLappalTeszt()
    gepVeszitTobbLappalTeszt()

def gepNyer():
    print("\n\n\ngép nyer tesztek:\n")
    jatekosNagyobb21Teszt()

    gepNyerKevesebbLappalTeszt()
    gepNyerTobbLappalTeszt()
    gepNyer21PonttalTeszt()

    jatekosVeszitKevesebbLappalTeszt()
    jatekosVeszitTobbLappalTeszt()




def tesztek():

    dontetlen()
    gepNyer()
    jatekosNyer()





tesztek()
