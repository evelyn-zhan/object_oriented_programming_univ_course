import os

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

class KelasA:
    def __init__(self):
        self.nama = 'Kelas A'
        self.daftar_mahasiswa = []
    
    def ruang(self): return 'T1/L2'

    def mata_kuliah(self): return 'Kalkulus'

    def deskripsi(self): return 'Belajar mengenai perhitungan kalkulus dan berbagai proses yang ada.'

class KelasB:
    def __init__(self):
        self.nama = 'Kelas B'
        self.daftar_mahasiswa = []
    
    def ruang(self): return 'T3/L2'

    def mata_kuliah(self): return 'Pemrograman'

    def deskripsi(self): return 'Belajar mengenai pemrograman beserta proses-proses dalam pemrograman.'

class KelasC:
    def __init__(self):
        self.nama = 'Kelas C'
        self.daftar_mahasiswa = []
    
    def ruang(self): return 'T5/L2'

    def mata_kuliah(self): return 'Bahasa Inggris'

    def deskripsi(self): return 'Belajar mengenai formula-formula yang dibutuhkan untuk merangkai kata-kata dalam Bahasa Inggris.'

class Adapter:
    def __init__(self, kelas, *informasi):
        self.kelas = kelas
        self.informasi = informasi
    
    def cetak_informasi(self):
        print(self.kelas.nama)

        for info in self.informasi:
            print(f'{info.title()}: {getattr(self.kelas, info)()}')
        
        if len(self.kelas.daftar_mahasiswa) == 0:
            print('Belum ada data mahasiswa.')
        else:
            print('Daftar mahasiswa:')
            for mahasiswa in self.kelas.daftar_mahasiswa:
                print(mahasiswa)

class Mahasiswa:
    def __init__(self, nim, nama, jenis_kelamin, hp):
        self.nim = nim
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.hp = hp
    
    def __str__(self):
        return str(self.__dict__)

def tambah_data():
    print(f'{'TAMBAH DATA MAHASISWA':^50}')
    print('-' * 50)

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
    
    valid = False

    while valid == False:
        kelas = input('Masukkan kelas (A/B/C): ').upper()

        try:
            if kelas == '':
                raise ValueError('Kelas tidak boleh kosong.')
            
            if kelas not in ['A', 'B', 'C']:
                raise ValueError('Kelas hanya boleh berupa A, B, atau C.')
            
            valid = True
        
        except ValueError as e:
            print(str(e))
    
    mahasiswa = Mahasiswa(nim, nama, jenis_kelamin, hp)

    if kelas == 'A':
        kelasA.daftar_mahasiswa.append(mahasiswa)
    elif kelas == 'B':
        kelasB.daftar_mahasiswa.append(mahasiswa)
    elif kelas == 'C':
        kelasC.daftar_mahasiswa.append(mahasiswa)
    
    print('-' * 50)
    print('Data mahasiswa berhasil ditambahkan.')

def cetak_informasi(kelasA, kelasB, kelasC):
    print(f'{'INFORMASI KELAS':^50}')
    print('-' * 50)

    kelasA.cetak_informasi()
    print('-' * 50)
    kelasB.cetak_informasi()
    print('-' * 50)
    kelasC.cetak_informasi()
    print('-' * 50)

if __name__ == '__main__':
    kelasA = KelasA()
    kelasB = KelasB()
    kelasC = KelasC()

    adapterKelasA = Adapter(kelasA, 'ruang', 'mata_kuliah', 'deskripsi')
    adapterKelasB = Adapter(kelasB, 'ruang', 'mata_kuliah', 'deskripsi')
    adapterKelasC = Adapter(kelasC, 'ruang', 'mata_kuliah', 'deskripsi')

    while True:
        cls()

        print(f'{'ABSENSI KELAS':^50}')
        print('-' * 50)
        print('1. Tambah data mahasiswa')
        print('2. Cetak informasi kelas')
        print('3. Keluar')
        print('-' * 50)

        pilihan = input('Pilih menu (1/2/3): ')

        if pilihan in ['1', '2']: cls()

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            cetak_informasi(adapterKelasA, adapterKelasB, adapterKelasC)
        elif pilihan == '3':
            print('Terima kasih\n')
            break
        else:
            print('Pilihan tidak valid')
    
        input('Tekan sembarang tombol untuk kembali...')