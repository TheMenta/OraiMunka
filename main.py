#megoldas
def eredmeny(g_lapok:[int],j_lapok:[int]):
    j_pontok = lapok_osszege(j_lapok)
    g_pontok = lapok_osszege(g_lapok)
    if j_pontok > 21:
        allapot ="jatekos vesztett"
    elif g_pontok > 21:
        allapot = "gep vesztett"
    return allapot

def lapok_osszege(lapok:[int]):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok
#teszt esetek
def teszt_esetek():
    jatekos_vesztett_teszt()

def jatekos_vesztett_teszt():
    jatekos = [10,9,3]
    gep = [10,9]
    vart_eredmeny ="jatekos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")
teszt_esetek()
