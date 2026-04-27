class Node:
    def __init__(self, data):
        self.data = data
        self.prev :Node = None
        self.next :Node = None

class DoubleLinkedList:
    def __init__(self):
        self.head : Node = None
        self.tail : Node = None

    def tambah_kendaraan(self, plat):
        current = Node(plat)
        if not self.head:
            self.head = current
            self.tail = current
        else:
            current.prev = self.tail
            self.tail.next = current
            self.tail = current 

    def tampilkan_maju(self):
        if not self.head:
            print("List kosong")
            return
        print("[Maju]")
        h = self.head
        while h:
            print(h.data)
            h = h.next

    def tampilkan_mundur(self):
        if not self.tail:
            print("List kosong")
            return
        print("\n[Mundur]")
        t = self.tail
        while t:
            print(t.data)
            t = t.prev

    def hapus_kendaraan(self,plat):
        h = self.head
        while h:
            if h.data == plat:
                break
            h = h.next
        
        if h is None:
            print("Data tidak ditemukan")
            return
        
        if h == self.head:
            self.head = h.next
            if self.head:
                self.head.prev = None
        elif h == self.tail:
            self.tail = h.next
            h.prev = h.next
        else:
            h.prev.next = h.next
            h.next.prev = h.prev
        return
    
parkir = DoubleLinkedList()
parkir.tambah_kendaraan("B 1234 ABC")
parkir.tambah_kendaraan("D 5678 XYZ")
parkir.tambah_kendaraan("A 9999 TUV") 
parkir.tampilkan_maju()
parkir.tampilkan_mundur()

print("")

parkir2 = DoubleLinkedList()
parkir2.tambah_kendaraan("B 1111 AA")
parkir2.tambah_kendaraan("D 2222 BB")
parkir2.tambah_kendaraan("A 3333 CC")
parkir2.tambah_kendaraan("B 4444 DD")
print("Sebelum:")
parkir2.tampilkan_maju()
parkir2.hapus_kendaraan("A 3333 CC")
print("\nSesudah:")
parkir2.tampilkan_maju()