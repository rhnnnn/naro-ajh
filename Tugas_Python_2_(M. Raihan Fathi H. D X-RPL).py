#Nama
print(30*"=")
print("Nama  : M. Raihan Fathi H. D")
print("Kelas : X-RPL")
print("Absen : 10")
print(30*"="+"\n")

#Chooser
print(20*"=", "Masukkan Pilihan", 20*"=")
print("1. Menuju Soal Nombor 1")
print("2. Menuju Soal Nombor 2")
print("3. Menuju Soal Nombor 3")
print(58*"=")
chosen=int(input("Masukkan nombor yang dipilih = "))
print()
#Proses
if chosen == 1:
    bilangan_1=int(input("Masukkan bilagan ke-1 = "))
    bilangan_2=int(input("Masukkan bilagan ke-2 = "))
    bilangan_3=int(input("Masukkan bilagan ke-3 = "))
    print()
    hasil_choosen=bilangan_1+bilangan_2+bilangan_3/3
    print(f"Hasilnya ialah = {hasil_choosen}")

elif chosen == 2:
    fungsi_x=int(input("Masukkan nilai untuk fungsi x = "))
    hasil_choosen=2*fungsi_x**3+2*fungsi_x+15/fungsi_x
    print(f"Hasil daripada soal fungsi x tersebut ialah = {hasil_choosen}")

elif chosen == 3:
    nilai_a=float(input("Masukkan nilai A = "))
    nilai_b=float(input("Masukkan nilai B = "))
    nilai_c=float(input("Masukkan nilai C = "))
    nilai_d=float(input("Masukkan nilai D = "))
    
    biar_bisa=nilai_a
    nilai_a=nilai_b
    nilai_b=nilai_d
    nilai_d=nilai_c
    nilai_c=biar_bisa
    print()
    print("Nilai A = ", nilai_a)
    print("Nilai B = ", nilai_b)
    print("Nilai C = ", nilai_c)
    print("Nilai D = ", nilai_d)

else:
    print("Kaga ada EUY")
