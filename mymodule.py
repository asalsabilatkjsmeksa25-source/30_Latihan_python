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