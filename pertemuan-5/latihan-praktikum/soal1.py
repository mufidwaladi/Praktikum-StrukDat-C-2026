stok_barang = [15, 40, 30, 10, 25]
#A
stok_barang[stok_barang.index(10)] = 50



#B
stok_barang.append(5)
stok_barang.sort(reverse=True)

#C
print(stok_barang)

#D
rata_rata = sum(stok_barang)/len(stok_barang)
rata_rata = print("Stok aman")if rata_rata > 20 in stok_barang else print("Waspada")