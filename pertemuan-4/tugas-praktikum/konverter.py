from tabulate import tabulate
from kurs import kurs

data_tabel = [[k, v] for k, v in kurs.items()]
headers = ["Kode", "Kurs"]

print("=== KONVERTER MATA UANG ===")
print(tabulate(data_tabel, headers=headers, tablefmt="psql"))
def idr(uang):
    try:
        jumlah = int(input("Masukkan mata uang : "))
        if uang == "USD":
            hasil = jumlah / kurs["USD"]
            print(f"{hasil:.2f}")
        elif uang == "EUR":
            hasil = jumlah / kurs["EUR"]
            print(f"{hasil:.2f}")
        elif uang == "SGD":
            hasil = jumlah / kurs["SGD"]
            print(f"{hasil:.2f}")
        elif uang == "JPY":
            hasil = jumlah / kurs["JPY"]
            print(f"{hasil:.2f}")
        else:
            print("Jenis Mata Uang tidak valid")
    except ValueError:
        print("Jangan text dek,harus angka ya dek")
def usd(uang):
    try:
        jumlah = int(input("Masukkan mata uang : "))
        if uang == "IDR":
            hasil = jumlah * kurs["USD"]
            print(hasil) 
        elif uang == "EUR":
            hasil = jumlah * kurs["USD"]
            hasil /= kurs["EUR"]
            print(f"{hasil:.2f}")
        elif uang == "SGD":
            hasil = jumlah * kurs["USD"]
            hasil /= kurs["SGD"]
            print(f"{hasil:.2f}")
        elif uang == "JPY":
            hasil = jumlah * kurs["USD"]
            hasil /= kurs["JPY"]
            print(f"{hasil:.2f}")
        else:
            print("Jenis Mata Uang tidak valid")
    except ValueError:
        print("Jangan text dek,harus angka ya dek")
def eur(uang):
    try:
        jumlah = int(input("Masukkan mata uang : "))
        if uang == "IDR":
            hasil = jumlah * kurs["EUR"]
            print(hasil) 
        elif uang == "USD":
            hasil = jumlah * kurs["EUR"]
            hasil /= kurs["USD"]
            print(f"{hasil:.2f}")
        elif uang == "SGD":
            hasil = jumlah * kurs["EUR"]
            hasil /= kurs["SGD"]
            print(f"{hasil:.2f}")
        elif uang == "JPY":
            hasil = jumlah * kurs["EUR"]
            hasil /= kurs["JPY"]
            print(f"{hasil:.2f}")
        else:
            print("Jenis Mata Uang tidak valid")
    except ValueError:
        print("Jangan text dek,harus angka ya dek")
def sgd(uang):
    try:
        jumlah = int(input("Masukkan mata uang : "))
        if uang == "IDR":
            hasil = jumlah * kurs["SGD"]
            print(hasil) 
        elif uang == "USD":
            hasil = jumlah * kurs["SGD"] 
            hasil /= kurs["EUR"]
            print(f"{hasil:.2f}")
        elif uang == "EUR":
            hasil = jumlah * kurs["SGD"] 
            hasil /= kurs["EUR"]
            print(f"{hasil:.2f}")
        elif uang == "JPY":
            hasil = jumlah * kurs["SGD"] 
            hasil /= kurs["JPY"]
            print(f"{hasil:.2f}")
        else:
            print("Jenis Mata Uang tidak valid")
    except ValueError:
        print("Jangan text dek,harus angka ya dek")

def jpy(uang):
    try:
        jumlah = int(input("Masukkan mata uang : "))
        if uang == "IDR":
            hasil = jumlah * kurs["JPY"]
            print(hasil)
        elif uang == "USD":
            hasil = jumlah * kurs["JPY"]
            hasil /= kurs["USD"] 
            print(f"{hasil:.2f}")
        elif uang == "EUR":
            hasil = jumlah * kurs["JPY"]
            hasil /= kurs["EUR"]
            print(f"{hasil:.2f}")
        elif uang == "SGD":
            hasil = jumlah * kurs["JPY"]
            hasil /= kurs["SGD"]
            print(f"{hasil:.2f}")
        else:
            print("Jenis Mata Uang tidak valid")
    except ValueError:
        print("Jangan text dek,harus angka ya dek")


