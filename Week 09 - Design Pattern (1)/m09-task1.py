import os

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

class Wrapper:
    def __init__(self, kode, nama, jenis_kelamin, hp):
        self.kode = kode
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.hp = hp

class Mahasiswa:
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def data_tambahan(self, jurusan):
        self.jurusan = jurusan

class Dosen:
    def __init__(self, wrapper):
        self.wrapper = wrapper
    
    def data_tambahan(self, jabatan):
        self.jabatan = jabatan

class Absensi:
    def __init__(self, orang):
        self.orang = orang
        self.data = {}

        for key, value in self.orang.wrapper.__dict__.items():
            self.data[key] = value
        
        if self.orang is Mahasiswa:
            self.data['jurusan'] = self.orang.jurusan
        
        if self.orang is Dosen:
            self.data['jabatan'] = self.orang.jabatan
        
    def __repr__(self):
        return str(self.data)

daftar_mahasiswa = []
daftar_dosen = []

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
            nama.title()
        
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
    
    mahasiswa = Mahasiswa(Wrapper(nim, nama, jenis_kelamin, hp))
    mahasiswa.data_tambahan(jurusan)
    daftar_mahasiswa.append(mahasiswa)

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
            nama.title()
        
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

    dosen = Dosen(Wrapper(nip, nama, jenis_kelamin, hp))
    dosen.data_tambahan(jabatan)
    daftar_dosen.append(dosen)

def absensi():
    print(f'{'ABSENSI':^80}')
    print('-' * 80)

    print('Daftar mahasiswa:')
    if len(daftar_mahasiswa) == 0:
        print('Belum ada data mahasiswa.')
    else:
        print(f'Terdapat {len(daftar_mahasiswa)} orang mahasiswa.')
        for mahasiswa in daftar_mahasiswa:
            print(Absensi(mahasiswa))
    
    print('-' * 80)

    print('Daftar dosen:')
    if len(daftar_dosen) == 0:
        print('Belum ada data dosen.')
    else:
        print(f'Terdapat {len(daftar_dosen)} orang dosen.')
        for dosen in daftar_dosen:
            print(Absensi(dosen))
    
    print('-' * 80)

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