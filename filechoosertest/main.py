from kivy.app import App
from kivy.uix.widget import Widget

class wdgt(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        pass

class MainApp(App):
    def build(self):
        return wdgt()

if __name__ == '__main__':
    MainApp().run()