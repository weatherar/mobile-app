from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class TriangleApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10)

        self.label_alas = Label(text='Masukkan panjang alas:')
        self.input_alas = TextInput(multiline=False)   #multiline True bisa membuat pargaraf (bisa dienter)
        self.label_tinggi = Label(text='Masukkan tinggi segitiga:')
        self.input_tinggi = TextInput(multiline=False)

        self.layout.add_widget(self.label_alas)
        self.layout.add_widget(self.input_alas)
        self.layout.add_widget(self.label_tinggi)
        self.layout.add_widget(self.input_tinggi)

        self.calculate_button = Button(text='Hitung Luas Segitiga')
        self.calculate_button.bind(on_press=self.calculate_area)
        self.layout.add_widget(self.calculate_button)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        return self.layout

    def calculate_area(self, instance):
        try:
            alas = float(self.input_alas.text)
            tinggi = float(self.input_tinggi.text)
            luas = 0.5 * alas * tinggi
            self.result_label.text = f'Luas Segitiga: {luas}'
        except ValueError:
            self.result_label.text = 'Masukkan angka yang valid'


if __name__ == '__main__':
    TriangleApp().run()
