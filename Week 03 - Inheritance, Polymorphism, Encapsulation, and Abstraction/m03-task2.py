import os
from abc import ABC, abstractproperty, abstractmethod

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Les(ABC):
    # @abstractproperty
    def nama(self):
        pass

    # @abstractproperty
    def nomor_hp_orang_tua(self):
        pass

    @abstractmethod
    def cetak(self):
        pass

class Murid:
    def __init__(self, tingkat, biaya):
        self.tingkat = tingkat
        self.biaya = biaya

class SD(Murid, Les):
    def __init__(self, nama, nomor_hp_orang_tua, tingkat, biaya, jenis_kelamin):
        super().__init__(tingkat, biaya)
        self.nama = nama
        self.nomor_hp_orang_tua = nomor_hp_orang_tua
        self.jenis_kelamin = jenis_kelamin

    def cetak(self):
        print(f"{"DATA MURID":^50}")
        print("=" * 50)
        print(f"Nama: {self.nama}")
        print(f"Nomor HP Orang Tua: {self.nomor_hp_orang_tua}")
        print(f"Jenis Kelamin: {self.jenis_kelamin}")
        print(f"Tingkat: {self.tingkat}")
        print(f"Biaya Les: {self.biaya}")
        print("=" * 50)
    
class SMP(Murid, Les):
    def __init__(self, nama, nomor_hp_orang_tua, tingkat, biaya, umur):
        super().__init__(tingkat, biaya)
        self.nama = nama
        self.nomor_hp_orang_tua = nomor_hp_orang_tua
        self.umur = umur

    def cetak(self):
        print(f"{"DATA MURID":^50}")
        print("=" * 50)
        print(f"Nama: {self.nama}")
        print(f"Nomor HP Orang Tua: {self.nomor_hp_orang_tua}")
        print(f"Umur: {self.umur}")
        print(f"Tingkat: {self.tingkat}")
        print(f"Biaya Les: {self.biaya}")
        print("=" * 50)

class SMA(Murid, Les):
    def __init__(self, nama, nomor_hp_orang_tua, tingkat, biaya, jurusan):
        super().__init__(tingkat, biaya)
        self.nama = nama
        self.nomor_hp_orang_tua = nomor_hp_orang_tua
        self.jurusan = jurusan

    def cetak(self):
        print(f"{"DATA MURID":^50}")
        print("=" * 50)
        print(f"Nama: {self.nama}")
        print(f"Nomor HP Orang Tua: {self.nomor_hp_orang_tua}")
        print(f"Jurusan: {self.jurusan}")
        print(f"Tingkat: {self.tingkat}")
        print(f"Biaya Les: {self.biaya}")
        print("=" * 50)

murid = []

def tambah_murid():
    print(f"{"TAMBAH MURID":^50}")
    print("=" * 50)
    
    nama = input("Nama: ").title()
    nomor_hp_orang_tua = input("Nomor HP Orang Tua: ")

    tingkat = input("Tingkatan [SD/SMP/SMA]: ").upper()

    while tingkat != "SD" and tingkat != "SMP" and tingkat != "SMA":
        print("Tingkatan harus berupa SD, SMP, atau SMA.")
        tingkat = input("Tingkatan [SD/SMP/SMA]: ").upper()

    if tingkat == "SD":
        biaya = 500000
        jenis_kelamin = input("Jenis Kelamin [L/P]: ").upper()
        while jenis_kelamin != "L" and jenis_kelamin != "P":
            print("Jenis kelamin harus berupa L (Laki-laki) atau P (Perempuan).")
            jenis_kelamin = input("Jenis Kelamin [L/P]: ").upper()
        murid.append(SD(nama, nomor_hp_orang_tua, tingkat, biaya, jenis_kelamin))
    elif tingkat == "SMP":
        biaya = 1000000
        umur = int(input("Umur: "))
        murid.append(SMP(nama, nomor_hp_orang_tua, tingkat, biaya, umur))
    elif tingkat == "SMA":
        biaya = 1500000
        jurusan = input("Jurusan [IPA/IPS]: ").upper()
        while jurusan != "IPA" and jurusan != "IPS":
            print("Jurusan harus berupa IPA atau IPS.")
            jurusan = input("Jurusan [IPA/IPS]: ").upper()
        murid.append(SMA(nama, nomor_hp_orang_tua, tingkat, biaya, jurusan))
    
    print("=" * 50)
    print("Data murid berhasil ditambahkan.")
    input("Tekan ENTER untuk kembali...")

def cetak_data():
    print(f"{"DATA MURID":^50}")
    print("=" * 50)
    
    if len(murid) == 0:
        print("Belum ada data murid.")
    else:
        print(f"{"No":<5}{"Nama":<25}{"Tingkatan"}")
        for i in range(len(murid)):
            print(f"{i + 1:<5}{murid[i].nama:<25}{murid[i].tingkat}")
        
        print("=" * 50)
        nomor = int(input("Masukkan nomor murid untuk melihat data: "))

        while nomor < 1 or nomor > len(murid):
            print("Tidak ada murid dengan nomor tersebut.\n")
            nomor = int(input("Masukkan nomor murid untuk melihat data: "))
            
        print("=" * 50 + "\n")
        murid[nomor - 1].cetak()
            
    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"MENU":^50}")
    print("=" * 50)
    print("1. Tambah Murid")
    print("2. Cetak Data Murid")
    print("3. Keluar")
    print("=" * 50)
    pilihan = int(input("Pilih menu [1/2/3]: "))

    if 1 <= pilihan <= 2:
        clear_screen()

    if pilihan == 1:
        tambah_murid()
    elif pilihan == 2:
        cetak_data()
    elif pilihan == 3:
        print("\nTerima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")