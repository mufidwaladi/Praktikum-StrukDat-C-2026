#tuple bisa valuenya tidak bisa diganti dan berurutan,indeksnya dimulai dari 0,bisa duplikat
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#perbedaan tuple dan string

#untuk mengakses sama seperti list
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#contoh mengakses tuple dari indeks 0 sampai sebelum 4

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#cara mengubah tuple adalah dengan mengubahnya menjadi list terlebih dahulu

"""thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#del bisa menghapus tuple sepenuhnya"""

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits
#* berguna menyimpan sisa data yang ada kecuali jika ada suatu pembatas
print(green)
print(tropic)
print(red)
#contoh mengekstrak tuple

thistuple = ("apple", "banana", "cherry")
i = 0
while i < thistuple:
  print(thistuple[i])
  i = i + 1 
#contoh penggunaan loop sama seperti list bisa menggunakan indeks ataupun tidak