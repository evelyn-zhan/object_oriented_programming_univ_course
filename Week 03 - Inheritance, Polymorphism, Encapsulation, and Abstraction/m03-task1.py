import os
from abc import ABC, abstractmethod

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Kampus(ABC):
    def nomor_induk(self):
        pass

    def nama(self):
        pass

    @abstractmethod
    def absensi(self):
        pass

class Mikroskil:
    def __init__(self, nomor_induk, nama):
        self.nomor_induk = nomor_induk
        self.nama = nama

class Dosen(Mikroskil, Kampus):
    def __init__(self, nomor_induk, nama):
        super().__init__(nomor_induk, nama)
    
    def absensi(self):
        print(f"Selamat datang, {self.nama}. Silakan memulai pelajaran.")

class Mahasiswa(Mikroskil, Kampus):
    def __init__(self, nomor_induk, nama):
        super().__init__(nomor_induk, nama)
    
    def absensi(self):
        print(f"Terima kasih atas kehadiran Anda, {self.nama}.")

dosen = []
mahasiswa = []

def tambah_dosen():
    print(f"{"TAMBAH DATA DOSEN":^80}")
    print("=" * 80)
    nomor_induk = input("Masukkan nomor induk dosen: ")
    nama = input("Masukkan nama dosen: ").title()
    dosen.append(Dosen(nomor_induk, nama))
    print("=" * 80)
    print("Data dosen berhasil ditambahkan.")
    input("Tekan ENTER untuk kembali...")

def tambah_mahasiswa():
    print(f"{"TAMBAH DATA MAHASISWA":^80}")
    print("=" * 80)
    nomor_induk = input("Masukkan nomor induk mahasiswa: ")
    nama = input("Masukkan nama mahasiswa: ").title()
    mahasiswa.append(Mahasiswa(nomor_induk, nama))
    print("=" * 80)
    print("Data mahasiswa berhasil ditambahkan.")
    input("Tekan ENTER untuk kembali...")

def absensi_dosen():
    print(f"{"ABSENSI DOSEN":^80}")
    print("=" * 80)

    if len(dosen) == 0:
        print("Belum ada data dosen.")
    else:
        print(f"{"No":<5}{"NIP":<15}{"Nama"}")
        for i in range(len(dosen)):
            print(f"{i + 1:<5}{dosen[i].nomor_induk:<15}{dosen[i].nama}")
        print("=" * 80)

        nomor = int(input("Masukkan nomor dosen untuk melakukan absensi: "))

        while nomor < 1 or nomor > len(dosen):
            print("Tidak ada dosen dengan nomor tersebut.\n")
            nomor = int(input("Masukkan nomor dosen untuk melakukan absensi: "))

        print("=" * 80)
        dosen[nomor - 1].absensi()

    input("Tekan ENTER untuk kembali...")

def absensi_mahasiswa():
    print(f"{"ABSENSI MAHASISWA":^80}")
    print("=" * 80)

    if len(mahasiswa) == 0:
        print("Belum ada data mahasiswa.")
    else:
        print(f"{"No":<5}{"NIM":<15}{"Nama"}")
        for i in range(len(mahasiswa)):
            print(f"{i + 1:<5}{mahasiswa[i].nomor_induk:<15}{mahasiswa[i].nama}")
        print("=" * 80)

        nomor = int(input("Masukkan nomor mahasiswa untuk melakukan absensi: "))

        while nomor < 1 or nomor > len(mahasiswa):
            print("Tidak ada mahasiswa dengan nomor tersebut.\n")
            nomor = int(input("Masukkan nomor mahasiswa untuk melakukan absensi: "))

        print("=" * 80)
        mahasiswa[nomor - 1].absensi()

    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"ABSENSI KAMPUS":^80}")
    print("=" * 80)
    print("1. Tambah Data Dosen")
    print("2. Tambah Data Mahasiswa")
    print("3. Absensi Dosen")
    print("4. Absensi Mahasiswa")
    print("5. Keluar")
    print("=" * 80)
    pilihan = int(input("\nPilih menu [1/2/3/4/5]: "))

    if 1 <= pilihan <= 4:
        clear_screen()

    if pilihan == 1:
        tambah_dosen()
    elif pilihan == 2:
        tambah_mahasiswa()
    elif pilihan == 3:
        absensi_dosen()
    elif pilihan == 4:
        absensi_mahasiswa()
    elif pilihan == 5:
        print("\nTerima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")
