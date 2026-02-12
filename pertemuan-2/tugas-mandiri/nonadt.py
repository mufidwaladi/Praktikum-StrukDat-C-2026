# Data disimpan dalam list biasa
keranjang = []

# Menambah item manual
keranjang.append({"nama": "Kopi", "harga": 5000})
keranjang.append({"nama": "Roti", "harga": 3000})

# Menghitung total manual
total = 0
for item in keranjang:
    total += item["harga"]

print(f"Total bayar belanjaan adalah: {total}")