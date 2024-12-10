from mahasiswa import Mahasiswa

if __name__ == "__main__":
    daftar_mahasiswa = Mahasiswa()

    while True:
        print("\n=== Menu ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            nama = input("Masukkan nama: ")
            nilai = float(input("Masukkan nilai: "))
            daftar_mahasiswa.tambah(nama, nilai)
        elif pilihan == '2':
            daftar_mahasiswa.tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama yang ingin dihapus: ")
            daftar_mahasiswa.hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama yang ingin diubah: ")
            nilai_baru = float(input("Masukkan nilai baru: "))
            daftar_mahasiswa.ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
