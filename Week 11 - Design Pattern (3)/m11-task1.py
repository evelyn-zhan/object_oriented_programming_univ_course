class KelasA:
    def __init__(self):
        self.nama = 'Kelas A'
    
    def ruang(self): return 'T1/L2'

    def mata_kuliah(self): return 'Kalkulus'

    def deskripsi(self): return 'Belajar mengenai perhitungan kalkulus dan berbagai proses yang ada.'

class KelasB:
    def __init__(self):
        self.nama = 'Kelas B'
    
    def ruang(self): return 'T3/L2'

    def mata_kuliah(self): return 'Pemrograman'

    def deskripsi(self): return 'Belajar mengenai pemrograman beserta proses-proses dalam pemrograman.'

class KelasC:
    def __init__(self):
        self.nama = 'Kelas C'
    
    def ruang(self): return 'T5/L2'

    def mata_kuliah(self): return 'Bahasa Inggris'

    def deskripsi(self): return 'Belajar mengenai formula-formula yang dibutuhkan untuk merangkai kata-kata dalam Bahasa Inggris.'

class Adapter:
    def __init__(self, kelas, *informasi):
        self.kelas = kelas
        self.informasi = informasi
        # print(self.informasi)
    
    def cetak_informasi(self):
        print(self.kelas.nama)
        for info in self.informasi:
            print(f'{info.title()}: {getattr(self.kelas, info)()}')

if __name__ == '__main__':
    kelasA = KelasA()
    kelasB = KelasB()
    kelasC = KelasC()

    print()

    adapterKelasA = Adapter(kelasA, 'ruang', 'mata_kuliah', 'deskripsi')
    adapterKelasA.cetak_informasi()

    print('-' * 50)

    adapterKelasB = Adapter(kelasB, 'ruang', 'mata_kuliah', 'deskripsi')
    adapterKelasB.cetak_informasi()

    print('-' * 50)

    adapterKelasC = Adapter(kelasC, 'ruang', 'mata_kuliah', 'deskripsi')
    adapterKelasC.cetak_informasi()

    print()