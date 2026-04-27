class Node:
    def __init__(self,nama):
        self.nama = nama
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_turn = None
    
    def tambah_petugas(self, nama):
        new_node = Node(nama)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            self.current_turn = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def giliran_berikutnya(self, n):
        if not self.head:
            print("Daftar Petugas Kosong")
            return
        
        for i in range(1, n + 1):
            print(f"Giliran {i}: {self.current_turn.nama}")
            self.current_turn = self.current_turn.next


urutan_valet = CircularLinkedList()
urutan_valet.tambah_petugas("Andi")
urutan_valet.tambah_petugas("Budi")
urutan_valet.tambah_petugas("Citra")
urutan_valet.tambah_petugas("Dewi")
urutan_valet.giliran_berikutnya(6)