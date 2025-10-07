#Superclass
class Kendaraan:
    def __init__(self, merk, tahun):
        self.merk = merk
        self.tahun = tahun
        
    def info(self):
        print(f"Merk : {self.merk}, Tahun : {self.tahun}")
        
    def bergerak(self):
        print('Mobil bergerak di jalan raya')
        
class Motor(Kendaraan):
    def __init__(self, merk, tahun, jenis):
        super().__init__(merk, tahun)
        self.jenis = jenis
        
    def info(self):
        super().info()
        print(f"jenis motor : {self.jenis}")
        
    def bergerak(self): #override method
        print("Motor melaju dengan cepat")
    
class Mobil(Kendaraan):
    def __init__(self, merk, tahun, jumlah_pintu):
        super().__init__(merk, tahun)
        self.jumlah_pintu = jumlah_pintu
    
    def info(self):
        super().info()
        print(f"Jumlah Pintu : {self.jumlah_pintu}")
        
    def bergerak(self): #override method
        print("Mobil melaju dengan cepat")
        

mobil1 = Mobil("Toyota", 2020, 4)
motor1 = Motor("Honda", 2021, "Matic")

mobil1.info()
mobil1.bergerak()

print("-" * 40)

motor1.info()
motor1.bergerak()