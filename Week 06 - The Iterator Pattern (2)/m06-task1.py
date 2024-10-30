import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class DaftarMahasiswa:
    def __init__(self):
        self.isi = []
    
    def tambah(self, mahasiswa):
        self.isi.append(mahasiswa)
    
    def cari(self, cari):
        daftar_cari = []
        for mahasiswa in self.isi:
            if mahasiswa.nim == cari or mahasiswa.nama == cari:
                daftar_cari.append(mahasiswa.absensi())
        if len(daftar_cari) > 0:
            print('Mahasiswa ditemukan!')
            daftar_cari = sorted(daftar_cari, key=lambda x: x['nim'])
            return daftar_cari
        print('Mahasiswa tidak ditemukan.')
        return []

class Mahasiswa:
    def __init__(self, nim, nama, jurusan, jenis_kelamin, hp):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.jenis_kelamin = jenis_kelamin
        self.hp = hp
    
    def absensi(self):
        return self.__dict__

daftar_mahasiswa = DaftarMahasiswa()

def tambah_data():
    print(f'{"TAMBAH DATA MAHASISWA":^80}')
    print('=' * 80)

    valid = False
    
    while valid == False:
        nim = input('NIM: ')
        
        try:
            if nim == '':
                raise ValueError('NIM tidak boleh kosong.')

            for karakter in nim:
                if karakter not in '0123456789':
                    raise ValueError('NIM hanya boleh terdiri dari angka saja.')
            
            if len(nim) != 9:
                raise ValueError('NIM hanya boleh terdiri 9 angka saja.')
            
            valid = True

        except ValueError as e:
            print(str(e))
    
    kode_jurusan = nim[2:5]
    if kode_jurusan == '111':
        jurusan = 'Teknik Informatika'
    elif kode_jurusan == '112':
        jurusan = 'Sistem Informasi'
    elif kode_jurusan == '113':
        jurusan = 'Teknologi Informasi'
    elif kode_jurusan == '211':
        jurusan = 'Akuntansi'
    elif kode_jurusan == '212':
        jurusan = 'Manajemen'

    valid = False
    
    while valid == False:
        nama = input('Nama: ').lower()

        try:
            if nama == '':
                raise ValueError('Nama tidak boleh kosong.')
            
            count = 0

            for karakter in nama:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ':
                    raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter != ' ':
                    count += 1
            
            if count == 0:
                raise ValueError('Nama tidak boleh kosong.')
            
            valid = True

        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        jenis_kelamin = input('Jenis kelamin (L/P): ').lower()

        try:
            if jenis_kelamin == '':
                raise ValueError('Jenis kelamin tidak boleh kosong.')

            if jenis_kelamin != 'l' and jenis_kelamin != 'p':
                raise ValueError('Jenis kelamin harus berupa L atau P.')

            jenis_kelamin = 'Laki-Laki' if jenis_kelamin == 'l' else 'Perempuan'

            valid = True

        except ValueError as e:
            print(str(e))

    valid = False
    
    while valid == False:
        hp = input('Nomor HP: ')

        try:
            if hp == '':
                raise ValueError('Nomor HP tidak boleh kosong.')

            for karakter in hp:
                if karakter not in '0123456789+':
                    raise ValueError('Nomor HP hanya boleh terdiri dari angka dan tanda "+" saja.')
            
            if len(hp) < 8 or len(hp) > 15:
                raise ValueError('Nomor HP hanya boleh terdiri dari 8 - 15 angka saja.')
            
            valid = True

        except ValueError as e:
            print(str(e))

    daftar_mahasiswa.tambah(Mahasiswa(nim, nama.title(), jurusan, jenis_kelamin, hp))

    print('=' * 80)
    print('Data berhasil ditambahkan.')

def absensi_mahasiswa():
    print(f'{"ABSENSI MAHASISWA":^80}')
    print('=' * 80)
    print('1. Cari berdasarkan NIM')
    print('2. Cari berdasarkan Nama')
    print('=' * 80)
    pilihan = int(input('Pilih menu (1/2): '))

    print()

    if pilihan == 1:

        valid = False

        while valid == False:
            nim = input('Masukkan NIM Mahasiswa yang ingin dicari: ')

            try:
                if nim == '':
                    raise ValueError('NIM yang ingin dicari tidak boleh kosong.')

                for karakter in nim:
                    if karakter not in '0123456789':
                        raise ValueError('NIM hanya boleh terdiri dari angka saja.')
                
                if len(nim) != 9:
                    raise ValueError('NIM hanya boleh terdiri 9 angka saja.')
                
                valid = True

            except ValueError as e:
                print(str(e))
    
        print('=' * 80)

        for mahasiswa in daftar_mahasiswa.cari(nim):
            print(mahasiswa)
    
    elif pilihan == 2:

        valid = False

        while valid == False:
            nama = input('Masukkan Nama Mahasiswa yang ingin dicari: ').lower()

            try:
                if nama == '':
                    raise ValueError('Nama yang ingin dicari tidak boleh kosong.')

                count = 0

                for karakter in nama:
                    if karakter not in 'abcdefghijklmnopqrstuvwxyz ':
                        raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
                    if karakter != ' ':
                        count += 1
                
                if count == 0:
                    raise ValueError('Nama tidak boleh kosong.')

                valid = True
            
            except ValueError as e:
                print(str(e))
    
        print('=' * 80)

        for mahasiswa in daftar_mahasiswa.cari(nama.title()):
            print(mahasiswa)

    else:
        print('Pilihan tidak valid.')

def cetak_semua():
    print(f'{'DATA SELURUH MAHASISWA':^80}')
    print('=' * 80)
    
    if len(daftar_mahasiswa.isi) == 0:
        print('Belum ada data mahasiswa.')
    else:
        daftar_mahasiswa_terurut = sorted(daftar_mahasiswa.isi, key=lambda x: x.nim)
        for mahasiswa in daftar_mahasiswa_terurut:
            print(mahasiswa.absensi())
        print('=' * 80)

while True:
    clear_screen()

    print(f'{'MENU ABSENSI MAHASISWA':^80}')
    print('=' * 80)
    print('1. Tambah Data Mahasiswa')
    print('2. Absensi Mahasiswa')
    print('3. Cetak Data Seluruh Mahasiswa')
    print('4. Keluar')
    print('=' * 80)
    pilihan = int(input('Pilih menu (1/2/3/4): '))

    if 1 <= pilihan <= 3:
        clear_screen()
    
    if pilihan == 1:
        tambah_data()
    elif pilihan == 2:
        absensi_mahasiswa()
    elif pilihan == 3:
        cetak_semua()
    elif pilihan == 4:
        print('\nTerima kasih.')
        break
    else:
        print('\nPilihan tidak valid.')
    
    input('Tekan sembarang tombol untuk kembali...')