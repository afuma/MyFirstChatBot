
from kivy.core.text import LabelBase
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.core.window import Window
from kivy.clock import Clock
Window.size = (350, 600)

kv = '''
<CircularProgressBar>
    canvas.before:
        Color:
            rgba: root.bar_color + [0.3]
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)
    canvas.after:
        Color:
            rgb: root.bar_color
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_value*3.6)
    MDLabel:
        text: root.text
        # font_name: "BPoppins"
        font_size: "40sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        halign: "center"
        color: root.bar_color
MDFloatLayout:
    md_bg_color: 1, 0, 100/255, .1
    CircularProgressBar:
        size_hint: None, None
        size: 200, 200
        pos_hint: {"center_x": .5, "center_y": .5}
        value: 80

'''

class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    value = NumericProperty(0)
    bar_color = ListProperty([1, 0, 100/255])
    bar_width = NumericProperty(20)
    text = StringProperty("0%")
    duration = NumericProperty(1.5)
    counter = 0

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)

    def animate(self, *args):
        Clock.schedule_interval(self.percent_counter, self.duration/self.value)

    def percent_counter(self, *args):
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)

class ProgressBar(MDApp):

    def build(self):
        return Builder.load_string(kv)

if __name__ == '__main__':
    # LabelBase.register(name="Poppins", fn_regular="polices/Poppins-Regular.ttf")
    ProgressBar().run()