class Laptop:
    def __init__(self, merk, model, tahun, spesifikasi, harga_beli):
        self.merk = merk
        self.model = model
        self.tahun =tahun
        self.spesifikasi =spesifikasi
        self.__harga_beli = harga_beli #atribut private tidak bisa diakses langsung

    #Getter untuk membaca harga beli karena harga beli merupakan atribut private
    def get_harga_beli(self):
        return self.__harga_beli
    
    #Setter untuk merubah harga beli menjadi harga baru namun ditambahkan method untuk me
    def set_harga_beli(self, harga_baru):
        if harga_baru > 0:
            self.__harga_beli = harga_baru
        else:
            print("Harga beli harus lebih besar daripada 0!!!")
            
    def hitung_harga_jual(self):
        return self.__harga_beli + (0.25 * self.__harga_beli)
    
    def tampil_info(self):
        print(f"Laptop : {self.merk} dengan model {self.model}")
        print(f"Tahun : {self.tahun}")
        print(f"Spesifikasi : {self.spesifikasi}")
        print(f"Harga Beli : Rp {self.get_harga_beli():,.0f}")
        print(f"Harga Jual : Rp {self.hitung_harga_jual():,.0f}")
        print(f"-" * 40)
        
laptop1 = Laptop("Asus", "Vivobook 14", 2022, "i5, 8GB RAM, 512GB SSD", 8000000)
laptop2 = Laptop("Lenovo", "Thinkpad X1", 2021, "i7, 16GB RAM, 1TB SSD", 20000000)
laptop3 = Laptop("Macbook", "Macbook pro M3", 2024, "14 inch, 512GB", 24000000)

laptop1.tampil_info()
laptop2.tampil_info()
laptop3.tampil_info()

total_beli = laptop1.get_harga_beli() + laptop2.get_harga_beli() + laptop3.get_harga_beli()
total_jual = laptop1.hitung_harga_jual() + laptop2.hitung_harga_jual() + laptop3.hitung_harga_jual()

print(f"Total Harga Beli : {total_beli}")
print(f"Total Harga Jual : {total_jual}")

print("\n== Ubah Harga Beli Laptop ==")
laptop1.set_harga_beli(8500000) #ubah harga beli laptop1
laptop1.tampil_info()

#coba ubah dengan salah harga dan harusnya muncul pesan error
laptop2.set_harga_beli(-8500000) 
