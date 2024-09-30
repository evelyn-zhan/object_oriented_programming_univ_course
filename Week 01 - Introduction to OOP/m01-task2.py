import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Produk:
    def __init__(self, nama, stok, harga_beli, harga_jual):
        self.nama = nama
        self.stok = stok
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual

barang = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
harga_beli = [25000, 100000, 70000, 30000]
harga_jual = [30000, 120000, 80000, 40000]
stok = [5, 3, 4, 3]
produk = []

for i in range(len(barang)):
    produk.append(Produk(barang[i], stok[i], harga_beli[i], harga_jual[i]))

def cek_stok():
    print(f"{"CEK STOK BARANG":^50}")
    print("=" * 50)

    print(f"{"No":<5}{"Nama Barang":<25}{"Stok"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].stok}")
    
    print("=" * 50)
    input("Tekan ENTER untuk kembali...")

def jual_produk():
    print(f"{"JUAL PRODUK":^50}")
    print("=" * 50)

    print(f"{"No":<5}{"Produk":<25}{"Stok":<8}{"Harga Jual"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].nama:<25}{produk[i].stok:<8}{produk[i].harga_jual}")
    
    print("=" * 50)

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

    print("=" * 50)
    print(f"{produk[nomor].nama} telah dijual sebanyak {jumlah} buah.")
    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"MENU":^50}")
    print("=" * 50)
    print("1. Cek Stok")
    print("2. Jual Produk")
    print("3. Beli Stok")
    print("4. Laporan Pengeluaran")
    print("5. Keluar")
    print("=" * 50)

    pilihan = int(input("\nPilih menu [1/2/3/4]: "))

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