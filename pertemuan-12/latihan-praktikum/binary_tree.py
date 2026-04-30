class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def insert_root(self, data):
        self.root = Node(data)

    def insert_left(self, parent_node ,data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node

    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node

    def traverse_preorder(self, node, res):
        if node is not None:
            res.append(node.data)
            self.traverse_preorder(node.left, res)
            self.traverse_preorder(node.right, res)
        return res

    def traverse_inorder(self, node, res):
        if node is not None:
            self.traverse_inorder(node.left, res)
            res.append(node.data)
            self.traverse_inorder(node.right, res)
        return res

    def traverse_postorder(self, node, res):
        if node is not None:
            self.traverse_postorder(node.left, res)
            self.traverse_postorder(node.right, res)
            res.append(node.data)
        return res

    def get_leaf_nodes(self, node, res):
        if node is not None:
            if node.left is None and node.right is None:
                res.append(node.data)
            self.get_leaf_nodes(node.left, res)
            self.get_leaf_nodes(node.right, res)
        return res
    
    def cetak_list(self, daftar, pemisah="-"):
        hasil = ""
        for i in range(len(daftar)):
            hasil += str(daftar[i])
            if i < len(daftar) - 1:
                hasil += pemisah
        return hasil

    
def main():
    Pohon = BinaryTree()
    Pohon.insert_root("A")
    Pohon.insert_left(Pohon.root, "B")
    Pohon.insert_right(Pohon.root, "C")
    Pohon.insert_left(Pohon.root.left, "D")
    Pohon.insert_right(Pohon.root.left, "E")
    Pohon.insert_right(Pohon.root.right, "F")

    print("[INFO] Struktur berhasil dibuat.")
    print("====")
    print("HASIL AUDIT:")

    # Eksekusi dan tampilkan hasil
    pre = Pohon.traverse_preorder(Pohon.root, [])
    print("1. Pre-Order  :", Pohon.cetak_list(pre, "-"))

    ino = Pohon.traverse_inorder(Pohon.root, [])
    print("2. In-Order   :", Pohon.cetak_list(ino, "-"))
                                                    
    post = Pohon.traverse_postorder(Pohon.root, [])
    print("3. Post-Order :", Pohon.cetak_list(post, "-"))

    leaf = Pohon.get_leaf_nodes(Pohon.root, [])
    print("[DATA] Gudang Ujung (Leaf Nodes):", Pohon.cetak_list(leaf, ", "))

if __name__ == "__main__":
    main()