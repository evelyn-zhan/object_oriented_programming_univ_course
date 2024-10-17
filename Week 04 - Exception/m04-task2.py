import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class KartuMurid:
    def __init__(self, nama, tingkatan):
        if self.cek_nama(nama):
            self.nama = nama.title()
            self.tingkatan = tingkatan
            if tingkatan == 'tk':
                self.jam_pengajaran = 2
                self.biaya_les = 300000
            elif tingkatan == 'sd':
                self.jam_pengajaran = 2
                self.biaya_les = 500000
            elif tingkatan == 'smp':
                self.jam_pengajaran = 1
                self.biaya_les = 700000
            else:
                self.jam_pengajaran = 1
                self.biaya_les = 1000000
        else:
            self.nama = ''
            self.tingkatan = ''
            self.jam_pengajaran = 0
            self.biaya_les = 0
    
    def cek_nama(self, nama):
        huruf = 'abcdefghijklmnopqrstuvwxyz'
        valid = True

        for karakter in nama:
            if karakter not in huruf and karakter != ' ':
                valid = False
        
        try:
            if len(nama) == 0:
                raise ValueError('Nama tidak boleh kosong.')
            
            if not valid:
                raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
        
        except ValueError as e:
            print(str(e))
            return False

        return True
    
    def cetak_kartu(self):
        clear_screen()
        print(f'{'KARTU MURID':^50}')
        print('=' * 50)
        print(f'{'Nama':<25}: {self.nama}')
        print(f'{'Tingkatan':<25}: {self.tingkatan}')
        print(f'{'Jam Pengajaran':<25}: {self.jam_pengajaran} jam')
        print(f'{'Biaya Les':<25}: Rp {self.biaya_les}')
        print('=' * 50)
        input('Tekan ENTER untuk kembali...')

murid = []

def pendaftaran():
    print(f'{'PENDAFTARAN MURID BARU':^50}')
    print('=' * 50)
    
    nama = input(f'{'Nama':<25}: ').lower()

    tingkatan = input(f'{'Tingkatan [TK/SD/SMP/SMA]':<25}: ').upper()

    while tingkatan != 'TK' and tingkatan != 'SD' and tingkatan != 'SMP' and tingkatan != 'SMA':
        print('Tingkatan harus berupa TK, SD, SMP, atau SMA.')
        tingkatan = input(f'{'Tingkatan [TK/SD/SMP]':<25}: ').upper()
    
    data_murid = KartuMurid(nama, tingkatan)

    if data_murid.nama != '':
        murid.append(data_murid)

    print('=' * 50)

def cetak_kartu():
    print(f'{'CETAK KARTU MURID':^50}')
    print('=' * 50)

    if len(murid) == 0:
        print('Belum ada data murid.')
    else:
        print('Murid mana yang ingin dicetak kartunya?')
        for i in range(len(murid)):
            print(f'{i + 1}. {murid[i].nama}')
        print('=' * 50)
        
        nomor = int(input('\nMasukkan nomor murid yang ingin dicetak kartunya: '))

        while nomor < 1 or nomor > len(murid):
            print('Tidak ada murid dengan nomor tersebut.')
            nomor = int(input('\nMasukkan nomor murid yang ingin dicetak kartunya: '))

        murid[nomor - 1].cetak_kartu()
    
    print('=' * 50)

while True:
    clear_screen()

    print(f'{'SELAMAT DATANG DI PRIVATE LES':^50}')
    print('=' * 50)
    print('1. Pendaftaran Murid Baru')
    print('2. Cetak Kartu Murid')
    print('3. Keluar')
    print('=' * 50)

    pilihan = int(input('Pilih menu [1/2/3]: '))

    if 1 <= pilihan <= 2:
        clear_screen()
    
    if pilihan == 1:
        pendaftaran()
    elif pilihan == 2:
        cetak_kartu()
    elif pilihan == 3:
        print('\nTerima kasih.\n')
        break
    else:
        print('\nPilihan tidak valid.')
    
    input('Tekan sembarang tombol untuk kembali...')