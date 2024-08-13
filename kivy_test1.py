
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
 
class ScrButton(Button):
   def __init__(self, screen, direction='right', goal='main', **kwargs):
       super().__init__(**kwargs)
       self.screen = screen
       self.direction = direction
       self.goal = goal
   def on_press(self):
       self.screen.manager.transition.direction = self.direction
       self.screen.manager.current = self.goal
      
class MainScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
       hl = BoxLayout()
       txt = Label(text= 'Choose a screen')
 
       vl.add_widget(ScrButton(self, direction='down', goal='first', text="1"))
       vl.add_widget(ScrButton(self, direction='left', goal='second', text="2"))
       vl.add_widget(ScrButton(self, direction='up', goal='third', text="3"))
       vl.add_widget(ScrButton(self, direction='right', goal='fourth', text="4"))
 
       hl.add_widget(txt)
       hl.add_widget(vl)
       self.add_widget(hl)
 
class FirstScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', size_hint=(.5, .5), pos_hint={'center_x': 0.5, 'center_y': 0.5})
       btn = Button(text= 'Choice: 1', size_hint=(.5, 1), pos_hint={'left': 0})
       btn_back = ScrButton(self, direction='up', goal='main', text="Back", size_hint=(.5, 1), pos_hint={'right': 1})
       vl.add_widget(btn)
       vl.add_widget(btn_back)
       self.add_widget(vl)
 
class SecondScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical')
 
       self.txt = Label(text= 'Choice: 2') 
       vl.add_widget(self.txt)

       hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
       lbl1 = Label(text='Enter your password:', halign='right')
       self.input = TextInput(multiline=False)

       hl_0.add_widget(lbl1)
       hl_0.add_widget(self.input)
       vl.add_widget(hl_0)
 
       
       hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
       btn_false = Button(text="OK!")
       btn_back = ScrButton(self, direction='right', goal='main', text="Back")

       hl.add_widget(btn_false)
       hl.add_widget(btn_back)
       vl.add_widget(hl)
       self.add_widget(vl)
       btn_false.on_press = self.change_text
 
   def change_text(self):
       self.txt.text = self.input.text + '? It did not work ...'       
 
 
class ThirdScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       layout = BoxLayout(orientation='vertical')
       btn_back = ScrButton(self, direction='down', goal='main', text="back", size_hint=(1, None), height='40sp')
       test_label = Label(text = "Your own screen")
       layout.add_widget(test_label)
       layout.add_widget(btn_back)
       self.add_widget(layout)

class FourthScr(Screen):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical', spacing=8)
       a = 'START ' + 'Выбор: 3 ' * 200
 
       test_label = Label(text = "Additional task",size_hint=(0.3,None))

       btn_back = ScrButton(self, direction='left', goal='main', text="Back", size_hint=(1, .2), pos_hint={'center-x': 0.5})
 
       self.label = Label(text=a, size_hint_y=None, font_size='24sp', halign='left', valign='top')  
       self.label.bind(size=self.resize)
       self.scroll = ScrollView(size_hint=(1, 1))
       self.scroll.add_widget(self.label)

       vl.add_widget(test_label)
       vl.add_widget(btn_back)
       vl.add_widget(self.scroll)
       self.add_widget(vl)
 
   def resize(self, *args):
       self.label.text_size = (self.label.width, None)
       self.label.texture_update()
       self.label.height = self.label.texture_size[1]

class MyApp(App):
   def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(FirstScr(name='first'))
       sm.add_widget(SecondScr(name='second'))
       sm.add_widget(ThirdScr(name='third'))
       sm.add_widget(FourthScr(name='fourth'))
 
       return sm
 
MyApp().run()

