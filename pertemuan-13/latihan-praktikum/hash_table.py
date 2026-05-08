class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]
    
    def hash_function(self, key):
        total = 0

        # Jumlahkan Unicode tiap karakter
        for char in str(key):
            total += ord(char)

        return total % self.size
    
    def insert(self , kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i , (k,v) in enumerate(bucket):

            if k == kode:

                # Update value lama
                bucket[i] = (kode, judul)

                print(f"Data dengan kode : '{kode}' berhasil di-update")
                return
        bucket.append((kode, judul))

        print(f"Data '{kode}:{judul}' berhasil ditambahkan")
    
    def search(self,kode):
        # Cari index bucket
        index = self.hash_function(kode)

        # Ambil bucket
        bucket = self.table[index]

        # Cari key di bucket
        for k, v in bucket:

            if k == kode:
                print(f"Judul bukunya adalah : {v}")
                return v
        
        print("Buku tidak ditemukan")
        return None

    def delete(self, kode):
        # Cari index bucket
        index = self.hash_function(kode)

        # Ambil bucket
        bucket = self.table[index]

        # Cari posisi data
        for i, (k, v) in enumerate(bucket):

            if k == kode:

                # Hapus data
                del bucket[i]

                print(f"Data dengan key '{kode}' berhasil dihapus")
                return True

        # Jika key tidak ditemukan
        print(f"Key '{kode}' tidak ditemukan")
        return False

    
    def display(self):

        print("\n===== ISI HASH TABLE =====")

        for index, bucket in enumerate(self.table):
            print(f"Index {index}: {bucket}")

        print("==========================\n")

lib = HashTable()


lib.insert("BK111", "Mahir C++ Dalam Satu Jam")
lib.insert("BK222", "Python Dasar")
lib.insert("BK333", "Matematika Diskrit")
lib.insert("BK444", "Atomic Habits")

lib.display()


lib.insert("BK045", "Mein Kampf")
lib.insert("BK111", "Bumi Manusia") # Update judul kode BK111 

lib.display()

lib.search("BK222")
lib.search("BK999") # Mencari buku yang tidak ada

lib.delete("BK333")

lib.display()