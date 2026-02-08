nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}

nilai_siswa
["S04"] = {"nama": "Fafa",
"tugas": 85,
"uts": 80,
"uas" : 90}

for x in nilai_siswa.values():
    final = (x["tugas"] * (20/100) + x["uts"] * (30/100) + x["uas"] * (50/100))
    if(final > 80):
        print(f"{x["nama"]}: {final}")