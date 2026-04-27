# 3 attribut
# 2 method

class Komputer:
    def __init__(self,layar,prossesor,storage):
        self.layar = layar
        self.prossesor = prossesor
        self.storage = storage

    def ubah(self,change_layar,change_prosessor,change_storage):
        self.layar = change_layar
        self.prossesor = change_prosessor
        self.storage = change_storage
        
    def pr(self):
        print(self.prossesor)
        print(self.layar)
        print(self.storage)

komputer1 = Komputer("oled", "intel i7 gen 12", "ssd 2 tb")
komputer1.ubah("ips", "intel i3 gen 3", "ssd 512 gb")
komputer1.pr()