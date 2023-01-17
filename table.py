import pandas as pd
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.datatables import MDDataTable
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp


path_excel = "glowna.xlsx"
path_excel_kom = "kom.xlsx"
df = pd.read_excel(path_excel)
df_kom = pd.read_excel(path_excel_kom)

df = pd.DataFrame(df)
df_kom = pd.DataFrame(df_kom)



def get_data_table(dataframe):
    column_data = list(dataframe.columns)
    row_data = dataframe.to_records(index=False)
    return column_data, row_data

def get_data_table2(dataframe):
    column_data = list(dataframe.columns)
    row_data = dataframe.to_records(index=False)
    return column_data, row_data



class MyApp(MDApp):
    def build(self):
        layout = GridLayout(

            cols= 2,
            rows=2
        )
        layout2 = BoxLayout(
            orientation='vertical'
        )

        layout3 = BoxLayout(
            orientation='vertical'
        )


        # container = my_root.ids.container
        # print(container)
        column_data, row_data = get_data_table(df)
        column_data = [(x, dp(100)) for x in column_data]

        column_data2, row_data2 = get_data_table(df_kom)
        column_data2 = [(x, dp(100)) for x in column_data2]

        g_label = Label(
            text='Szukaj głowne',
            color='000000',
            font_size= 34,
            # pos_hint={'right':1, 'top':1},
            )

        k_label = Label(
            text='Szukaj komplementarne',
            color='000000',
            font_size=34,
            # pos_hint={'left':1, 'top':1},
        )

        table = MDDataTable(
            # pos_hint = {'right':1,'bottom':1},
            size_hint = (0.9, 0.8),
            check = True,
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num = 100


        )

        table2 = MDDataTable(
            # pos_hint={'left':1, 'bottom':1},
            check=True,
            size_hint=(0.9, 0.8),

            column_data=column_data2,
            row_data=row_data2,
            use_pagination=True,
            rows_num=100
        )

        layout.add_widget(layout2)
        layout.add_widget(layout3)
        layout2.add_widget(g_label)
        layout2.add_widget(k_label)
        layout.add_widget(table)
        layout.add_widget(table2)

        return layout


MyApp().run()