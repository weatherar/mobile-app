try:
    # Potongan kode di sini yang mungkin menimbulkan pengecualian
    angka = int(input("Masukkan sebuah angka: "))
    hasil = 10 / angka
    print("Hasil pembagian adalah:", hasil)

except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol!")

except ValueError:
    print("Masukan yang Anda berikan bukan merupakan angka.")

except Exception as e:
    print("Terjadi kesalahan:", e)

finally:
    print("Program selesai.")