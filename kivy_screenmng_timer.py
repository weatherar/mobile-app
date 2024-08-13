from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.timer_count = 0
        self.timer_label = Label(text='Timer: 0')
        #self.next_screen_button = Button(text='Next Screen') 
        #self.next_screen_button.bind(on_press=self.next_screen)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.timer_label)
        #layout.add_widget(self.next_screen_button)
        self.add_widget(layout)
        self.timer_event = None
        self.start_timer()

    def start_timer(self):
        self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        self.timer_count += 1
        self.timer_label.text = 'Timer: {}'.format(self.timer_count)
        if self.timer_count >= 15:
            self.next_screen()

    def next_screen(self, *args):
        self.manager.current = 'second'


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='This is the second screen'))
        self.add_widget(layout)


class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


if __name__ == '__main__':
    TestApp().run()
