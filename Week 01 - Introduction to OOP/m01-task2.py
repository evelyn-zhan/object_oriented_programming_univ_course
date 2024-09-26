import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Produk:
    def __init__(self, nama, stok):
        self.nama = nama
        self.stok = stok

barang = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
daftar_produk = []

clear_screen()

print(f"{"PENGINPUTAN STOK BARANG":^50}")
print("=" * 50)

for i in range(len(barang)):
    stok = int(input(f"Masukkan jumlah stok {barang[i]}: "))
    produk = Produk(barang[i], stok)
    daftar_produk.append(produk)

print()

print(f"{"LAPORAN STOK BARANG":^50}")
print("=" * 50)

print(f"{"Nama Produk":<30}{"Jumlah Stok"}")
print("-" * 50)

for i in range(len(daftar_produk)):
    print(f"{daftar_produk[i].nama:<30}{daftar_produk[i].stok}")

print()