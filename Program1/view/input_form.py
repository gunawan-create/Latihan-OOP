def menu():
    print("\n=== Menu ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

def input_tambah():
    nama = input("Masukkan nama: ")
    nilai = float(input("Masukkan nilai: "))
    return nama, nilai

def input_hapus():
    nama = input("Masukkan nama yang ingin dihapus: ")
    return nama

def input_ubah():
    nama = input("Masukkan nama yang ingin diubah: ")
    nilai_baru = float(input("Masukkan nilai baru: "))
    return nama, nilai_baru
