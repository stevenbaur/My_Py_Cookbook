from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.filechooser import FileChooserListView

from kivy.uix.button import Button
from functools import partial

class mygrid(GridLayout):
    def __init__(self, **kwargs):
        super(mygrid,self).__init__(**kwargs)
        self.cols=2

        #-----FileChooser on the right side
        right = FileChooserListView()
        right.rootpath="/home/stevenbaur/Musik"
        right.filters=['*.wav','*.mp3']

        #-----Test-Arrea on the left side

        left = Button()
        left.text="test"
        left.bind(on_release=partial(self.load_from_filechooser, right))

        self.add_widget(left)
        self.add_widget(right)

    def load_from_filechooser(self, filechooser, *args):
        self.load(self, filechooser.path, filechooser.selection)

    def load(self, path, selection, something):
        print(selection) #path
        print(something) #selected_file


class MainApp(App):
    def build(self):
        return mygrid()

if __name__ == '__main__':
    MainApp().run()