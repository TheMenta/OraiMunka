#megoldas
def eredmeny(g_lapok:[int],j_lapok:[int]):
    j_pontok = lapok_osszege(j_lapok)
    g_pontok = lapok_osszege(g_lapok)
    allapot = " "
    if j_pontok > 21:
        allapot ="jatekos vesztett"
    elif g_pontok > 21:
        allapot = "gep vesztett"
    elif j_pontok == g_pontok:
        allapot = "dontetlen"
    elif j_pontok == 21:
        allapot = "jatekos nyert"
    elif g_pontok == 21:
        allapot = "gep nyert"
    elif 21 > g_pontok > j_pontok:
        allapot = "gep nyert"
    elif 21 > j_pontok > g_pontok:
        allapot = "jatekos nyert"
    elif j_pontok == g_pontok:
        print("döntetlen")


    return allapot

def lapok_osszege(lapok: [int]):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return pontok
#teszt esetek
def teszt_esetek():
    jatekos_vesztett_teszt()
    jatekos_kisebblapok_teszt()
    gep_vesztett_teszt()
    gep_kisebblapok_teszt()
    dontetlen_teszt()
def jatekos_vesztett_teszt():
    jatekos = [10,9,3]
    gep = [10,9]
    vart_eredmeny ="jatekos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)
    print("ez, itt a jatekos vesztett,tul-21")
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")

def gep_vesztett_teszt():
    jatekos = [10,9]
    gep = [10,9,3]
    vart_eredmeny ="gep vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")


def dontetlen_teszt():
    jatekos = [10,9]
    gep = [10,9,]
    vart_eredmeny ="dontetlen"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")
def dontetlen_teszt1():
    jatekos = [10, 3, 6, 2]
    gep = [10, 5, 4, 2]
    vart_eredmeny ="dontetlen"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")

def jatekos_kisebblapok_teszt():
    jatekos = [10,6]
    gep = [10,9]
    vart_eredmeny ="gep nyert"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")


def gep_kisebblapok_teszt():
    jatekos = [10,9,]
    gep = [10,2]
    vart_eredmeny ="jatekos nyert"
    kapott_eredmeny = eredmeny(gep,jatekos)
    if kapott_eredmeny == vart_eredmeny:
        print("teszt sikeres")
    else:
        print("nem sikerult")

teszt_esetek()