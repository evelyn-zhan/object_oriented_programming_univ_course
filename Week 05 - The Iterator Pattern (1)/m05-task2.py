import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class DaftarProduk:
    def __init__(self):
        self.isi = []
    
    def tambah(self, produk):
        self.isi.append(produk)
    
    def cetak(self):
        iterator = iter(self.isi)
        
        while True:
            try:
                produk = next(iterator)
                print(produk.cetak())
            except StopIteration:
                break
    
    def cari(self, kode):
        iterator = iter(self.isi)

        while True:
            try:
                produk = next(iterator)
                if produk.kode == kode:
                    return produk
            except StopIteration:
                return None
    
    def tambah_stok(self, kode, jumlah):
        iterator = iter(self.isi)

        while True:
            try:
                produk = next(iterator)
                if produk.kode == kode:
                    produk.jumlah += jumlah
                    return
            except StopIteration:
                break
    
    def jual(self, kode, jumlah):
        iterator = iter(self.isi)

        while True:
            try:
                produk = next(iterator)
                if produk.kode == kode:
                    produk.jumlah -= jumlah
                    return
            except StopIteration:
                break

class Produk:
    def __init__(self, kode, nama, jumlah, jenis):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah
        self.jenis = jenis
    
    def cetak(self):
        return self.__dict__

daftar_produk = DaftarProduk()

def tambah_produk():
    print(f'{'TAMBAH PRODUK':^80}')
    print('=' * 80)
    print('1. Tambah Produk Lama')
    print('2. Tambah Produk Baru')
    print('3. Kembali')
    print('=' * 80)
    pilihan = int(input('Pilih menu (1/2/3): '))

    if 1 <= pilihan <= 2:
        print()

    if pilihan == 1:
        daftar_produk.cetak()
        print('=' * 80)

        valid = False

        while valid == False:
            kode = input('Masukkan kode produk yang ingin ditambah stoknya: ').upper()

            try:
                if kode == '':
                    raise ValueError('Kode produk tidak boleh kosong.\n')
                
                if daftar_produk.cari(kode) is None:
                    raise ValueError('Produk tidak ditemukan.\n')
                
                valid = True

            except ValueError as e:
                print(str(e))

        valid = False

        while valid == False:
            jumlah = int(input('Masukkan stok produk yang ingin ditambah: '))

            try:
                if jumlah <= 0:
                    raise ValueError('Jumlah produk yang ditambahkan harus lebih dari 0.')
                    
                valid = True
                
            except ValueError as e:
                print(str(e))
            
        daftar_produk.tambah_stok(kode, jumlah)

        print('=' * 80)
        print('Stok produk berhasil ditambahkan.')

    elif pilihan == 2:
        valid = False

        while valid == False:
            kode = input('Masukkan kode produk: ').upper()

            try:
                if kode == '':
                    raise ValueError('Kode produk tidak boleh kosong.\n')
                
                if daftar_produk.cari(kode) is not None:
                    raise ValueError('Produk dengan kode tersebut sudah ada.\n')
                
                valid = True
            
            except ValueError as e:
                print(str(e))
        
        valid = False

        while valid == False:
            nama = input('Masukkan nama produk: ').title()

            try:
                if nama == '':
                    raise ValueError('Nama produk tidak boleh kosong.\n')
                
                valid = True
            
            except ValueError as e:
                print(str(e))
        
        valid = False

        while valid == False:
            jumlah = int(input('Masukkan stok produk: '))

            try:
                if jumlah <= 0:
                    raise ValueError('Stok produk harus lebih dari 0.\n')
                
                valid = True
            
            except ValueError as e:
                print(str(e))
        
        valid = False

        while valid == False:
            jenis = input('Masukkan jenis produk: ').title()

            try:
                if jenis == '':
                    raise ValueError('Jenis produk tidak boleh kosong.\n')
                
                valid = True
            
            except ValueError as e:
                print(str(e))
        
        daftar_produk.tambah(Produk(kode, nama, jumlah, jenis))

        print('=' * 80)
        print('Produk baru berhasil ditambahkan.')

    elif pilihan == 3:
        pass
    else:
        print('\nPilihan tidak valid.')

def cari_produk():
    print(f'{'CARI PRODUK':^80}')
    print('=' * 80)

    valid = False

    while valid == False:
        kode = input('Masukkan kode produk: ').upper()

        try:
            if kode == '':
                raise ValueError('Kode produk tidak boleh kosong.\n')
            
            if daftar_produk.cari(kode) is None:
                raise ValueError('Produk tidak ditemukan.\n')
            
            valid = True
        
        except ValueError as e:
            print(str(e))

    print('=' * 80)
    print('Produk ditemukan!')
    
    produk = daftar_produk.cari(kode)
    print(produk.cetak())

    if produk.jumlah <= 5:
        print('Stok produk ini sudah mau habis. Jangan lupa untuk menambah stok.')

def jual_produk():
    print(f'{'JUAL PRODUK':^80}')
    print('=' * 80)
    daftar_produk.cetak()
    print('=' * 80)

    valid = False

    while valid == False:
        kode = input('Masukkan kode produk: ').upper()

        try:
            if kode == '':
                raise ValueError('Kode produk tidak boleh kosong.\n')
            
            if daftar_produk.cari(kode) is None:
                raise ValueError('Produk tidak ditemukan.\n')
            
            valid = True
        
        except ValueError as e:
            print(str(e))
    
    print()
    
    valid = False
    produk = daftar_produk.cari(kode)

    while valid == False:
        jumlah = int(input('Masukkan jumlah dari produk tersebut yang ingin dijual: '))

        try:
            if jumlah <= 0:
                raise ValueError('Jumlah produk yang dijual harus lebih dari 0.\n')
            
            if jumlah > produk.jumlah:
                raise ValueError('Jumlah produk yang dijual tidak boleh melebihi stok.\n')
            
            valid = True
        
        except ValueError as e:
            print(str(e))

    daftar_produk.jual(kode, jumlah)

    print('=' * 80)
    print('Produk berhasil dijual!')

daftar_produk.tambah(Produk('A001', 'Hand Sanitizer', 10, 'Kebersihan'))
daftar_produk.tambah(Produk('A002', 'Ban Mobil', 8, 'Otomotif'))
daftar_produk.tambah(Produk('A003', 'Buah-Buahan', 5, 'Produk Makanan Segar'))
daftar_produk.tambah(Produk('A004', 'Botol Minuman Bayi', 8, 'Perlengkapan Bayi'))

while True:
    clear_screen()

    print(f'{'DATA PRODUK E-COMMERCE':^80}')
    print('=' * 80)
    print('1. Tambah Produk')
    print('2. Cari Produk')
    print('3. Jual Produk')
    print('4. Keluar')
    print('=' * 80)
    pilihan = int(input('Pilih menu (1/2/3/4): '))

    if 1 <= pilihan <= 3:
        clear_screen()
    
    if pilihan == 1:
        tambah_produk()
    elif pilihan == 2:
        cari_produk()
    elif pilihan == 3:
        jual_produk()
    elif pilihan == 4:
        print('\nTerima kasih.')
        break
    else:
        print('\nPilihan tidak valid.')
    
    input('Tekan sembarang tombol untuk kembali...')