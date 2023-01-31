#megoldas
def eredmeny():
    J_lapok_szama = 22
    if J_lapok_szama > 21:
        print("jatekos vesztett")
    elif J_lapok_szama > 15:
        print("Jatekos nyert")
def lapok_osszege():
    lapok = 0
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]
    return
#teszt esetek