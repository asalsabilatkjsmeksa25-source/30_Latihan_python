def cek_ganjil_genap():
    while True:
        teks = input('Masukkan angka (atau ketik "keluar" untuk berhenti): ')
        
        if teks.lower() == 'keluar':
            print("Program selesai. Terima kasih!")
            break
            
        try:
            x = int(teks)
            print(f'angka {x} adalah genap') if x % 2 == 0 else print(f'angka {x} adalah ganjil')
        except ValueError:
            print("Input tidak valid! Harap masukkan angka bulat.")


