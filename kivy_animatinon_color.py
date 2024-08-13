from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.animation import Animation


class SlideButton(Button):
    def __init__(self, **kwargs):
        super(SlideButton, self).__init__(**kwargs)
        self.slide_animation()

    def slide_animation(self):
        #anim = Animation(x=800, duration=2) + Animation(x=0, duration=2)
        anim = Animation(y=800, duration=2) + Animation(y=0, duration=2)
        anim.repeat = True
        anim.start(self)


class SlideButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Background color
        with layout.canvas.before:
            Color(0, 0, 0.5, 1)  # Pink color
            self.rect = Rectangle(size=(layout.width, layout.height), pos=layout.pos)

        button = SlideButton(text="Slide Me", size_hint=(None, None), size=(200, 50))
        btn_color = (0.98, 0.31, 0.8, 1)
        button.background_color = btn_color
        layout.add_widget(button)
        return layout

    def on_start(self):
        self.rect.size = self.root.size
        self.rect.pos = self.root.pos


if __name__ == "__main__":
    SlideButtonApp().run()

"""
menambahkan bagian dengan with layout.canvas.before: sebelum menambahkan tombol ke dalam layout. 
Di dalam blok ini, kita menggunakan Color untuk mengatur warna latar belakang menjadi pink,
kemudian kita membuat objek Rectangle yang mengisi seluruh area layout.
"""