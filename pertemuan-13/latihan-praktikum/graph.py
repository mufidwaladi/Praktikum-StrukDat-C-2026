class NavigasiLogistik:
    def __init__(self):
        self.graph = {}

    def tambah_kota(self, nama):
        if nama not in self.graph:
            self.graph[nama] = []

    def tambah_jalan(self, u, v, jarak):
        self.tambah_kota(u)
        self.tambah_kota(v)
        self.graph[u].append((v, jarak))
        self.graph[v].append((u, jarak))
        print(f"[INPUT] Menambahkan jalan: {u} <-> {v} ({jarak} km)")

    def tampilkan_graph(self): 
        print("\n[INFO] Struktur Jaringan Distribusi:")
        for kota, tetangga in self.graph.items():
            koneksi = ", ".join([f"{t[0]} ({t[1]})" for t in tetangga])
            print(f"{kota} terhubung ke: {koneksi}")

    def dijkstra(self, kota_asal):

        jarak_terpendek = {kota: float('inf') for kota in self.graph}
        jarak_terpendek[kota_asal] = 0
        dikunjungi = set()

        print(f"\n[PROSES] Menghitung rute terpendek dari: {kota_asal}...")

        while len(dikunjungi) < len(self.graph):
            # Cari kota dengan jarak terkecil yang belum dikunjungi 
            kota_sekarang = None
            jarak_terkecil = float('inf')

            for kota in self.graph:
                if kota not in dikunjungi and jarak_terpendek[kota] < jarak_terkecil:
                    jarak_terkecil = jarak_terpendek[kota]
                    kota_sekarang = kota

            if kota_sekarang is None:
                break

            dikunjungi.add(kota_sekarang)

            for tetangga, bobot in self.graph[kota_sekarang]:
                jarak_baru = jarak_terpendek[kota_sekarang] + bobot
                if jarak_baru < jarak_terpendek[tetangga]:
                    jarak_terpendek[tetangga] = jarak_baru

        print(f"[HASIL] Jarak Terpendek dari {kota_asal}:")
        i = 1
        for kota, jarak in jarak_terpendek.items():
            if kota != kota_asal:
                print(f"{i}. Ke {kota}: {jarak} km")
                i += 1
        print("Simulasi Navigasi Selesai!")


sistem = NavigasiLogistik()

sistem.tambah_jalan("Jakarta", "Bandung", 150)
sistem.tambah_jalan("Jakarta", "Cirebon", 200)
sistem.tambah_jalan("Bandung", "Tasikmalaya", 100)
sistem.tambah_jalan("Bandung", "Cirebon", 130)
sistem.tambah_jalan("Cirebon", "Semarang", 250)
sistem.tambah_jalan("Tasikmalaya", "Semarang", 200)


sistem.tampilkan_graph()

sistem.dijkstra("Jakarta")