import sqlite3

def buat_database():
    conn = sqlite3.connect("data_asa.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hasil (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            angka INTEGER,
            hasil TEXT
        )
    """)

    conn.commit()
    conn.close()


def simpan_data(nama, angka, hasil):
    conn = sqlite3.connect("data_asa.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO hasil (nama, angka, hasil) VALUES (?, ?, ?)",
        (nama, angka, hasil)
    )

    conn.commit()
    conn.close()


def tampilkan_data():
    conn = sqlite3.connect("data_asa.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM hasil")
    data = cursor.fetchall()

    conn.close()
    return data