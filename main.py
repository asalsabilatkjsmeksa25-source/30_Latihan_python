def ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


def prima(angka):
    if angka < 2:
        return False

    for i in range(2, angka):
        if angka % i == 0:
            return False

    return True


angka = int(input("Masukkan bilangan: "))

print("Bilangan:", ganjil_genap(angka))

if prima(angka):
    print("Bilangan Prima")
else:
    print("Bukan Bilangan Prima")
