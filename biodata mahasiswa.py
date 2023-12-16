class Mahasiswa:
    total_mahasiswa = 0 

    def __init__(self, nama, nim, jurusan, angkatan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.angkatan = angkatan
        Mahasiswa.total_mahasiswa += 1  

    def tampilkan_biodata(self):
        print("Biodata Mahasiswa:")
        print("Nama: ", self.nama)
        print("NIM: ", self.nim)
        print("Jurusan: ", self.jurusan)
        print("Angkatan: ", self.angkatan)

    @classmethod
    def tampilkan_total_mahasiswa(cls):
        print(f"Total Mahasiswa: {cls.total_mahasiswa}")


def input_data_mahasiswa():
    nama = input("Masukkan Nama Mahasiswa: ")
    nim = input("Masukkan NIM Mahasiswa: ")
    jurusan = input("Masukkan Jurusan Mahasiswa: ")
    angkatan = input("Masukkan Angkatan Mahasiswa: ")

    mahasiswa_baru = Mahasiswa(nama, nim, jurusan, angkatan)
    return mahasiswa_baru

if __name__ == "__main__":
    mahasiswa = input_data_mahasiswa()
    mahasiswa.tampilkan_biodata()
    Mahasiswa.tampilkan_total_mahasiswa()
