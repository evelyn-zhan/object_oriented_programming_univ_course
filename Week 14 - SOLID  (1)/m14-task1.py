import os
from abc import ABC, abstractmethod

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

class Daftar:
    def __init__(self):
        self.isi = []
    
    def jumlah(self):
        return len(self.isi)
    
    def tambah(self, data):
        self.isi.append(data)

class Mahasiswa:
    def __init__(self, nim, nama, jenis_kelamin, hp, jurusan):
        self.nim = nim
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.hp = hp
        self.jurusan = jurusan
    
    def __str__(self):
        return str(self.__dict__)

class Dosen:
    def __init__(self, nip, nama, jenis_kelamin, hp, jabatan):
        self.nip = nip
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.hp = hp
        self.jabatan = jabatan
    
    def __str__(self):
        return str(self.__dict__)

class Absensi(ABC):
    @abstractmethod
    def cetak_absensi(self): pass

class AbsensiMahasiswa(Absensi):
    def cetak_absensi(self, daftar):
        print('Daftar mahasiswa:')

        jumlah = daftar.jumlah()

        if jumlah == 0:
            print('Belum ada data mahasiswa.')
        else:
            print(f'Terdapat {jumlah} orang mahasiswa.')
            for mahasiswa in daftar.isi:
                print(mahasiswa)

        print('-' * 80)

class AbsensiDosen(Absensi):
    def cetak_absensi(self, daftar):
        print('Daftar dosen:')

        jumlah = daftar.jumlah()

        if jumlah == 0:
            print('Belum ada data dosen.')
        else:
            print(f'Terdapat {jumlah} orang dosen.')
            for dosen in daftar.isi:
                print(dosen)

        print('-' * 80)

daftar_mahasiswa = Daftar()
daftar_dosen = Daftar()

def tambah_mahasiswa():
    print(f'{'TAMBAH DATA MAHASISWA':^80}')
    print('-' * 80)

    valid = False

    while valid == False:
        nim = input('Masukkan NIM: ')

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
    
    valid = False

    while valid == False:
        nama = input('Masukkan nama: ').lower()

        try:
            if nama == '':
                raise ValueError('Nama tidak boleh kosong.')
            
            spasi = 0
            
            for karakter in nama:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ':
                    raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter == ' ':
                    spasi += 1
            
            if spasi == len(nama):
                raise ValueError('Nama tidak boleh hanya terdiri dari spasi saja.')

            valid = True
            nama = nama.title()
        
        except ValueError as e:
            print(str(e))

    valid = False

    while valid == False:
        jenis_kelamin = input('Masukkan jenis kelamin (L/P): ').upper()

        try:
            if jenis_kelamin == '':
                raise ValueError('Jenis kelamin tidak boleh kosong.')

            if jenis_kelamin not in ['L', 'P']:
                raise ValueError('Jenis kelamin hanya boleh berupa L atau P.')

            valid = True
            jenis_kelamin = 'Laki-laki' if jenis_kelamin == 'L' else 'Perempuan'
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        hp = input('Masukkan nomor HP: ')

        try:
            if hp == '':
                raise ValueError('Nomor HP tidak boleh kosong.')
            
            for karakter in hp:
                if karakter not in '0123456789+':
                    raise ValueError("Nomor HP hanya boleh terdiri dari angka atau tanda '+' saja.")
            
            if len(hp) < 8 or len(hp) > 15:
                raise ValueError('Nomor HP hanya boleh terdiri dari 8 - 15 angka saja.')

            valid = True

        except ValueError as e:
            print(str(e))

    if nim[2:5] == '111':
        jurusan = 'Teknik Informatika'
    elif nim[2:5] == '112':
        jurusan = 'Sistem Informasi'
    elif nim[2:5] == '113':
        jurusan = 'Teknologi Informasi'
    elif nim[2:5] == '211':
        jurusan = 'Akuntansi'
    elif nim[2:5] == '212':
        jurusan = 'Manajemen'
    
    mahasiswa = Mahasiswa(nim, nama, jenis_kelamin, hp, jurusan)
    daftar_mahasiswa.tambah(mahasiswa)

    print('-' * 80)
    print('Data mahasiswa berhasil ditambahkan.')

def tambah_dosen():
    print(f'{'TAMBAH DATA DOSEN':^80}')
    print('-' * 80)

    valid = False

    while valid == False:
        nip = input('Masukkan NIP: ')

        try:
            if nip == '':
                raise ValueError('NIP tidak boleh kosong.')
            
            for karakter in nip:
                if karakter not in '0123456789':
                    raise ValueError('NIP hanya boleh terdiri dari angka saja.')

            if len(nip) != 9:
                raise ValueError('NIP hanya boleh terdiri 9 angka saja.')

            valid = True
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        nama = input('Masukkan nama: ').lower()

        try:
            if nama == '':
                raise ValueError('Nama tidak boleh kosong.')
            
            spasi = 0
            
            for karakter in nama:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ':
                    raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter == ' ':
                    spasi += 1
            
            if spasi == len(nama):
                raise ValueError('Nama tidak boleh hanya terdiri dari spasi saja.')

            valid = True
            nama = nama.title()
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        jenis_kelamin = input('Masukkan jenis kelamin (L/P): ').upper()

        try:
            if jenis_kelamin == '':
                raise ValueError('Jenis kelamin tidak boleh kosong.')

            if jenis_kelamin not in ['L', 'P']:
                raise ValueError('Jenis kelamin hanya boleh berupa L atau P.')

            valid = True
            jenis_kelamin = 'Laki-Laki' if jenis_kelamin == 'L' else 'Perempuan'
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        hp = input('Masukkan nomor HP: ')

        try:
            if hp == '':
                raise ValueError('Nomor HP tidak boleh kosong.')
            
            for karakter in hp:
                if karakter not in '0123456789+':
                    raise ValueError("Nomor HP hanya boleh terdiri dari angka atau tanda '+' saja.")
            
            if len(hp) < 8 or len(hp) > 15:
                raise ValueError('Nomor HP hanya boleh terdiri dari 8 - 15 angka saja.')

            valid = True
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        jabatan = input('Masukkan jabatan: ').lower()

        try:
            if jabatan == '':
                raise ValueError('Jabatan tidak boleh kosong.')
            
            spasi = 0
            
            for karakter in jabatan:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ':
                    raise ValueError('Jabatan hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter == ' ':
                    spasi += 1
            
            if spasi == len(jabatan):
                raise ValueError('Jabatan tidak boleh hanya terdiri dari spasi saja.')

            valid = True
            jabatan.title()
        
        except ValueError as e:
            print(str(e))

    dosen = Dosen(nip, nama, jenis_kelamin, hp, jabatan)
    daftar_dosen.tambah(dosen)

    print('-' * 80)
    print('Data dosen berhasil ditambahkan.')

def absensi():
    print(f'{'ABSENSI':^80}')
    print('-' * 80)

    # for proses in Absensi.__subclasses__():
    for proses in [AbsensiMahasiswa(), AbsensiDosen()]:
        proses.cetak_absensi(daftar_mahasiswa if isinstance(proses, AbsensiMahasiswa) else daftar_dosen)

if __name__ == '__main__':
    while True:
        cls()

        print(f'{'ABSENSI KAMPUS':^80}')
        print('-' * 80)
        print('1. Tambah data mahasiswa')
        print('2. Tambah data dosen')
        print('3. Absensi')
        print('4. Keluar')
        print('-' * 80)

        pilihan = input('Pilih menu (1/2/3/4): ')

        if pilihan == '1':
            cls()
            tambah_mahasiswa()
        elif pilihan == '2':
            cls()
            tambah_dosen()
        elif pilihan == '3':
            cls()
            absensi()
        elif pilihan == '4':
            print('Terima kasih\n')
            break
        else:
            print('Pilihan tidak valid')
        
        input('Tekan sembarang tombol untuk kembali...')