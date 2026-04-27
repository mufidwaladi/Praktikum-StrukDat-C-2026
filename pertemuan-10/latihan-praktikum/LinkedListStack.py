class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class RiwayatUrl:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        return self.count == 0
    
    def push(self, url):
        newNode = Node(url)
        newNode.next = self.top
        self.top = newNode
        self.count += 1

    def pop(self):
        if self.is_empty():
            return "Isi List Kosong"
        Popped_url = self.top
        self.top = self.top.next
        self.count -= 1
        return Popped_url.url

    def peek(self):
        if self.is_empty():
            return "Isi List Kosong"
        return self.top.url
    
    def size(self):
        return self.count
    
    def back(self):
        self.pop()
        return self.peek()

    def visit(self,url):
        self.push(url)
        
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print("None")


def main():
    Chrome = RiwayatUrl()
    Chrome.visit("https://www.w3schools.com/python/python_dsa_stacks.asp")
    Chrome.visit("www.youtube.com")
    Chrome.visit("https://github.com")
    Chrome.traverseAndPrint()

    Chrome.back()
    Chrome.traverseAndPrint()

    print(Chrome.size())
    print(Chrome.peek())

if __name__ == "__main__":
    main()