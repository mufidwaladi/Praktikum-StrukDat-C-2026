class Node:
    def __init__(self,nama,keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None

class QuequeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def isEmpty(self):
        if self.head is None:
            print("Antrian kosong \n")
        else:
            print("Antrian Tidak Kosong")
    
    def enqueque(self,nama,keluhan):
        new_node = Node(nama,keluhan)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._count += 1
        print(f"menambah antrian {nama} \n")
    
    def dequeque(self):
        if self.isEmpty():
            print("Antrian Kosong sehingga tidak ada yang bisa dihapus \n")
        
        nama_pasien = self.head.nama
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._count -= 1

        return nama_pasien
    
    def peek(self):
        if self.isEmpty():
            print("Queque Kosong")
        print(f"nama pasien {self.head.nama} , keluhan {self.head.keluhan} \n")
    
    def info(self):
        print(f"Jumlah pasien Mengantri {self._count} \n")

    def clear(self):
        self.head = self.tail = None
        print("sesi selesai antrian dikosongkan")

    def traversal(self):
        if self.head is None:
            return "IssEmptyinya kosong"
        curr = self.head

        while curr:
            print(f"nama pasien {curr.nama} , keluhan {curr.keluhan}")
            curr = curr.next


def main():
    Rumah_sakit = QuequeLinkedList()
    Rumah_sakit.isEmpty()
    Rumah_sakit.enqueque("Budi", "demam tinggi")
    Rumah_sakit.enqueque("Ani", "batuk pilek")
    Rumah_sakit.enqueque("Citra", "sakit kepala")
    Rumah_sakit.info()
    Rumah_sakit.peek()
    Rumah_sakit.dequeque()
    Rumah_sakit.enqueque("Dodi", "nyeri perut")
    Rumah_sakit.traversal()
    Rumah_sakit.dequeque()
    Rumah_sakit.info()
    Rumah_sakit.traversal()
    Rumah_sakit.clear()
    Rumah_sakit.isEmpty()

if __name__ == "__main__":
    main()  