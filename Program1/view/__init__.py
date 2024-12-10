from mahasiswa import Mahasiswa
from input_form import menu, input_tambah, input_hapus, input_ubah

def main():
    daftar_mahasiswa = Mahasiswa()

    while True:
        menu()
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nama, nilai = input_tambah()
            daftar_mahasiswa.tambah(nama, nilai)
        elif pilihan == '2':
            daftar_mahasiswa.tampilkan()
        elif pilihan == '3':
            nama = input_hapus()
            daftar_mahasiswa.hapus(nama)
        elif pilihan == '4':
            nama, nilai_baru = input_ubah()
            daftar_mahasiswa.ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
