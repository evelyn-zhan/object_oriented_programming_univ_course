import os

def cls(): os.system('cls' if os.name == 'nt' else 'clear')

class CompositeElement:
    def __init__(self, nama, biaya=''):
        self.nama = nama
        self.biaya = biaya
        self.subBiaya = []
    
    def tambah(self, biaya):
        self.subBiaya.append(biaya)
    
    def lihatDetail(self):
        print(self.nama, end='')
        if self.biaya != '': print(f'\t: Rp {self.biaya}')
        else: print()
        for biaya in self.subBiaya:
            print('\t', end='')
            biaya.lihatDetail()

class LeafElement:
    def __init__(self, nama, biaya):
        self.nama = nama
        self.biaya = biaya
    
    def lihatDetail(self):
        print(f'{self.nama}\t: Rp {self.biaya}')

class Mahasiswa:
    def __init__(self, nama, jenisKelamin, HP, jurusan):
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.HP = HP
        self.jurusan = jurusan
        self.statusPembayaran = False
    
    def bayar(self):
        if self.statusPembayaran == False:
            self.statusPembayaran = True
            print('Biaya Pendaftaran berhasil dibayar!')
            return
        
        print('Biaya Pendaftaran sudah pernah dibayar! Tidak bisa membayar ulang.')
        return

daftarMahasiswa = []

def detailBiaya():
    print('-' * 80)
    print(f'{'RINCIAN BIAYA PENDAFTARAN':^80}')
    print('-' * 80)

    UangPendaftaran = CompositeElement('Uang Pendaftaran', 200000)
    UangKuliahPertama = CompositeElement('Uang Kuliah Pertama', 1500000)
    UangMPT = CompositeElement('Uang MPT')

    UangTraining = LeafElement('Uang Training', 100000)
    UangPenginapan = LeafElement('Uang Penginapan', 200000)
    UangKonsumsi = LeafElement('Uang Konsumsi', 150000)

    UangMPT.tambah(UangTraining)
    UangMPT.tambah(UangPenginapan)
    UangMPT.tambah(UangKonsumsi)

    UangPendaftaran.lihatDetail()
    UangKuliahPertama.lihatDetail()
    UangMPT.lihatDetail()

    print('-' * 80)

def pendaftaran():
    print('-' * 80)
    print(f'{'PENDAFTARAN MAHASISWA BARU':^80}')
    print('-' * 80)

    valid = False

    while valid == False:
        nama = input('Masukkan nama: ').lower()

        try:
            if nama == '': raise ValueError('Nama tidak boleh kosong.')
            
            spasi = 0
            
            for karakter in nama:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ': raise ValueError('Nama hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter == ' ': spasi += 1
            
            if spasi == len(nama): raise ValueError('Nama tidak boleh kosong.')

            valid = True
            nama = nama.title()
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        jenis_kelamin = input('Masukkan jenis kelamin (L/P): ').upper()

        try:
            if jenis_kelamin == '': raise ValueError('Jenis kelamin tidak boleh kosong.')

            if jenis_kelamin not in ['L', 'P']: raise ValueError('Jenis kelamin hanya boleh berupa L atau P.')

            valid = True
            jenis_kelamin = 'Laki-laki' if jenis_kelamin == 'L' else 'Perempuan'
        
        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        hp = input('Masukkan nomor HP: ')

        try:
            if hp == '': raise ValueError('Nomor HP tidak boleh kosong.')
            
            for karakter in hp:
                if karakter not in '0123456789+': raise ValueError("Nomor HP hanya boleh terdiri dari angka atau tanda '+' saja.")
            
            if len(hp) < 8 or len(hp) > 15: raise ValueError('Nomor HP hanya boleh terdiri dari 8 - 15 angka saja.')

            valid = True

        except ValueError as e:
            print(str(e))
    
    valid = False

    while valid == False:
        jurusan = input('Masukkan jurusan (IF/SI/TI/AK/MN): ').lower()

        try:
            if jurusan == '': raise ValueError('Jurusan tidak boleh kosong.')
            
            spasi = 0
            
            for karakter in jurusan:
                if karakter not in 'abcdefghijklmnopqrstuvwxyz ': raise ValueError('Jurusan hanya boleh terdiri dari huruf dan spasi saja.')
                if karakter == ' ': spasi += 1
            
            if spasi == len(jurusan): raise ValueError('Jurusan tidak boleh kosong.')

            if jurusan not in ['if', 'si', 'ti', 'ak', 'mn']: raise ValueError('Jurusan hanya boleh berupa IF, SI, TI, AK, atau MN.')

            valid = True
            
            if jurusan == 'if': jurusan = 'Teknik Informatika'
            elif jurusan == 'si': jurusan = 'Sistem Informasi'
            elif jurusan == 'ti': jurusan = 'Teknologi Informasi'
            elif jurusan == 'ak': jurusan = 'Akuntansi'
            elif jurusan == 'mn': jurusan = 'Manajemen'

        except ValueError as e:
            print(str(e))
    
    mahasiswaBaru = Mahasiswa(nama, jenis_kelamin, hp, jurusan)
    daftarMahasiswa.append(mahasiswaBaru)

    print('-' * 80)
    print('Mahasiswa baru berhasil didaftarkan!')

def lihatDaftar():
    print('-' * 80)
    print(f'{'DAFTAR MAHASISWA BARU':^80}')
    print('-' * 80)

    if len(daftarMahasiswa) == 0:
        print('Belum ada data mahasiswa baru.')
    else:
        for mahasiswa in daftarMahasiswa:
            print(mahasiswa.__dict__)
    
    print('-' * 80)

def statusPembayaran():
    print('-' * 80)
    print(f'{'STATUS PEMBAYARAN':^80}')
    print('-' * 80)

    if len(daftarMahasiswa) == 0:
        print('Belum ada data mahasiswa baru.')
    else:
        idx = 0
        for mahasiswa in daftarMahasiswa:
            idx += 1
            print(idx, end='. ')
            print(mahasiswa.__dict__)
    
    print('-' * 80)

    valid = False

    while valid == False:
        nomor = input('Masukkan nomor mahasiswa yang membayar biaya pendaftaran: ')

        try:
            if nomor == '': raise ValueError('Nomor tidak boleh kosong.')

            for karakter in nomor:
                if karakter not in '0123456789': raise ValueError('Nomor hanya boleh terdiri dari angka saja.')

            nomor = int(nomor)
            if nomor < 1 or nomor > len(daftarMahasiswa): raise ValueError('Nomor mahasiswa tidak valid.')

            valid = True
            nomor -= 1
        
        except ValueError as e:
            print(str(e))
    
    print('-' * 80)
    
    daftarMahasiswa[nomor].bayar()

    print('-' * 80)

if __name__ == '__main__':
    while True:
        cls()

        print('-' * 80)
        print(f'{'PENDAFTARAN MAHASISWA BARU':^80}')
        print('-' * 80)

        print('1. Lihat Rincian Biaya Pendaftaran')
        print('2. Pendaftaran Mahasiswa Baru')
        print('3. Daftar Mahasiswa Baru')
        print('4. Status Pembayaran')
        print('5. Keluar')

        print('-' * 80)

        pilihan = input('Pilih menu (1/2/3/4/5): ')

        if pilihan in ['1', '2', '3', '4']: cls()

        if pilihan == '1':
            detailBiaya()
        elif pilihan == '2':
            pendaftaran()
        elif pilihan == '3':
            lihatDaftar()
        elif pilihan == '4':
            statusPembayaran()
        elif pilihan == '5':
            print('Terima kasih\n')
            break
        else:
            print('Pilihan tidak valid!')

        input('Tekan sembarang tombol untuk kembali...')