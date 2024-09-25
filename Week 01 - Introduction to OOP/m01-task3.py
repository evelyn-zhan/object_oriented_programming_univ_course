import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class KartuMurid:
    def __init__(self, nama, tingkatan):
        self.nama = nama
        self.tingkatan = tingkatan
        if tingkatan == "tk":
            self.jam_pengajaran = 2
            self.biaya_les = 300000
        elif tingkatan == "sd":
            self.jam_pengajaran = 2
            self.biaya_les = 500000
        elif tingkatan == "smp":
            self.jam_pengajaran = 1
            self.biaya_les = 700000
        else:
            self.jam_pengajaran = 1
            self.biaya_les = 1000000
    
    def cetak_kartu(self):
        clear_screen()
        print(f"{"KARTU MURID":^50}")
        print("=" * 50)
        print(f"{"Nama":<25}: {self.nama}")
        print(f"{"Tingkatan":<25}: {self.tingkatan}")
        print(f"{"Jam Pengajaran":<25}: {self.jam_pengajaran} jam")
        print(f"{"Biaya Les":<25}: Rp {self.biaya_les}")
        print("=" * 50)
        input("Tekan ENTER untuk kembali...")


daftar_murid = []


def pendaftaran():
    print(f"{"PENDAFTARAN MURID BARU":^50}")
    print("=" * 50)
    
    nama = input(f"{"Nama":<25}: ").title()

    tingkatan = input(f"{"Tingkatan [TK/SD/SMP/SMA]":<25}: ").upper()

    while tingkatan != "TK" and tingkatan != "SD" and tingkatan != "SMP" and tingkatan != "SMA":
        print("Tingkatan harus berupa TK, SD, SMP, atau SMA.")
        tingkatan = input(f"{"Tingkatan [TK/SD/SMP]":<25}: ").upper()
    
    murid = KartuMurid(nama, tingkatan)
    daftar_murid.append(murid)

    print("=" * 50)
    print("Pendaftaran berhasil.")
    input("Tekan ENTER untuk kembali...")


def cetak_kartu():
    print(f"{"CETAK KARTU MURID":^50}")
    print("=" * 50)

    print("Murid mana yang ingin dicetak kartunya?")

    count = 0
    for murid in daftar_murid:
        count += 1
        print(f"{count}. {murid.nama}")
    
    pilihan = int(input("\nMasukkan nomor murid yang ingin dicetak kartunya: "))

    while pilihan < 1 or pilihan > count:
        print("Tidak ada murid dengan nomor tersebut.")
        pilihan = int(input("\nMasukkan nomor murid yang ingin dicetak kartunya: "))

    murid = daftar_murid[pilihan - 1]
    murid.cetak_kartu()


while True:
    clear_screen()

    print(f"{"SELAMAT DATANG DI PRIVATE LES":^50}")
    print("=" * 50)
    print("1. Pendaftaran Murid Baru")
    print("2. Cetak Kartu Murid")
    print("3. Keluar")

    pilihan = int(input("\nPilih menu [1/2/3]: "))

    if 1 <= pilihan <= 2:
        clear_screen()
    
    if pilihan == 1:
        pendaftaran()
    elif pilihan == 2:
        cetak_kartu()
    elif pilihan == 3:
        print("Terima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")