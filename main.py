#megoldás
def eredmeny(jatekos, gep):
    szoveg=""
    if jatekos > 21 and gep > 21:
        szoveg="döntetlen"
    elif jatekos > 21:
        szoveg="vesztettél"
    elif gep > 21:
        szoveg ="nyertél"
    return szoveg
#teszesetek