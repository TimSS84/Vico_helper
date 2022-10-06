from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Vico_HelperApp(MDApp):
    def build(self):
        return MDLabel(text="Привет, кожаный!", halign="center")


Vico_HelperApp().run()