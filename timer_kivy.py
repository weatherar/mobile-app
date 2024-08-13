from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class TimerApp(App):
    def build(self):
        self.time_left = 60  # waktu awal dalam detik
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.label = Label(text=str(self.time_left))
        self.layout.add_widget(self.label)

        self.start_button = Button(text='Start', on_press=self.start_timer)
        self.layout.add_widget(self.start_button)

        self.stop_button = Button(text='Stop', on_press=self.stop_timer)
        self.layout.add_widget(self.stop_button)

        return self.layout

    def start_timer(self, instance):
        Clock.schedule_interval(self.update_timer, 1)  # panggil fungsi update_timer setiap detik

    def stop_timer(self, instance):
        Clock.unschedule(self.update_timer)  # hentikan pemanggilan fungsi update_timer

    def update_timer(self, dt):
        self.time_left -= 1   #berkurang setiap 1 detik
        self.label.text = str(self.time_left)

        if self.time_left <= 0:
            self.label.text = 'Waktu Habis'
            Clock.unschedule(self.update_timer)  # hentikan pemanggilan fungsi update_timer

if __name__ == '__main__':
    TimerApp().run()
