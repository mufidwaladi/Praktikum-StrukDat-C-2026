class KeranjangBelanja:
    def __init__(self):
        self.__items = []

    def tambah_barang(self, barang, harga):
        item = {"barang": barang, "harga": harga}
        self.__items.append(item)

    def hitung_total(self):
        return sum(item["harga"] for item in self.__items)

# Penggunaan
keranjang = KeranjangBelanja()
keranjang.tambah_barang("Kopi", 5000)
keranjang.tambah_barang("Roti", 3000)

print(f"Total bayar belanjaan adalah : {keranjang.hitung_total()}")