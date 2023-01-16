from main_program import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window


from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp




import re
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
path_excel = "glowna.xlsx"
path_excel_kom = "kom.xlsx"
df = pd.read_excel(path_excel)
df_kom = pd.read_excel(path_excel_kom)
# path_csv = "glowna.csv"
# path_csv_kom = "kom.csv"
# df = pd.read_csv(path_csv)
# df_kom = pd.read_csv(path_csv_kom)
df = pd.DataFrame(df)
df_kom = pd.DataFrame(df_kom)

global df2, df_kom2, df_kom_all
global kat_g
Window.softinput_mode="below_target"


Builder.load_file('my.kv')


def wybrana_lista(szukaj):
    show = P()
    show2 = Z()

    szukaj2 = szukaj.split()
    if szukaj == "":
        print("KONIEC")
        # Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True, content=show2).open()
        theapp.screenm.current = 'first'
    global df2
    df2 = df
    for i in range(len(szukaj2)):

        df2 = df2[df2["NAZWA"].str.contains(szukaj2[i], flags=re.IGNORECASE, regex=True)]
        if df2.empty:
            # print("Nie ma takiego produktu glowna")
            Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True, content=show).open()
            theapp.screenm.current = 'first'

    if df2.empty:
        print("")
    else:
        df4 = df2["NAZWA"].unique()
        df5 = pd.DataFrame(df4)
        df6 = df2["KATEGORIA"].unique()
        df7 = pd.DataFrame(df6)
        print(len(df7))
        print(df7)
        if len(df7) <= 2:
            theapp.secscreen.ids.lb_wynik_glowny.text = (df5.to_string(index=False, header=False))
            global kat_g
            kat_g = [df2["KATEGORIA"].iloc[0], df2["KATEGORIA"].iloc[1]]
            theapp.screenm.current = 'second'
        else:
            Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True, content=show2).open()




def wynik_komplemanatrny(szukaj_kom):
    show = P()
    df_kom2 = df_kom
    szukaj_kom2 = szukaj_kom.split()

    for i in range(len(szukaj_kom2)):

        df_kom2 = df_kom2[df_kom2["KATEGORIA"].str.contains(str(kat_g), flags=re.IGNORECASE, regex=True)]
        df_kom2 = df_kom2[df_kom2["NAZWA"].str.contains(szukaj_kom2[i], flags=re.IGNORECASE, regex=True)]


    if df_kom2.empty:
        theapp.secscreen.ids.ti_komplementarna.text = ""
        Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True,
              content=show).open()
    else:
        df0 = df_kom2["NAZWA"].unique()
        df01 = pd.DataFrame(df0)
        theapp.secscreen.ids.lb_komplementarna.text = df01.to_string(index=False, header=False)



def wynik_komplemanatrny_all():
    df_kom2 = df_kom
    df_kom2 = df_kom2[df_kom2["KATEGORIA"].str.contains(str(kat_g), flags=re.IGNORECASE, regex=True)]
    df0 = df_kom2["NAZWA"].unique()
    df01 = pd.DataFrame(df0)
    theapp.secscreen.ids.lb_komplementarna.text = df01.to_string(index=False, header=False)



class P(FloatLayout):
    pass
class Z(FloatLayout):
    pass


class fscreen(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def change(self):
        show=P()
        show2=Z()
        if theapp.fscreen.ids.in_first.text == "":
            Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True,
                  content=show).open()
        else:
            wybrana_lista(theapp.fscreen.ids.in_first.text)
            # wynik_komplemanatrny_all()
        # theapp.fscreen.ids.in_first.text = ""


    # on_release: root.secscreen.ids.ti_komplementarna.focus = True

    

    def exit(self):
        theapp.stop()


class secscreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change(self):
        theapp.screenm.current = 'first'
        theapp.secscreen.ids.lb_wynik_glowny.text = ""
        theapp.secscreen.ids.lb_komplementarna.text = ""
        theapp.fscreen.ids.in_first.text = ""


    def focus(self):
        theapp.fscreen.ids.in_first.focus = True



    def change_color(self):
        # theapp.stop()
        show=P()

        if theapp.secscreen.ids.ti_komplementarna.text == "":
            Popup(size_hint=(None, None), size=(400, 400), title="BŁĄD", auto_dismiss=True,
                  content=show).open()
        else:
            wynik_komplemanatrny(theapp.secscreen.ids.ti_komplementarna.text)
        theapp.secscreen.ids.ti_komplementarna.text = ""



    def exit(self):
        theapp.stop()

class theapp(App):
    def build(self):
        self.screenm = ScreenManager()
        self.fscreen = fscreen()
        screen = Screen(name="first")
        screen.add_widget(self.fscreen)
        self.screenm.add_widget(screen)

        self.secscreen = secscreen()
        screen = Screen(name="second")
        screen.add_widget(self.secscreen)
        self.screenm.add_widget(screen)

        return self.screenm
    


if __name__ == "__main__":
    theapp = theapp()
    theapp.run()
