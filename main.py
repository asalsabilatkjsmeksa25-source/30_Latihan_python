from Database import buat_database

buat_database()

while True:
    print("==============================")
    print("       PROGRAM DATA ASA TKJ")
    print("==============================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Pilih menu (1/2/3): ")

    if choice == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        print("Registrasi berhasil!")

    elif choice == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        if username == "Asa" and password == "Asa123":
            print("Login berhasil!")
            break
        else:
            print("Username atau password salah!")

    elif choice == "3":
        print("Terima kasih! Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
