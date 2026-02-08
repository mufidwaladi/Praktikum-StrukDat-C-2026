thisset = {"apple", "banana", "cherry", False, True, 0}
#false dan 0 adalah sama
print(thisset)
#isi set tidak bisa diubah,tidak berurutan,dan tidak boleh duplikat

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
#set tidak bisa di akses melalui indeks

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 
#isi set tidak bisa diubah tetapi bisa di tambah

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset) 
#menambahkan isi set dengan list(bisa juga set,tuples dan dictionary)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")
#contoh menghapus value sebuah set
print(thisset) 
#bisa juga menggunakan remove tetapi jika tidak di temukan maka dia aka error

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#menggunakan loop

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z) 
#menggabung set dan tuple(tetapi bisa juga menggabung sesama set)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset) 
#menggabungkan set pada set

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#menambah isi set dan mengganti set original

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) 
#menyimpan sebagai set baru dan hanya meyimpan value yang sama

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1) 
#menyimpan sebagai set baru dan hanya meyimpan value yang sama dan mengganti isi set tersebut

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) #bisa menggunakan set1 - set2

print(set3) 
#menyimpan value set pertama yang tidak sama dengan set ke 2

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3) 
#menyimpan semua value yang tidak memiliki kesamaan

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#versi set yang tidak dapat diubah
