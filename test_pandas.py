# import
import re

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
path_excel = "/home/darek/git/komplementarna/glowna.xlsx"
path_excel_kom = "/home/darek/git/komplementarna/kom.xlsx"
df = pd.read_excel(path_excel)
df_kom = pd.read_excel(path_excel_kom)
df = pd.DataFrame(df)
df_kom = pd.DataFrame(df_kom)

global df2, df_kom2, df_kom_all


def glowna(szukaj):
    # while True:

        # szukaj =
    szukaj2 = szukaj.split()
    if szukaj == "":
        print("KONIEC")

    df2 = df
    for i in range(len(szukaj2)):

        # print (szukaj2[i])
        df2 = df2[df2["NAZWA"].str.contains(szukaj2[i], flags=re.IGNORECASE, regex=True)]
        if df2.empty:
            print("Nie ma takiego produktu")

    if df2.empty:
        print("")
    else:
        df4 = df2["NAZWA"].unique()
        df5 = pd.DataFrame(df4)
        print(df5.to_string(index=False, header=False))
        global kat_g
        kat_g = df2["KATEGORIA"].iloc[0]


def komplementarna(szukaj_kom):
    # while True:

    df_kom2 = df_kom


    szukaj_kom2 = szukaj_kom.split()
    if szukaj_kom == "":
        print ("")

    for i in range(len(szukaj_kom2)):

        df_kom2 = df_kom2[df_kom2["KATEGORIA"].str.contains(str(kat_g), flags=re.IGNORECASE, regex=True)]
        df_kom2 = df_kom2[df_kom2["NAZWA"].str.contains(szukaj_kom2[i], flags=re.IGNORECASE, regex=True)]
        if df_kom2.empty:
            print("nie ma takiego produktu")

    if df_kom2.empty:
        print("")
    else:
        df0 = df_kom2["NAZWA"].unique()
        df01 = pd.DataFrame(df0)
        print(df01.to_string(index=False, header=False))


def kategoria_all():
    print(kat_g)
    df_kom_all = (df_kom[df_kom["KATEGORIA"].str.contains(str(kat_g))])
    df_kom3 = df_kom_all["NAZWA"].unique()
    df_kom3 = pd.DataFrame(df_kom3)
    print(df_kom3.to_string(index=False, header=False))


glowna(str(input("podaj wartośc \n")))
# kategoria_all()
komplementarna(str(input("podaj komplemntarna \n")))
