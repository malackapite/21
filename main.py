#megoldás
def eredmeny(jatekosLapok, gepLapok):
    szoveg=""
    jatekos=pontszamitas(jatekosLapok)
    gep=pontszamitas(gepLapok)

    if jatekos > 21 and gep > 21:
        szoveg="döntetlen"
    elif jatekos > 21:
        szoveg="vesztettél"
    elif gep > 21:
        szoveg ="nyertél"
    return szoveg
def pontszamitas(lista):
    sum=0
    for ix in lista:
        sum+=ix
    return sum
    #return sum(lista)
#teszesetek