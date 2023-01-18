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
from kivy.uix.button import Button



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
        layout = BoxLayout(
            orientation="vertical"
        )

        anchor_layout_top = AnchorLayout(
            size_hint=(1, 0.2),
            anchor_x="center",
            anchor_y="top",
        )
        anchor_layout_bottom = AnchorLayout(

            size_hint=(1, 0.5),
            anchor_x = "center",
            anchor_y = "bottom",
        )
        grid_layout_bottom = GridLayout(

            cols= 2,
            rows=2
        )
        grid_layout_top = GridLayout(

            cols=2,
            # rows=2
        )
        box_layout_l = BoxLayout(
            orientation='vertical',
            padding= [50, 50, 50, 50],

        )
        box_layout_p = BoxLayout(
            orientation='vertical',
            padding= [50, 50, 50, 50],
        )



        column_data, row_data = get_data_table(df)
        column_data = [(x, dp(100)) for x in column_data]

        column_data2, row_data2 = get_data_table(df_kom)
        column_data2 = [(x, dp(100)) for x in column_data2]

        g_label = Label(
            text='Szukaj głowne',
            color='000000',
            font_size= 34,

            )

        k_label = Label(
            text='Szukaj komplementarne',
            color='000000',
            font_size=34,


        )

        table = MDDataTable(
            # pos_hint = {'right':1,'bottom':1},
            size = (0.9, 0.8),
            check = True,
            column_data=column_data,
            row_data=row_data,
            use_pagination=True,
            rows_num = 100


        )

        table2 = MDDataTable(
            # pos_hint={'left':1, 'bottom':1},
            check=True,
            size=(0.9, 0.8),

            column_data=column_data2,
            row_data=row_data2,
            use_pagination=True,
            rows_num=100
        )


        input_glowny=TextInput(
            multiline=False,
            size_hint = (1, 0.3),

        )
        input_komplementerny=TextInput(
            multiline=False,
            size_hint = (1, 0.3),

        )


        button_szukaj=Button(
            text="SZUKAJ"
        )
        button_sprawdz=Button(
            text="SPRAWDŹ"
        )



        layout.add_widget(anchor_layout_top)
        layout.add_widget(anchor_layout_bottom)
        anchor_layout_bottom.add_widget(grid_layout_bottom)
        anchor_layout_top.add_widget(grid_layout_top)
        grid_layout_top.add_widget(box_layout_l)
        grid_layout_top.add_widget(box_layout_p)
        box_layout_l.add_widget(button_szukaj)
        box_layout_l.add_widget(g_label)
        box_layout_l.add_widget(input_glowny)
        box_layout_p.add_widget(button_sprawdz)
        box_layout_p.add_widget(k_label)
        box_layout_p.add_widget(input_komplementerny)
        grid_layout_bottom.add_widget(table)
        grid_layout_bottom.add_widget(table2)

        return layout



MyApp().run()