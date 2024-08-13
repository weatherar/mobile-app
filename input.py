import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

class InputScreen(Screen):
    def __init__(self, **kwargs):
        super(InputScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Masukkan data:')
        self.input = TextInput()
        self.submit_btn = Button(text='Submit', on_press=self.on_submit)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.submit_btn)
        self.add_widget(self.layout)

    def on_submit(self, instance):
        data = self.input.text
        self.manager.get_screen('Result').update_result(data)
        self.manager.current = 'Result'

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Hasil:')

        self.layout.add_widget(self.label)
        self.add_widget(self.layout)

    def update_result(self, data):
        self.label.text = f'Hasil: {data}'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InputScreen(name='Input'))
        sm.add_widget(ResultScreen(name='Result'))
        return sm

if __name__ == '__main__':
    MyApp().run()
