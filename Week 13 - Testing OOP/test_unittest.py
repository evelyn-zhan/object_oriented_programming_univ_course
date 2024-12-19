import unittest
from m13task1 import DaftarMahasiswa, DaftarDosen, Mahasiswa, Dosen

df_mhs = DaftarMahasiswa()
df_dsn = DaftarDosen()

df_mhs.tambah(Mahasiswa('231111684', 'Evelyn', 'Perempuan', '08123456789', 'Teknik Informatika'))

class test_program(unittest.TestCase):
    def test_jumlah(self):
        self.assertEqual(df_mhs.jumlah(), 1)
    
    def test_data(self):
        self.assertEqual(df_mhs.isi[0].nim, '231111684')
    
    def test_salah(self):
        self.assertEqual(df_dsn.jumlah(), 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)