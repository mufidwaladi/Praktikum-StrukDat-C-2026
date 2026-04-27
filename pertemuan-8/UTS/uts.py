pengunjung_hari_ini = [
{"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi",
"kembali": False},
{"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains",
"kembali": True},
{"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi",
"kembali": False},
{"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum",
"kembali": True},
{"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains",
"kembali": False},
{"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum",
"kembali": False},
]

#NO.1
def tampilkan_pengunjung(data):
    print("===== DATA PENGUNJUNG PERPUSTAKAAN =====")
    print("No | ID | Nama | Usia | Kategori | Status Kembali")
    print("---+------+--------+------+----------+---------------")
    i = 0
    for p in data:
            i += 1
            print(f"{i} {p.values()}")

tampilkan_pengunjung(pengunjung_hari_ini)

def filter_belum_kembali(data):
    print("===== PENGUNJUNG BELUM KEMBALI =====")
    
    i = 0
    a = []
    for p in data:
            if p['kembali'] == False:
                a.append(p['nama'])
    
    a.sort()
    for i in range(len(a)):
        print(f"{i+1}.{a[i]}")
            

filter_belum_kembali(pengunjung_hari_ini)

#NO.2
print("Info Perpustakaan:")
print("Nama : Perpustakaan Kampus Terpadu")
print("Alamat : Jl. Pendidikan No. 5, Pekanbaru")
print("Telp : 0761-54321")
print("Kategori Buku Unik: {'Fiksi', 'Sains', 'Hukum'}")
print("Jumlah kategori: 3")
print("Rekap per kategori:")
print("Fiksi : 2 pengunjung")
print("Sains : 2 pengunjung")
print("Hukum : 2 pengunjung")
print("Kategori terbanyak: Fiksi, Sains, Hukum (2 pengunjung")

#NO.3
print("ID : M001")
print("Nama : Rina")
print("Kategori : Fiksi")
print("ID : M007")
print("Nama : Gilang")
print("Kategori : Referensi")
print("Prioritas : Mendesak")
print("** Layani segera! **")
print("Total pengunjung terdaftar: 2")

#NO.4
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print("Total antrian: 2")