import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Produk:
    def __init__(self, nama, stok, harga_beli, harga_jual):
        self.nama = nama
        self.stok = stok
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.pembelian = 0
    
class HandSanitizer(Produk):
    def __init__(self, nama, stok, harga_beli, harga_jual, ml):
        super().__init__(nama, stok, harga_beli, harga_jual)
        self.ml = ml

class BanMobil(Produk):
    def __init__(self, nama, stok, harga_beli, harga_jual, diameter):
        super().__init__(nama, stok, harga_beli, harga_jual)
        self.diameter = diameter

class BuahBuahan(Produk):
    def __init__(self, nama, stok, harga_beli, harga_jual, berat):
        super().__init__(nama, stok, harga_beli, harga_jual)
        self.berat = berat

class BotolMinumanBayi(Produk):
    def __init__(self, nama, stok, harga_beli, harga_jual, ukuran):
        super().__init__(nama, stok, harga_beli, harga_jual)
        self.ukuran = ukuran

barang = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
harga_beli = [25000, 100000, 70000, 30000]
harga_jual = [30000, 120000, 80000, 40000]
stok = [5, 3, 4, 3]
produk = []

produk.append(HandSanitizer("Hand Sanitizer", stok[0], harga_beli[0], harga_jual[0], "150 ml"))
produk.append(BanMobil("Ban Mobil", stok[1], harga_beli[1], harga_jual[1], "60 cm"))
produk.append(BuahBuahan("Buah-Buahan", stok[2], harga_beli[2], harga_jual[2], "1 kg"))
produk.append(BotolMinumanBayi("Botol Minuman Bayi", stok[3], harga_beli[3], harga_jual[3], "250 ml"))

def cek_stok():
    print(f"{"CEK STOK BARANG":^70}")
    print("=" * 70)

    print(f"{"No":<5}{"Nama Barang":<25}{"Stok"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].stok}")
    
    print("=" * 70)
    input("Tekan ENTER untuk kembali...")

def jual_produk():
    print(f"{"JUAL PRODUK":^70}")
    print("=" * 70)

    print(f"{"No":<5}{"Produk":<25}{"Stok":<8}{"Harga Jual"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].stok:<8}{produk[i].harga_jual}")
    
    print("=" * 70)

    nomor = int(input("Masukkan nomor barang yang ingin dijual: "))

    while nomor < 1 or nomor > len(produk):
        print("Tidak ada produk dengan nomor tersebut.\n")
        nomor = int(input("Masukkan nomor barang yang ingin dijual: "))
    
    nomor -= 1

    print()

    jumlah = int(input(f"Masukkan jumlah {produk[nomor].nama} yang ingin dijual: "))

    while jumlah == 0 or jumlah > produk[nomor].stok:
        print("Jumlah barang yang dijual minimal 1 dan tidak boleh melebihi stok yang ada.\n")
        jumlah = int(input(f"Masukkan jumlah {produk[nomor].nama} yang ingin dijual: "))
    
    produk[nomor].stok -= jumlah

    print("=" * 70)
    print(f"{produk[nomor].nama} telah dijual sebanyak {jumlah} buah.")
    input("Tekan ENTER untuk kembali...")

def beli_stok():
    print(f"{"BELI STOK BARANG":^70}")
    print("=" * 70)

    print(f"{"No":<5}{"Produk":<25}{"Harga Beli"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].harga_beli}")
    
    print("=" * 70)

    nomor = int(input("Masukkan nomor barang yang ingin dibeli: "))

    while nomor < 1 or nomor > len(produk):
        print("Tidak ada produk dengan nomor tersebut.\n")
        nomor = int(input("Masukkan nomor barang yang ingin dibeli: "))
    
    nomor -= 1

    print()

    jumlah = int(input(f"Masukkan berapa buah {produk[nomor].nama} yang ingin dibeli: "))

    while jumlah <= 0:
        print("Jumlah barang yang dibeli minimal 1.\n")
        jumlah = int(input(f"Masukkan berapa buah {produk[nomor].nama} yang ingin dijumlah: "))

    produk[nomor].stok += jumlah
    produk[nomor].pembelian += jumlah

    print("=" * 70)
    print(f"{produk[nomor].nama} telah dibeli sebanyak {jumlah} buah.")
    input("Tekan ENTER untuk kembali...")

def laporan_pengeluaran():
    print(f"{"LAPORAN PENGELUARAN":^70}")
    print("=" * 70)

    total = 0

    print(f"{"No":<5}{"Produk":<25}{"Harga Beli":<15}{"Jumlah Pembelian"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].harga_beli:<15}{produk[i].pembelian}")
        total += produk[i].pembelian * produk[i].harga_beli
    
    print("=" * 70)
    print(f"Total Pengeluaran: Rp {total}")
    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"MENU":^70}")
    print("=" * 70)
    print("1. Cek Stok")
    print("2. Jual Produk")
    print("3. Beli Stok")
    print("4. Laporan Pengeluaran")
    print("5. Keluar")
    print("=" * 70)

    pilihan = int(input("\nPilih menu [1/2/3/4/5]: "))

    if 1 <= pilihan <= 4:
        clear_screen()

    if pilihan == 1:
        cek_stok()
    elif pilihan == 2:
        jual_produk()
    elif pilihan == 3:
        beli_stok()
    elif pilihan == 4:
        laporan_pengeluaran()
    elif pilihan == 5:
        print("\nTerima kasih.\n")
        break
    else:
        print("\nPilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")