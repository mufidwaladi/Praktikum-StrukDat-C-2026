import soal1,soal2,soal3,soal4,soal5

def main():
    try:    
        inventaris = []
        skema_komisi = (
        (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
        (50000000, 5), # Penjualan >= 50jt -> Komisi 5%
        (20000000, 2), # Penjualan >= 20jt -> Komisi 2%
        (0, 0) # Di bawah 20jt -> Tidak ada komisi
        )
        while True:
            print("=== PyGadget Hub ===")
            print("1. Tambah Gadget")
            print("2. Daftar Inventaris")
            print("3. Update Stok")
            print("4. Cek Komisi")
            print("5. Keluar")

            pilih = input("Masukkan opsi yang ingin di pilih")
            match pilih:
                case "1":
                    merk = input("Masukkan merek gadget")
                    tipe = input("Masukkan type gadget")
                    harga = int(input("Masukkkan harga barang"))
                    sn = input("Masukkan nomor serial")
                    sementara = soal1.registrasi_gadget(merk, tipe, harga, sn)
                    inventaris = inventaris.append(sementara)


                case "2":
                    min_harga = int(input("Masukkkan harga minimum barang"))
                    max_harga = int(input("Masukkkan harga maximum barang"))
                    hasil = soal2.rentang_harga(inventaris, min_harga, max_harga)
                    if len(hasil) > 0:
                        for x in hasil:
                            print(f"merek = {x['merk']}")
                            print(f"tipe = {x['tipe']}")
                            print(f"harga = {x['harga']}")
                            print(f"serial number = {x['sn']}")
                            print(f"status = {x['status']}")
                case "3":
                    sn_target = str(input("Masukkan kode sn "))
                    jumlah_tambah = int(input("Masukkan jumlah stok baru "))
                    soal3.update_stok(inventaris, sn_target, jumlah_tambah)
                case "4":
                    sales = input("Masukkan nama sales ")
                    total_penjualan = int(input("Masukkan total penjualan"))
                    persen = soal4.hitung_komisi(total_penjualan,skema_komisi)
                    total_komisi = (total_penjualan * persen / 100)
                    print(f"Nama sales {sales}\nhasil komisi : Rp.{total_komisi}")
                    soal4.hitung_komisi(total_penjualan,skema_komisi,index=0)
                case _ :
                    break
    except:
        print("Aduh ada yang salah")

    

if __name__ == "__main__":
     main()