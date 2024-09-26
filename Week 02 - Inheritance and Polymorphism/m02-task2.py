import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class JesslynCaroline:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok

class HandSanitizer(JesslynCaroline):
    def __init__(self, nama, stok, ml):
        super().__init__(nama, stok)
        self.ml = ml

class BanMobil(JesslynCaroline):
    def __init__(self, nama, stok, diameter):
        super().__init__(nama, stok)
        self.diameter = diameter

class BuahBuahan(JesslynCaroline):
    def __init__(self, nama, stok):
        super().__init__(nama, stok)

class BotolMinumanBayi(JesslynCaroline):
    def __init__(self, nama, stok, ukuran):
        super().__init__(nama, stok)
        self.ukuran = ukuran

barang = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
stok = []
produk = []

clear_screen()

print(f"{"PENGINPUTAN STOK BARANG":^50}")
print("=" * 50)

for i in range(len(barang)):
    stok.append(int(input(f"Masukkan jumlah stok {barang[i]}: ")))

produk.append(HandSanitizer("Hand Sanitizer", stok[0], "150 ml"))
produk.append(BanMobil("Ban Mobil", stok[1], 15))
produk.append(BuahBuahan("Buah-Buahan", stok[2]))
produk.append(BotolMinumanBayi("Botol Minuman Bayi", stok[3], "250 ml"))

print()

print(f"{"LAPORAN STOK BARANG":^50}")
print("=" * 50)

print(f"{"Nama Produk":<30}{"Jumlah Stok"}")
print("-" * 50)

for i in range(len(produk)):
    print(f"{produk[i].nama:<30}{produk[i].stok}")

print()