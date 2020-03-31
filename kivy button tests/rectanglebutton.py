from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

#from kivy.graphics import Rectangle


class mybutton(Button):
    def __init__(self, btn_text, **kwargs):
        super().__init__(**kwargs)
        self.text = btn_text
        self.background_normal = ''
        self.background_color = (1,0.4,.1,1)

class wdgt(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=2
        btn_play = mybutton("Play")
        btn_next = mybutton("|>")
        btn_prev = mybutton("<|")
        btn_vinyl = mybutton("Plattenspieler")
        btn_cd = mybutton("CD")
        btn_blue = mybutton("Bluetooth")
        btn_stream = mybutton("Stream")
        btn_aux = mybutton("AUX")
        btn_usb = mybutton("USB")
        btn_color = mybutton("COLOR")
        btn_list=[btn_play,btn_next,btn_prev,btn_vinyl,btn_cd,btn_blue,btn_stream,btn_aux,btn_usb,btn_color]
        for element in btn_list:
            self.add_widget(element)


class MainApp(App):
    def build(self):
        return wdgt()

if __name__ == '__main__':
    MainApp().run()