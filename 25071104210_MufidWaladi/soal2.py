


def rentang_harga(data, min_harga, max_harga):
    sesuai_rentang = []

    for x in data:
        if x['harga'] >= min_harga and x['harga'] <= max_harga:
            sesuai_rentang.append(x['merk'])
    
    print(sesuai_rentang)
        


def main():
    stok_gadget = [
    {'merk': 'Samsung', 'tipe': 'S23', 'harga': 12000000},
    {'merk': 'Oppo', 'tipe': 'Reno 10', 'harga': 6000000}, 
    {'merk': 'Xiaomi', 'tipe': 'Mi 13', 'harga': 10000000},
    {'merk': 'Iphone', 'tipe': '15 Pro', 'harga': 20000000},
    ]
    min_harga = int(input("Masukkan batas bawah"))
    max_harga = int(input("Masukkan batas atas"))
    rentang_harga(stok_gadget,min_harga,max_harga)

if __name__ == "__main__":
    main()