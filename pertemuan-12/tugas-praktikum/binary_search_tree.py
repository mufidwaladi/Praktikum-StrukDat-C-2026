class Node:
    def __init__(self,id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
        else:
            currentNode = self.root
            self.ubahNode(currentNode, id_buku, judul)


    def ubahNode(self, current_node, id_buku_baru, judul_baru):
        if current_node.id_buku > id_buku_baru:
            if current_node.left is None:
                current_node.left = Node(id_buku_baru,judul_baru)
            else:
                self.ubahNode(current_node.left, id_buku_baru, judul_baru)

        elif current_node.id_buku < id_buku_baru:
            if current_node.right is None:
                current_node.right = Node(id_buku_baru,judul_baru)
            else:
                self.ubahNode(current_node.right, id_buku_baru, judul_baru)



    def search(self, id_buku):
        if self.root is None:
            print("Buku tidak ditemukan")
            return
        
        current_node = self.root       
        self.cari(current_node, id_buku)


    def cari(self, current_node, id_buku):
        if current_node:
            if current_node.id_buku == id_buku:
                print(f"[SEARCH] Mencari ID {id_buku}... Ditemukan! Judul: {current_node.judul}")
                return
            elif id_buku < current_node.id_buku:
                self.cari(current_node.left,id_buku)
                return

            elif id_buku > current_node.id_buku:
                self.cari(current_node.right,id_buku)
                return
        
        print(f"[SEARCH] Mencari ID {id_buku}... Data tidak ditemukan")
        return

    def traversal_inorder(self, node):
        if node is not None:
            self.traversal_inorder(node.left)
            print(node.id_buku,"-", node.judul)
            self.traversal_inorder(node.right)

    def get_min(self, node):
        if node is None:
            return
        
        curr = node
        while curr.left:
            curr = curr.left
        
        return curr
        

    def get_max(self, node):
        if node is None:
            return
        
        curr = node
        while curr.right:
            curr = curr.right
        
        return curr
        
    def height(self, node):
        if node is None:
            return -1
        
        hi_left = self.height(node.left)
        hi_right = self.height(node.right)

        return max(hi_left, hi_right) + 1
            
            
def main():
    perpustakaan = BST()
    
    print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
    print("===")
    
    data_buku = [
        (50, "Dasar Pemrograman"),
        (30, "Struktur Data"),
        (70, "Kecerdasan Buatan"),
        (20, "Matematika Diskrit"),
        (40, "Basis Data"),
        (60, "Jaringan Komputer"),
        (80, "Sistem Operasi")
    ]
    
    for id_buku, judul in data_buku:
        perpustakaan.insert(id_buku, judul)
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku}")
    
    print("======")
    
    print("[INFO] Koleksi Buku (In-Order Traversal):")
    perpustakaan.traversal_inorder(perpustakaan.root)
    print("======")
    
    perpustakaan.search(60)
    perpustakaan.search(100)
    
    print("")

    node_min = perpustakaan.get_min(perpustakaan.root)
    node_max = perpustakaan.get_max(perpustakaan.root)
    
    if node_min:
        print(f"[STATISTIK] ID Terkecil: {node_min.id_buku}")
    if node_max:
        print(f"[STATISTIK] ID Terbesar: {node_max.id_buku}")
        
    # 5. Analisis Struktur (Height) [cite: 31]
    tinggi_tree = perpustakaan.height(perpustakaan.root)
    print(f"[INFO] Tinggi (Height) Tree: {tinggi_tree}")
    
    print("===")
    print("Simulasi Selesai!")
    print("====")

# Memanggil fungsi main untuk menjalankan simulasi
if __name__ == "__main__":
    main()