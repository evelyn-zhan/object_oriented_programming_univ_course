import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Orang:
    def __init__(self, kode, nama, hp):
        if(self.cek_kode(kode) and self.cek_nama(nama) and self.cek_hp(hp)):
            self.kode = kode
            self.nama = nama.title()
            self.hp = hp
            print('Data berhasil ditambahkan.')
        else:
            self.kode = ''
            self.nama = ''
            self.hp = ''
    
    def cek_kode(self, kode):
        angka = '0123456789'
        valid = True

        for karakter in kode:
            if karakter not in angka:
                valid = False

        try:
            if not valid:
                raise ValueError('Kode harus terdiri dari angka saja.')
            
            if len(kode) != 9:
                raise ValueError('Kode harus memiliki panjang 9 karakter.')
            
        except ValueError as e:
            print(str(e))
            return False
        
        return True

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

    def cek_hp(self, hp):
        valid = True
        angka = '0123456789+'

        for karakter in hp:
            if karakter not in angka:
                valid = False
        
        try:
            if len(hp) < 8 or len(hp) > 15:
                raise ValueError('Nomor HP hanya boleh terdiri dari 8 - 15 angka saja.')
            
            if not valid:
                raise ValueError('Nomor HP harus terdiri dari angka atau tanda "+" saja.')
            
        except ValueError as e:
            print(str(e))
            return False
        
        return True

dosen = []
mahasiswa = []

def tambah_dosen():
    print(f'{'TAMBAH DATA DOSEN':^80}')
    print('=' * 80)
    
    kode = input('NIP: ')
    nama = input('Nama: ').lower()
    hp = input('Nomor HP: ')

    print('=' * 80)

    data_dosen = Orang(kode, nama, hp)

    if data_dosen.kode != '' and data_dosen.nama != '' and data_dosen.hp != '':
        dosen.append(data_dosen)

def tambah_mahasiswa():
    print(f'{'TAMBAH DATA MAHASISWA':^80}')
    print('=' * 80)
    
    kode = input('NIM: ')
    nama = input('Nama: ').lower()
    hp = input('Nomor HP: ')

    print('=' * 80)

    data_mahasiswa = Orang(kode, nama, hp)

    if data_mahasiswa.kode != '' and data_mahasiswa.nama != '' and data_mahasiswa.hp != '':
        mahasiswa.append(data_mahasiswa)

def cetak_data():
    print(f'{'CETAK DATA':^80}')
    print('=' * 80)
    print()

    print(f'{'DAFTAR DOSEN':^80}')
    print('=' * 80)

    if len(dosen) == 0:
        print('Belum ada data dosen.')
    else:
        print(f'{'No':<5}{'NIP':<15}{'Nama':<25}{'Nomor HP'}')
        for i in range(len(dosen)):
            print(f'{i + 1:<5}{dosen[i].kode:<15}{dosen[i].nama:<25}{dosen[i].hp}')

    print('=' * 80)
    print()

    print(f'{'DAFTAR MAHASISWA':^80}')
    print('=' * 80)

    if len(mahasiswa) == 0:
        print('Belum ada data mahasiswa.')
    else:
        print(f'{'No':<5}{'NIM':<15}{'Nama':<25}{'Nomor HP'}')
        for i in range(len(mahasiswa)):
            print(f'{i + 1:<5}{mahasiswa[i].kode:<15}{mahasiswa[i].nama:<25}{mahasiswa[i].hp}')

    print('=' * 80)
    print()

while True:
    clear_screen()

    print(f'{'MENU':^80}')
    print('=' * 80)
    print('1. Tambah Data Dosen')
    print('2. Tambah Data Mahasiswa')
    print('3. Cetak Data')
    print('4. Keluar')
    print('=' * 80)

    pilihan = int(input('Pilih menu [1/2/3/4]: '))

    if 1 <= pilihan <= 3:
        clear_screen()

    if pilihan == 1:
        tambah_dosen()
    elif pilihan == 2:
        tambah_mahasiswa()
    elif pilihan == 3:
        cetak_data()
    elif pilihan == 4:
        print('\nTerima kasih.\n')
        break
    else:
        print('\nPilihan tidak valid.')
    
    input('Tekan sembarang tombol untuk kembali...')