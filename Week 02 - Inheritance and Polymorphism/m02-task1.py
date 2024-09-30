import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Evelyn:
    def __init__(self, nomor_induk, nama, jenis_kelamin, nomor_hp):
        self.nomor_induk = nomor_induk
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.nomor_hp = nomor_hp

class Mahasiswa(Evelyn):
    def __init__(self, nomor_induk, nama, jenis_kelamin, nomor_hp):
        super().__init__(nomor_induk, nama, jenis_kelamin, nomor_hp)

    def absensi(self):
        print(f"{self.nomor_induk:<15}{self.nama}")

class Dosen(Evelyn):
    def __init__(self, nomor_induk, nama, jenis_kelamin, nomor_hp):
        super().__init__(nomor_induk, nama, jenis_kelamin, nomor_hp)
    
    def perkenalan(self):
        print(f"{self.nama:<20}{self.nomor_hp}")

mahasiswa = []
dosen = []

def tambah_mahasiswa():
    print(f"{"TAMBAH DATA MAHASISWA":^100}")
    print("=" * 100)
    
    nim = input(f"{"NIM":<25}: ")

    nama = input(f"{"Nama":<25}: ").title()

    jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()

    while jenis_kelamin != "l" and jenis_kelamin != "p":
        print("Jenis kelamin harus berupa L atau P.")
        jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()
    
    jenis_kelamin = "Laki-Laki" if jenis_kelamin == "l" else "Perempuan"

    nomor_hp = input(f"{"Nomor HP":<25}: ")

    mahasiswa.append(Mahasiswa(nim, nama, jenis_kelamin, nomor_hp))

    print("=" * 100)
    print("Data mahasiswa berhasil ditambahkan.")
    input("Tekan ENTER untuk kembali...")

def tambah_dosen():
    print(f"{"TAMBAH DATA DOSEN":^100}")
    print("=" * 100)

    nip = input(f"{"NIP":<25}: ")

    nama = input(f"{"Nama":<25}: ").title()

    jenis_kelamin = input(f"{"Jenis kelamin [L/P]":<25}: ").lower()

    while jenis_kelamin != "l" and jenis_kelamin != "p":
        print("Jenis kelamin harus berupa L atau P.")
    
    jenis_kelamin = "Laki-Laki" if jenis_kelamin == "l" else "Perempuan"

    nomor_hp = input(f"{"Nomor HP":<25}: ")

    dosen.append(Dosen(nip, nama, jenis_kelamin, nomor_hp))

    print("=" * 100)
    print("Data dosen berhasil ditambahkan.")
    input("Tekan ENTER untuk kembali...")

def absensi_mahasiswa():
    print(f"{"ABSENSI MAHASISWA":^100}")
    print("=" * 100)

    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print(f"{"No":<5}{"NIM":<15}{"Nama"}")
        for i in range(len(mahasiswa)):
            print(f"{i + 1:<5}", end = "")
            mahasiswa[i].absensi()

    print("=" * 100)
    input("Tekan ENTER untuk kembali...")

def perkenalan_dosen():
    print(f"{"PERKENALAN DOSEN":^100}")
    print("=" * 100)

    if len(dosen) == 0:
        print("Belum ada data dosen.")
    else:
        print(f"{"No":<5}{"Nama":<20}{"Nomor HP"}")
        for i in range(len(dosen)):
            print(f"{i + 1:<5}", end = "")
            dosen[i].perkenalan()

    print("=" * 100)
    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"MENU":^100}")
    print("=" * 100)
    print("1. Tambah Data Mahasiswa")
    print("2. Tambah Data Dosen")
    print("3. Absensi Mahasiswa")
    print("4. Perkenalan Dosen")
    print("5. Keluar")
    print("=" * 100)

    pilihan = int(input("Pilih menu [1/2/3/4/5] : "))

    if 1 <= pilihan <= 4:
        clear_screen()
    
    if pilihan == 1:
        tambah_mahasiswa()
    elif pilihan == 2:
        tambah_dosen()
    elif pilihan == 3:
        absensi_mahasiswa()
    elif pilihan == 4:
        perkenalan_dosen()
    elif pilihan == 5:
        print("\nTerima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")