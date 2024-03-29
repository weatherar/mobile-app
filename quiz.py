
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
 
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
       txt = Label(text= 'Pilih Level Quiz')
 
       vl.add_widget(ScrButton(self, direction='down', goal='first', text="Level 1"))
       vl.add_widget(ScrButton(self, direction='left', goal='second', text="Level 2"))
       vl.add_widget(ScrButton(self, direction='up', goal='third', text="score"))
 
       hl.add_widget(txt)
       hl.add_widget(vl)
       self.add_widget(hl)
 
class FirstScr(Screen):
     def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical')
       hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
       
       self.txt = Label(text= '1. Apakah python bersaudara dengan c ++ ?') 
       vl.add_widget(self.txt)

       hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
       btn_false = Button(text="Yes")
       btn_true = Button(text="No")
       btn_back = ScrButton(self, direction='right', goal='main', text="Back")

       hl.add_widget(btn_false)
       hl.add_widget(btn_true)
       hl.add_widget(btn_back)
       
       vl.add_widget(hl)
       self.add_widget(vl)
       btn_false.on_press = self.change_text
 
     def change_text(self):
        self.txt.text = self.input.text + '? It did not work ...' 

                
class SecondScr(Screen):
     def __init__(self, **kwargs):
       super().__init__(**kwargs)
 
       vl = BoxLayout(orientation='vertical')
       hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
       
       self.txt = Label(text= '2. Apakah python ezz ?') 
       vl.add_widget(self.txt)

       hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
       btn_false = Button(text="Yes")
       btn_true = Button(text="No")
       btn_back = ScrButton(self, direction='right', goal='main', text="Back")

       hl.add_widget(btn_false)
       hl.add_widget(btn_true)
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
       test_label = Label(text = "Total score anda : ")
       layout.add_widget(test_label)
       layout.add_widget(btn_back)
       self.add_widget(layout)

class MyApp(App):
   def build(self):
       sm = ScreenManager()
       sm.add_widget(MainScr(name='main'))
       sm.add_widget(FirstScr(name='first'))
       sm.add_widget(SecondScr(name='second'))
       sm.add_widget(ThirdScr(name='third'))
 
       return sm
 
MyApp().run()

