class RiwayatUrl:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "Isi List Kosong"
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            return "Isi List Kosong"
        return self.items[-1]
    def size(self):
        return len(self.items)
    
    def visit(self,url):
        self.push(url)

    def back(self):
        self.pop()
        return self.peek()
    
def main():
    Chrome = RiwayatUrl()
    Chrome.visit("https://www.w3schools.com/python/python_dsa_stacks.asp")
    Chrome.visit("www.youtube.com")
    Chrome.visit("https://github.com")
    print(Chrome.items)

    Chrome.back()
    print(Chrome.items)

    print(Chrome.size())
    print(Chrome.peek())

if __name__ == "__main__":
    main()