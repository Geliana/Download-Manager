from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivymd.material_resources import dp

paused_bg = BoxLayout(orientation="vertical")

top = BoxLayout(size_hint=(1, .07), orientation="horizontal")

top.add_widget(
    Label(text="Paused Downloads", size_hint=(None, None), width=dp(200), height=dp(40), font_size=20, valign="bottom",
          font_name="Assets/Fonts/Roboto-Light.ttf", pos_hint={"x": 0, "y": 0}))

paused_all = Button(text="All Downloads", size_hint=(None, None), width=dp(150), height=dp(40),
                    pos_hint={"x": .5, "y": 0})
top.add_widget(paused_all)

paused_downloading = Button(text="Downloading", size_hint=(None, None), width=dp(150), height=dp(40),
                            pos_hint={"x": .5, "y": 0})
top.add_widget(paused_downloading)

paused_finished = Button(text="Finished Downloads", size_hint=(None, None), width=dp(150), height=dp(40),
                         pos_hint={"x": .5, "y": 0})
top.add_widget(paused_finished)

paused_error = Button(text="Error Downloads", size_hint=(None, None), width=dp(150), height=dp(40),
                      pos_hint={"x": .5, "y": 0})
top.add_widget(paused_error)

paused_label = Label(text="0", font_name="Assets/fonts/FiraCode-Bold.ttf", size_hint=(.1, 1), color=(1, 1, 1),
                     font_size=dp(15))
top.add_widget(paused_label)

bottom = BoxLayout(size_hint=(1, .93))

scroll = ScrollView()

paused_box = BoxLayout()

scroll.add_widget(paused_box)
bottom.add_widget(scroll)

paused_bg.add_widget(top)
paused_bg.add_widget(bottom)
