import pytest
from m13task1 import DaftarMahasiswa, DaftarDosen, Mahasiswa, Dosen

@pytest.fixture
def data(request):
    df_mhs = DaftarMahasiswa()
    df_dsn = DaftarDosen()

    mhs1 = Mahasiswa('231111684', 'Evelyn', 'Perempuan', '08123456789', 'Teknik Informatika')
    df_mhs.tambah(mhs1)
    
    return df_mhs, df_dsn

def test_jumlah_mhs(data):
    df_mhs, df_dsn = data
    assert df_mhs.jumlah() == 1

def test_data_mhs(data):
    df_mhs, df_dsn = data
    assert df_mhs.isi[0].nim == '231111684'

def test_jumlah_dsn(data):
    df_mhs, df_dsn = data
    assert df_dsn.jumlah() == 2