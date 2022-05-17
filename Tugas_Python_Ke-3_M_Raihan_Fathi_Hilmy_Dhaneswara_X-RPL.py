#Nama
print(30*"=")
print("Nama  : M. Raihan Fathi H. D")
print("Kelas : X-RPL")
print("Absen : 10")
print(30*"="+"\n")

nilai=int(input("Masukkan Nilai = "))

if nilai >= 88:
    kriteria="Kriteria A"
elif nilai >= 77 and nilai < 88:
    kriteria="Kriteria B"
elif nilai >= 60 and nilai < 77:
    kriteria="Kriteria C"
elif nilai >= 45 and nilai < 60:
    kriteria="Kriteria D"
elif nilai < 45:
    kriteria="Kriteria E"

print("Nilai Anda %d, Termasuk Kedalam %s" % (nilai, kriteria) )
