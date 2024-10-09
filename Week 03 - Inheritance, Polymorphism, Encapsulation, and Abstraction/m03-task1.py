from abc import ABC, abstractmethod

class Kampus(ABC):
    def nomor_induk(self):
        pass

    def nama(self):
        pass

    @abstractmethod
    def absensi(self):
        pass

class Mikroskil:
    def __init__(self, nomor_induk, nama):
        self.nomor_induk = nomor_induk
        self.nama = nama

class Dosen(Mikroskil, Kampus):
    def __init__(self, nomor_induk, nama):
        super().__init__(nomor_induk, nama)
    
    def absensi(self):
        print(f"Selamat datang, {self.nama}. Silakan memulai pelajaran.")

class Mahasiswa(Mikroskil, Kampus):
    def __init__(self, nomor_induk, nama):
        super().__init__(nomor_induk, nama)
    
    def absensi(self):
        print(f"Terima kasih atas kehadiran Anda, {self.nama}.")

dosen = Dosen("1234567890", "Kelvin")
mahasiswa = Mahasiswa("231111684", "Evelyn")

dosen.absensi()
mahasiswa.absensi()