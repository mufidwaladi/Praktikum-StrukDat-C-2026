def gangen(daftar):
    ganjil = []
    genap = []
    for x in daftar:
        num =  int(x.split(" ")[1])
        if num % 2 == 0:
            genap.append(x)
        else:
            ganjil.append(x)
    return ganjil,genap
def main():
    ganjil, genap = gangen(["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"])
    print(ganjil)
    print(genap)

main()