stok = [15, 50, 30, 25, 40]
stok.append(100)
stok.insert(2, 75)
stok.sort(reverse = True)

rata2 = 0
jumlah = 0
for x in stok:
    jumlah += x

y = len(stok)

rata2 = jumlah / y

print(f"Jumlahnya adalah {rata2}")
