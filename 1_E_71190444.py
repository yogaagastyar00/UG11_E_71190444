print("Menu Program Yang Tersedia");
print("1. pangkatkan angka");
print("2. akarkan bilangan");
pilihan= int(input("Masukan pilihan yang diinginkan : "));
def akarBilangan():
    angkaakar= float(input("Masukan angka yang ingin di akar\nAngka : "));
    akarmodif= input("Ingin memodifikasi akar ?(yes/no)\n: ");
    if akarmodif == "yes":
        akarbaru= int(input("Masukan nilai akar : "));
        r2=angkaakar**(1/ akarbaru)
        print("Hasil akar pangkat",akarbaru,"dari",angkaakar,"=",round(r2,2));
    elif akarmodif =="no":
        r2=angkaakar**(1/2)
        print("Hasil akar pangkat 2 dari",angkaakar,"=",round(r2,2));
    else:
        print("ketik yes/no");
    return pilihan
def pangkatAngka():
    pangkat = float(input("Masukan angka ingin di Pangkatkan\nAngka : "));
    pangkatmodif=str(input("ingin memodifikasi pangkat ?(yes/no)\n: "));
    if pangkatmodif == "yes" :
        nilaipangkatbaru= float(input("Masukan nilai pangkat : "));
        r1 = pangkat ** nilaipangkatbaru
        print("Hasil dari",str(pangkat)+"^"+str(nilaipangkatbaru),"=",round(r1,2));
    elif pangkatmodif =="no":
        r1= pangkat ** 2
        print("Hasil dari",str(pangkat)+"^2 = ",round(r1,2));
    else:
        print("ketik yes/no");
    return pilihan
if pilihan == 1:
    pangkatAngka()
elif pilihan == 2:
    akarBilangan()
    
