def input_data_mahasiswa():
    nama = input("Masukkan Nama Mahasiswa: ")
    nilai = float(input("Masukkan Nilai Mahasiswa: "))
    return nama, nilai

def ubah_nilai_mahasiswa(data_mahasiswa):
    if not data_mahasiswa:
        print("Belum ada data Mahasiswa. Silakan input data terlebih dahulu.")
        return

    nama = input("Masukkan Nama Mahasiswa yang ingin diubah nilainya: ")
    if nama in data_mahasiswa:
        nilai_baru = float(input("Masukkan Nilai Mahasiswa yang baru: "))
        data_mahasiswa[nama] = nilai_baru
        print(f"Nilai Mahasiswa {nama} telah diubah.")
    else:
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

if __name__ == "__main__":
    data_mahasiswa = {}

    while True:
        print("\nProgram Manajemen Nilai Mahasiswa")
        print("1. Input Nama dan Nilai Mahasiswa")
        print("2. Menampilkan Nama dan Nilai Mahasiswa")
        print("3. Mengubah Nilai Mahasiswa")
        print("4. Keluar Dari Program")

        pilihan = input("Masukkan pilihan (1-4): ")

        if pilihan == "1":
            nama, nilai = input_data_mahasiswa()
            data_mahasiswa[nama] = nilai
            print("Data Mahasiswa berhasil disimpan.")

        elif pilihan == "2":
            if not data_mahasiswa:
                print("Belum ada data Mahasiswa. Silakan input data terlebih dahulu.")
            else:
                print("\nDaftar Nama dan Nilai Mahasiswa:")
                for nama, nilai in data_mahasiswa.items():
                    print(f"Nama: {nama}, Nilai: {nilai}")

        elif pilihan == "3":
            ubah_nilai_mahasiswa(data_mahasiswa)

        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 hingga 4.")
