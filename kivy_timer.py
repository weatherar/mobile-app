from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

class TimerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.label = Label(text="0")
        self.layout.add_widget(self.label)
        
        # Panggil method untuk memulai timer saat aplikasi dimulai
        Clock.schedule_interval(self.update_timer, 1)  # Timer akan diupdate setiap 1 detik
        
        return self.layout
    
    def update_timer(self, dt):
        # Method ini akan dipanggil setiap interval waktu yang ditentukan oleh Clock.schedule_interval()
        # Di sini, Anda bisa menambahkan logika untuk memperbarui timer
        self.label.text = str(int(self.label.text) + 1)  # Timer akan bertambah setiap detik

if __name__ == '__main__':
    TimerApp().run()


"""
- TimerApp adalah subclass dari App yang merupakan titik masuk utama aplikasi Kivy.
- Metode build() digunakan untuk membangun antarmuka pengguna. Di sini, kita membuat BoxLayout dan menambahkan Label untuk menampilkan nilai timer.
- Metode update_timer(dt) akan dipanggil setiap interval waktu yang ditentukan oleh Clock.schedule_interval(). Di dalam metode ini, nilai timer akan diperbarui.
- Saat aplikasi dimulai (build() dipanggil), kita menggunakan Clock.schedule_interval() untuk memanggil update_timer setiap 1 detik.
- if __name__ == '__main__': memastikan bahwa aplikasi dijalankan hanya jika file dieksekusi secara langsung, bukan diimpor sebagai modul."""