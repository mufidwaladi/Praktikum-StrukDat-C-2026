import konverter

asal = str(input("Dari (IDR/USD/EUR/SGD/JPY): ")).upper().strip()
menuju = str(input("Ke (IDR/USD/EUR/SGD/JPY): ")).upper().strip()

if asal == menuju:
    print("Mata uangnya sama tidak perlu dikonvert")
elif asal == "IDR":
    konverter.idr(menuju)
elif asal == "USD":
    konverter.usd(menuju)
elif asal == "EUR":
    konverter.eur(menuju)
elif asal == "SGD":
    konverter.sgd(menuju)
elif asal == "JPY":
    konverter.jpy(menuju)
else:
    print("Jenis Mata Uang tidak valid")