from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class  MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        v = BoxLayout(orientation ='vertical', padding = 8, spacing=8)
        h = BoxLayout(padding = 8, spacing = 8)
        h.add_widget(Label(text = "Выбери экран"))
        v.add_widget(Button(text = 'Экран 1'))
        v.add_widget(Button(text = 'Экран 2'))
        v.add_widget(Button(text = 'Экран 3'))
        v.add_widget(Button(text = 'Экран 4'))
        h.add_widget(v)

class  Scr1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

        
        
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr())

window = MyApp()
window.run()
