from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.popup import Popup #menu/library untuk memunculkan pop up
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Show Popup', size_hint=(None, None), size=(200, 50))
        btn_color = (0.98, 0.31, 0.8, 1)
        button.background_color = btn_color
        button.bind(on_press=self.show_popup)
        layout.add_widget(button)
        return layout

    def show_popup(self, instance):
        popup_layout = BoxLayout(orientation='vertical')
        content_label = Label(text="This is a popup!")
        close_button = Button(text="Close the popup")
        popup_layout.add_widget(content_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title='Popup Window', content=popup_layout, size_hint=(None, None), size=(300, 200))
        close_button.bind(on_press=popup.dismiss)

        popup.open()


if __name__ == '__main__':
    MyApp().run()
