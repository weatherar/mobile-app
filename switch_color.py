from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class MultiColorApp(App):
    def build(self):
        # Membuat tata letak dan widget utama
        layout = BoxLayout(orientation='vertical')
        
        # Mengatur tata letak dan warna latar belakang untuk setiap layar
        screen1_layout = BoxLayout(orientation='vertical')
        screen1_button = Button(text='Screen 1', on_press=self.change_to_screen1)
        screen1_layout.add_widget(screen1_button)

        # Default clear color (misalnya untuk screen 1)
        self.set_clear_color((0.87, .54, .8, 1))
        layout.add_widget(screen1_layout)  # Menambahkan screen1_layout ke dalam layout

        return layout

    def change_to_screen1(self, instance):
        # Fungsi ini dipanggil ketika tombol untuk layar 1 ditekan
        self.set_clear_color((0.87, .54, .8, 1))

    def change_to_screen2(self, instance):
        # Fungsi ini dipanggil ketika tombol untuk layar 2 ditekan
        self.set_clear_color((0.4, 0.7, 0.2, 1))  # Contoh warna lain untuk layar 2

    def set_clear_color(self, color):
        # Fungsi ini mengatur warna latar belakang
        Window.clearcolor = color

if __name__ == '__main__':
    MultiColorApp().run()
