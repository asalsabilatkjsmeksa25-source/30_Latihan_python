import Database

Database.buat_database()

def ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
     
print("==============================")
print("       PROGRAM DATA ASA")
print("==============================")

nama = "Asa"
angka = int(input("Masukkan angka: "))

hasil = ganjil_genap(angka)

print("\nHasil:")
print("Nama  :", nama)
print("Angka :", angka)
print("Hasil :", hasil)

Database.simpan_data(nama, angka, hasil)

print("\nData berhasil disimpan!")

pilihan = input("Apakah Anda ingin memasukkan angka lagi? (y/n): ")
if pilihan.lower() == "y": 
    def jalankan_program():
        while True:
            angka = int(input("Masukkan angka: "))
            hasil = ganjil_genap(angka)
            print(f"Hasil: {hasil}")
            Database.simpan_data(nama, angka, hasil)
            pilihan = input("Apakah Anda ingin memasukkan angka lagi? (y/n): ")
            if pilihan.lower() != "y":
                break
else:
    print("Terima kasih! Program selesai.")
    
print("\n=== DATA DATABASE ===")

data = Database.tampilkan_data()

for row in data:
    print(row)



def prima(angka):
    if angka < 2:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True
