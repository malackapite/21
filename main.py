# megoldás
def eredmeny(jatekosLapok: list, gepLapok: list):
    try:
        gPont = pontszamitas(gepLapok)
        jPont = pontszamitas(jatekosLapok)

        gDb = len(gepLapok)
        jDb = len(jatekosLapok)

        if gPont > 21 and jPont > 21:
                szoveg = "döntetlen, a ház nyert"
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
def jatekosNagyobb21KevesebbLappalTeszt():
    jatekos = [12, 10]
    gep = [1, 2, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Nagyobb 21 Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
    
def jatekosNagyobb21TobbLappalTeszt():
    jatekos = [6, 6, 5, 5]
    gep = [1, 2, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Nagyobb 21 Tobb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
    
def jatekosNagyobb21UgyanannyiLappalTeszt():
    jatekos = [12, 5, 5]
    gep = [1, 2, 3]
    kapott = eredmeny(jatekos, gep)
    vart = "vesztettél"
    print("jatekos Nagyobb 21 Ugyanannyi Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()





def gepNagyobb21KevesebbLappalTeszt():
    jatekos = [2, 3, 5]
    gep = [12, 10]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Nagyobb 21 Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()

def gepNagyobb21TobbLappalTeszt():
    jatekos = [2, 3, 5]
    gep = [6, 6, 5, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Nagyobb 21 Tobb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()

def gepNagyobb21UgyanannyiLappalTeszt():
    jatekos = [2, 3, 5]
    gep = [12, 5, 5]
    kapott = eredmeny(jatekos, gep)
    vart = "nyertél"
    print("gep Nagyobb 21 Kevesebb Lappal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()







def mindenkiVeszitUgyanannyiLapTeszt():
    jatekos = [12, 11]
    gep = [12, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, a ház nyert"
    print("mindenki Veszit Ugyanannyi Lap Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
    
def mindenkiVeszitGeptobbLapTeszt():
    jatekos = [12, 11]
    gep = [12, 6, 7]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, a ház nyert"
    print("mindenki Veszit Gep tobb Lap Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()
    
def mindenkiVeszitJatekostobbLapTeszt():
    jatekos = [12, 4, 8]
    gep = [12, 12]
    kapott = eredmeny(jatekos, gep)
    vart = "döntetlen, a ház nyert"
    print("mindenki Veszit Jatekos tobb Lap Teszt:")
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




def hibakezelesGepnelTeszt():
    jatekos = [12, 6]
    gep = "szöveg"
    kapott = eredmeny(jatekos, gep)
    vart = "hiba"
    print("hibakezeles Gepnel Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()

def hibakezelesJatekosnalTeszt():
    jatekos = "szöveg"
    gep = [12, 6]
    kapott = eredmeny(jatekos, gep)
    vart = "hiba"
    print("hibakezeles Jatekosnal Teszt:")
    if kapott == vart:
        print("sikeres teszt")
    else:
        print("teszt megbukott")
    print()








def dontetlen():
    mindenkiVeszitUgyanannyiLapTeszt()
    mindenkiVeszitGeptobbLapTeszt()
    mindenkiVeszitJatekostobbLapTeszt()

def jatekosNyer():
    gepNagyobb21KevesebbLappalTeszt()
    gepNagyobb21TobbLappalTeszt()
    gepNagyobb21UgyanannyiLappalTeszt()

    jatekosNyerKevesebbLappalTeszt()
    jatekosNyerTobbLappalTeszt()

def gepNyer():
    jatekosNagyobb21KevesebbLappalTeszt()
    jatekosNagyobb21TobbLappalTeszt()
    jatekosNagyobb21UgyanannyiLappalTeszt()

    gepNyerKevesebbLappalTeszt()
    gepNyerTobbLappalTeszt()
    
    
    
    
    
def tesztek():

    dontetlen()
    gepNyer()
    jatekosNyer()

    hibakezelesGepnelTeszt()
    hibakezelesJatekosnalTeszt()





tesztek()
