class Mahasiswa:
    def __init__(self):  
        self.data = []

    def tambah(self, nama, nilai):
        self.data.append({'nama': nama, 'nilai': nilai})
        print(f"Data {nama} berhasil ditambahkan.")

    def tampilkan(self):
        print("\nDaftar Nilai Mahasiswa:")
        if not self.data:
            print("Tidak ada data.")
        else:
            for idx, mhs in enumerate(self.data, start=1):
                print(f"{idx}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

    def hapus(self, nama):
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data {nama} berhasil dihapus.")
                return
        print(f"Data {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                mhs['nilai'] = nilai_baru
                print(f"Data {nama} berhasil diubah.")
                return
        print(f"Data {nama} tidak ditemukan.")
