import tkinter as tk

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi Pilihan")
top.geometry("500x600")
top.configure(bg="pink")

judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan:", bg="pink", fg="navy", font=("Arial", 11))
judul.pack(pady=10)

# input nilai mapel 1-10
for i in range(1, 11):
    L1 = tk.Label(top, text="Nilai Mata Pelajaran " + str(i), bg="pink", fg="purple")
    L1.pack()
    E1 = tk.Entry(top, bd=2)
    E1.pack()

def tampilkan_hasil():
    Label_hasil = tk.Label(top, text="Prodi: Teknologi Informasi", fg="darkblue")
    Label_hasil.pack(pady=10)
    

tombol = tk.Button(top, text="Hasil Prediksi", fg="navy", command=tampilkan_hasil)
tombol.pack(pady=15)

Label_hasil = tk.Label(top, text="Prodi: Tekologi Informasi", bg="pink", fg="purple")
Label_hasil.pack(pady=10)

top.mainloop()
