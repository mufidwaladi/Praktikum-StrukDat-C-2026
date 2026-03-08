
def registrasi_gadget(merk, tipe, harga, sn):
    if harga < 1000000:
        print("Harga salah")
        return None
    if len(sn) > 5 or len(sn) < 5:
        print("serial number salah")
        return None
    
    return[{
            "merek" : merk,
            "tipe" : tipe,
            "harga" : harga,
            "sn" : sn,
            "status" : "Tersedia",
            }]
    
        
    
def main():
    gadget = [{

}]

    m = str(input("masukkan merek barang "))
    t = str(input("masukkan tipe barang "))
    h = float(input("Masukkan harga barang "))
    s = str(input("Masukkan serial number "))
    gadget = registrasi_gadget(m, t, h, s)

    print(gadget)

if __name__ == "__main__":
    main()