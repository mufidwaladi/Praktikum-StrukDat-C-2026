

def hitung_komisi(total_penjualan, skema, index=0):
        if total_penjualan >= skema[index][1]:
            return skema[index][1]
        else:
            x += 1

def main():
    skema_komisi = (
    (100000000, 10), # Penjualan >= 100jt -> Komisi 10%
    (50000000, 5), # Penjualan >= 50jt -> Komisi 5%
    (20000000, 2), # Penjualan >= 20jt -> Komisi 2%
    (0, 0) # Di bawah 20jt -> Tidak ada komisi
    )
    sales = input("Masukkan nama sales ")
    total_penjualan = int(input("Masukkan total penjualan"))
    persen = hitung_komisi(total_penjualan,skema_komisi)
    total_komisi = (total_penjualan * persen / 100)
    print(f"Nama sales {sales}\nhasil komisi : Rp.{total_komisi}")


if __name__ == "__main__":
     main()