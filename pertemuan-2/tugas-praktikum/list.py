thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#List bisa menampung nama yang sama

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#bekerja untuk memeriksa panjang list

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#membuat menjadi sebuah list

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#cek list dari bagian belakang

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#menampilkan list dengan diawali dari index ke 2 sampai sebelum 5

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
#mengganti value indeks 1 dan menambahkan value sebelum indeks 2
print(thislist) 


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
#menambah data dengan menggunakan indeks untuk meletakkannya pada posisi spesifik
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
#menambahkan value pada bagian akhir karena list itu berurutan
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
#menambahkan anggota suatu list ataupun objek iterable(seperti tuple) terhadap 1 list
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
#menghapus suatu value pada list
print(thislist)
#jika terdapat value yang sama maka yang di hapus adalah bagian pertama

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#menghapus value pada spesifik indeks

thislist = ["apple", "banana", "cherry"]
del thislist[0]
#menghapus value dengan menggunakan fungsi asli python
print(thislist)
#beresiko menghapus list tersebut jika tidak menggunakan indeks

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#mengosongkan value list tetapi tidak menghilangkannya

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
#contoh menggunakan perulangan for menggunakan indeks
  print(thislist[i]) 
#loop bisa digunakan untuk menampilkan setiap baik menggunakan indeks maupun tidak,bisa juga menggunakan while

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 
#contoh untuk menampilkan suatu string yang memiliki value a

ruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)
#contoh memanipulasi suatu value sebelum pengulangannya selesai

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #bisa mengurutkan dari alphabet akhir jika menggunakan (reverse = True)
#mengurutkan huruf alphabet mulai dari alphabet pertama
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#contoh pengurutan yang dicustom menggunakan sebuah fungsi

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
#contoh mengganti isi list sesuai dari urutan penulisan

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
#menyalin isi list kedalam list lain
print(mylist)
#tidak menggunakan = karna dia hanya sekedar mengikuti list tersebut sebagai referensi

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) or mylist = thislist[:]
print(mylist) 
#bisa juga menggunakan metode diantara 2 ini

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
#join list bisa menggunakan metode + atau pun metode append dan extend

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
#mengitung jumlah isi list yang memiliki nilai yang sama bisa juga digunakan oleh tuple