# print ("Program sprawdzający dane w dwóch listach")
# coding=utf8
from glowna import bol_g, wlosy_g, grypa_odpornosc_g, opryszczka_masc_g, opryszcza_odpornosc_g, nogi_g, \
    hemoroidy_masc_g, hemoroidy_czopki_g, furagina_zurawina_g, alergia_calcium_g, alergia_inne_g, antybiotyk_g, \
    biegunka_elektrolity_g
from komplementarna import bol_k, wlosy_k, grypa_odpornosc_k, opryszczka_masc_k, opryszcza_odpornosc_k, nogi_k, \
    hemoroidy_masc_k, hemoroidy_czopki_k, furagina_zurawina_k, alergia_calcium_k, alergia_inne_k, antybiotyk_k, \
    biegunka_elektrolity_k

import re
# from tkinter import *


def zmiana_liter():
    for i in range(len(bol_g)):
        bol_g[i] = bol_g[i].lower()
    for i in range(len(bol_k)):
        bol_k[i] = bol_k[i].lower()

    for i in range(len(wlosy_g)):
        wlosy_g[i] = wlosy_g[i].lower()
    for i in range(len(wlosy_k)):
        wlosy_k[i] = wlosy_k[i].lower()

    for i in range(len(grypa_odpornosc_g)):
        grypa_odpornosc_g[i] = grypa_odpornosc_g[i].lower()
    for i in range(len(grypa_odpornosc_k)):
        grypa_odpornosc_k[i] = grypa_odpornosc_k[i].lower()

    for i in range(len(opryszczka_masc_g)):
        opryszczka_masc_g[i] = opryszczka_masc_g[i].lower()
    for i in range(len(opryszczka_masc_k)):
        opryszczka_masc_k[i] = opryszczka_masc_k[i].lower()

    for i in range(len(opryszcza_odpornosc_g)):
        opryszcza_odpornosc_g[i] = opryszcza_odpornosc_g[i].lower()
    for i in range(len(opryszcza_odpornosc_k)):
        opryszcza_odpornosc_k[i] = opryszcza_odpornosc_k[i].lower()

    for i in range(len(nogi_g)):
        nogi_g[i] = nogi_g[i].lower()
    for i in range(len(nogi_k)):
        nogi_k[i] = nogi_k[i].lower()

    for i in range(len(hemoroidy_masc_g)):
        hemoroidy_masc_g[i] = hemoroidy_masc_g[i].lower()
    for i in range(len(hemoroidy_masc_k)):
        hemoroidy_masc_k[i] = hemoroidy_masc_k[i].lower()

    for i in range(len(hemoroidy_czopki_g)):
        hemoroidy_czopki_g[i] = hemoroidy_czopki_g[i].lower()
    for i in range(len(hemoroidy_czopki_k)):
        hemoroidy_czopki_k[i] = hemoroidy_czopki_k[i].lower()

    for i in range(len(furagina_zurawina_g)):
        furagina_zurawina_g[i] = furagina_zurawina_g[i].lower()
    for i in range(len(furagina_zurawina_k)):
        furagina_zurawina_k[i] = furagina_zurawina_k[i].lower()

    for i in range(len(alergia_calcium_g)):
        alergia_calcium_g[i] = alergia_calcium_g[i].lower()
    for i in range(len(alergia_calcium_k)):
        alergia_calcium_k[i] = alergia_calcium_k[i].lower()

    for i in range(len(alergia_inne_g)):
        alergia_inne_g[i] = alergia_inne_g[i].lower()
    for i in range(len(alergia_inne_k)):
        alergia_inne_k[i] = alergia_inne_k[i].lower()

    for i in range(len(antybiotyk_g)):
        antybiotyk_g[i] = antybiotyk_g[i].lower()
    for i in range(len(antybiotyk_k)):
        antybiotyk_k[i] = antybiotyk_k[i].lower()

    for i in range(len(biegunka_elektrolity_g)):
        biegunka_elektrolity_g[i] = biegunka_elektrolity_g[i].lower()
    for i in range(len(biegunka_elektrolity_k)):
        biegunka_elektrolity_k[i] = biegunka_elektrolity_k[i].lower()


def wybrana_lista():
    interupt_glowny = "coś czego nie ma"
    # nr_listy=str(input("podaj cos z listy: "))

    while interupt_glowny != "":
        try:
            print("podaj glowny")
            interupt_glowny = str(input().lower())
            lista_nowa = list((bol_g, wlosy_g, grypa_odpornosc_g, opryszczka_masc_g, opryszcza_odpornosc_g, nogi_g,
                               hemoroidy_masc_g, hemoroidy_czopki_g, furagina_zurawina_g, alergia_calcium_g,
                               alergia_inne_g, antybiotyk_g, biegunka_elektrolity_g))
            lista_nowa2 = list((bol_k, wlosy_k, grypa_odpornosc_k, opryszczka_masc_k, opryszcza_odpornosc_k, nogi_k,
                                hemoroidy_masc_k, hemoroidy_czopki_k, furagina_zurawina_k, alergia_calcium_k,
                                alergia_inne_k, antybiotyk_k, biegunka_elektrolity_k))
            i = 0
            l = 0

            if interupt_glowny != "":
                while l == 0:
                    szukaj = lista_nowa[i]
                    szukaj2 = lista_nowa2[i]
                    r = re.compile(".*" + interupt_glowny)

                    new = list(filter(r.match, szukaj))  # Read Note belo
                    l = len(new)
                    i = i + 1

                print("\n")
                # print(szukaj)
                newlist = list(filter(r.match, szukaj))  # Read Note below
                print(*newlist, sep='\n')
                print("\n")
                # root = Tk()
                # t = Text(root)
                # for x in newlist:
                #     t.insert(END, x + '\n')
                # t.pack()
                # root.mainloop()

                if newlist:
                    interupt = "coś czego nie ma"

                    while interupt != "":
                        print("podaj komplementarna")
                        interupt = input().lower()
                        r = re.compile(".*" + interupt)
                        if interupt != "":
                            print("\n")
                            newlist2 = list(filter(r.match, szukaj2))  # Read Note below
                            print(*newlist2, sep='\n')
                            print("\n")
                            if not newlist2:
                                print("Brak,podaj poprawną warotść")
        except:
            print("Brak, podaj podaj poprawną wartość")
    print("KONIEC")


# zmiana_liter()
# wybrana_lista()
