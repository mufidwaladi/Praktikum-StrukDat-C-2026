
def update_stok(katalog, sn_target, jumlah_tambah):
    for x in katalog:
        if x['sn'] == sn_target:
            x['stok'] = jumlah_tambah

def main():
    katalog = [ {'merk': 'Samsung', 'tipe': 'S23', 'sn': 'SAM01', 'stok':2}, 
           {'merk': 'Oppo', 'tipe': 'Reno 10', 'sn': 'OPP01', 'stok': 5} ]

    sn_target = str(input("Masukkan kode sn "))
    jumlah_tambah = int(input("Masukkan jumlah stok baru "))

    daftar_merek = {}
    daftar_merek = set(daftar_merek)
    for x in katalog:
        daftar_merek.add(x['merk'])

    update_stok(katalog, sn_target, jumlah_tambah)
    print(katalog)
    print(daftar_merek)

if __name__ == "__main__":
    main()