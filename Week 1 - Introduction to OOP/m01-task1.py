import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Mahasiswa:
    def __init__(self, nim, nama, jenis_kelamin, jurusan, email):
        self.nim = nim
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.jurusan = jurusan
        self.email = email

class Dosen:
    def __init__(self, nip, nama, jenis_kelamin, jabatan, no_hp):
        self.nip = nip
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.jabatan = jabatan
        self.no_hp = no_hp


daftar_mahasiswa = []
daftar_dosen = []


def tambah_mahasiswa():
    print(f"{"TAMBAH DATA MAHASISWA":^120}")
    print("=" * 120)

    nim = input(f"{"NIM":<25}: ")

    nama = input(f"{"Nama":<25}: ").title()

    jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()

    while jenis_kelamin != "l" and jenis_kelamin != "p":
        print("Jenis kelamin harus berupa L atau P.")
        jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()
    
    jenis_kelamin = "Laki-Laki" if jenis_kelamin == "l" else "Perempuan"

    jurusan = input(f"{"Jurusan [IF/SI/TI/AK/MN]":<25}: ").lower()

    while jurusan != "if" and jurusan != "si" and jurusan != "ti" and jurusan != "ak" and jurusan != "mn":
        print("Jurusan harus berupa IF, SI, TI, AK, atau MN.")
        jurusan = input(f"{"Jurusan [IF/SI/TI/AK/MN]":<25}: ").lower()
    
    if jurusan == "if":
        jurusan = "Teknik Informatika"
    elif jurusan == "si":
        jurusan = "Sistem Informasi"
    elif jurusan == "ti":
        jurusan = "Teknologi Informasi"
    elif jurusan == "ak":
        jurusan = "Akuntansi"
    elif jurusan == "mn":
        jurusan = "Manajemen"

    email = input(f"{"E-mail":<25}: ")

    mahasiswa = Mahasiswa(nim, nama, jenis_kelamin, jurusan, email)
    daftar_mahasiswa.append(mahasiswa)


def tambah_dosen():
    print(f"{"TAMBAH DATA DOSEN":^120}")
    print("=" * 120)

    nip = input(f"{"NIP":<25}: ")

    nama = input(f"{"Nama":<25}: ").title()

    jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()

    while jenis_kelamin != "l" and jenis_kelamin != "p":
        print("Jenis kelamin harus berupa L atau P.")
        jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()
    
    jenis_kelamin = "Laki-Laki" if jenis_kelamin == "l" else "Perempuan"

    jabatan = input(f"{"Jabatan":<25}: ").title()

    no_hp = input(f"{"No. HP":<25}: ")

    dosen = Dosen(nip, nama, jenis_kelamin, jabatan, no_hp)
    daftar_dosen.append(dosen)


def cetak_absensi():
    print(f"{"REKAP ABSENI":^120}")
    print("=" * 120)

    print("\nDaftar Mahasiswa")
    print("=" * 120)
    if len(daftar_mahasiswa) == 0:
        print("Tidak ada mahasiswa yang hadir.")
    else:
        count = 0
        for mahasiswa in daftar_mahasiswa:
            count += 1
            print(f"{count:<4}{mahasiswa.nim:<12}{mahasiswa.nama:<25}{mahasiswa.jenis_kelamin:<15}{mahasiswa.jurusan:<22}{mahasiswa.email}")
        print("=" * 120)
        print(f"Jumlah mahasiswa yang hadir: {count} orang")

    print("\nDaftar Dosen")
    print("=" * 120)
    if len(daftar_dosen) == 0:
        print("Tidak ada dosen yang hadir.")
    else:
        count = 0
        for dosen in daftar_dosen:
            count += 1
            print(f"{count:<4}{dosen.nip:<12}{dosen.nama:<25}{dosen.jenis_kelamin:<15}{dosen.jabatan:<22}{dosen.no_hp}")
        print("=" * 120)
        print(f"Jumlah dosen yang hadir: {count} orang")

    print()
    print("=" * 120)
    print(f"Total: {len(daftar_mahasiswa) + len(daftar_dosen)} orang")

    input("\nTekan ENTER untuk kembali...")


while True:
    clear_screen()

    print(f"{"REKAP ABSENI":^120}")
    print("=" * 120)
    print("1. Tambah Data Mahasiswa")
    print("2. Tambah Data Dosen")
    print("3. Cetak Rekap Absensi")
    print("4. Keluar")

    pilihan = int(input("\nPilih menu [1/2/3/4]: "))

    if 1 <= pilihan <= 3:
        clear_screen()

    if pilihan == 1:
        tambah_mahasiswa()
    elif pilihan == 2:
        tambah_dosen()
    elif pilihan == 3:
        cetak_absensi()
    elif pilihan == 4:
        print("Terima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")