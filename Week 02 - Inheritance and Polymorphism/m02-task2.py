import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Produk:
    def __init__(self, id, nama, stok, harga):
        self.id = id
        self.nama = nama
        self.stok = stok
        self.harga = harga
        self.pembelian = 0
        self.penjualan = 0

class HandSanitizer(Produk):
    def __init__(self, id, nama, stok, harga, ml):
        super().__init__(id, nama, stok, harga)
        self.ml = ml

class BanMobil(Produk):
    def __init__(self, id, nama, stok, harga, diameter):
        super().__init__(id, nama, stok, harga)
        self.diameter = diameter

class BuahBuahan(Produk):
    def __init__(self, id, nama, stok, harga, berat):
        super().__init__(id, nama, stok, harga)
        self.berat = berat

class BotolMinumanBayi(Produk):
    def __init__(self, id, nama, stok, harga, ukuran):
        super().__init__(id, nama, stok, harga)
        self.ukuran = ukuran

id = ["ITM-001", "ITM-002", "ITM-003", "ITM-004", "ITM-005"]
barang = ["Hand Sanitizer", "Ban Mobil", "Buah-Buahan", "Botol Minuman Bayi"]
harga = [25000, 100000, 70000, 30000]
stok = [5, 3, 4, 3]
produk = []

produk.append(HandSanitizer(id[0], barang[0], stok[0], harga[0], "150 ml"))
produk.append(BanMobil(id[1], barang[1], stok[1], harga[1], "60 cm"))
produk.append(BuahBuahan(id[2], barang[2], stok[2], harga[2], "1 kg"))
produk.append(BotolMinumanBayi(id[3], barang[3], stok[3], harga[3], "250 ml"))

def tampilkan_barang():
    print(f"{"TAMPILKAN BARANG":^80}")
    print("=" * 80)

    print(f"{"No":<5}{"ID":<10}{"Nama Barang":<25}{"Stok":<8}{"Pembelian":<12}{"Penjualan"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].id:<10}{produk[i].nama:<25}{produk[i].stok:<8}{produk[i].pembelian:<12}{produk[i].penjualan}")
    
    print("=" * 80)
    input("Tekan ENTER untuk kembali...")

def jual_barang():
    print(f"{"JUAL PRODUK":^80}")
    print("=" * 80)

    print(f"{"No":<5}{"ID":<10}{"Produk":<25}{"Stok"}")

    for i in range(len(produk)):
        print(f"{i + 1:<5}{produk[i].id:<10}{produk[i].nama:<25}{produk[i].stok}")
    
    print("=" * 80)

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
    produk[nomor].penjualan += jumlah

    print("=" * 80)
    print(f"{produk[nomor].nama} telah dijual sebanyak {jumlah} buah.")
    input("Tekan ENTER untuk kembali...")

def tambah_barang():
    print(f"{"TAMBAH BARANG":^80}")
    print("=" * 80)
    print("1. Beli Barang Baru")
    print("2. Tambah Stok Barang Lama")
    print("=" * 80)

    pilihan = int(input("Masukkan pilihan [1/2]: "))

    print()

    if pilihan == 1:
        id = input(f"{"ID Barang":<20}: ").upper()
        nama = input(f"{"Nama Barang":<20}: ").title()
        harga_beli = int(input(f"{"Harga Beli":<20}: "))
        stok = int(input(f"{"Jumlah Pembelian":<20}: "))

        produk_baru = Produk(id, nama, stok, harga_beli)
        produk_baru.pembelian = stok
        produk.append(produk_baru)

        print("=" * 80)
        print("Barang berhasil ditambahkan")
    elif pilihan == 2:
        print(f"{"No":<5}{"ID":<10}{"Nama Barang":<25}{"Harga":<10}{"Stok"}")

        for i in range(len(produk)):
            print(f"{i + 1:<5}{produk[i].id:<10}{produk[i].nama:<25}{produk[i].harga:<10}{produk[i].stok}")
        
        print()

        nomor = int(input("Masukkan nomor barang yang ingin dibeli: "))

        while nomor < 1 or nomor > len(produk):
            print("Tidak ada produk dengan nomor tersebut.\n")
            nomor = int(input("Masukkan nomor barang yang ingin dibeli: "))
        
        nomor -= 1

        print()

        jumlah = int(input(f"Masukkan jumlah {produk[nomor].nama} yang ingin dibeli: "))

        while jumlah <= 0:
            print("Jumlah barang yang dibeli minimal 1.\n")
            jumlah = int(input(f"Masukkan jumlah {produk[nomor].nama} yang ingin dibeli: "))

        produk[nomor].stok += jumlah
        produk[nomor].pembelian += jumlah

        print("=" * 80)
        print("Barang berhasil ditambahkan")
    else:
        print("Pilihan tidak valid")

    input("Tekan ENTER untuk kembali...")

def laporan():
    print(f"{"LAPORAN PENGELUARAN":^80}")
    print("=" * 80)

    total = 0

    print(f"{"ID":<10}{"Nama Barang":<25}{"Harga":<10}{"Stok":<10}{"Pembelian":<12}{"Penjualan"}")

    for i in range(len(produk)):
        print(f"{produk[i].id:<10}{produk[i].nama:<25}{produk[i].harga:<10}{produk[i].stok:<10}{produk[i].pembelian:<12}{produk[i].penjualan}")
        total += produk[i].pembelian * produk[i].harga
    
    print("=" * 80)
    print(f"Total Pengeluaran: Rp {total}")
    input("Tekan ENTER untuk kembali...")

while True:
    clear_screen()

    print(f"{"MENU":^80}")
    print("=" * 80)
    print("1. Tambah Barang")
    print("2. Jual Barang")
    print("3. Tampilkan Barang / Laporan")
    print("4. Keluar")
    print("=" * 80)

    pilihan = int(input("Pilih menu [1/2/3/4]: "))

    if 1 <= pilihan <= 3:
        clear_screen()

    if pilihan == 1:
        tambah_barang()
    elif pilihan == 2:
        jual_barang()
    elif pilihan == 3:
        laporan()
    elif pilihan == 4:
        print("Terima kasih.\n")
        break
    else:
        print("Pilihan tidak valid.")
        input("Tekan ENTER untuk kembali...")