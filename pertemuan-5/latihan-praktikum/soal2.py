data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]

#A
for x,y in data_aktivitas:
    if y > 80:
        print(f"{x} mendapatkan prediket gold")

    elif y > 50 and y < 80:
        print(f"{x}mendapatkan predikat Silver")

    else:
        print(f"{x}mendapatkan predikat Bronze")