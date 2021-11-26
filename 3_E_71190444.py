print ("=======Program Manipulasi String=======");
print ("Pilihan Menu");
print ("1. Hitung kata");
print ("2. cek kata");
print ("3. ubah kata");
pilihan = int(input("Pilihan anda : "));
kata = input("Masukan sebuah kalimat/kata : ");
kalimat = kata.lower()
def hitungKata():
    if pilihan == 1:
        katahitung = input("Masukan kata yang ingin dihitung : ").lower();
        hitungkalimat = kalimat.count(katahitung)

        print ("Terdapat sebanyak", hitungkalimat, "kata", katahitung, "didalam string");
def cekkata():
    if pilihan == 2:
        katacek = input("Masukan kata yang ingin di cek : ");
        kataup = katacek.upper()
        hasil = kalimat.replace(katacek, kataup)
        if kataup not in kalimat:
            print ("Kata", katacek, "tidak terdapat di dalam string");
            print ("String diubah menjadi : ");
            print (hasil, katacek)
        else:
            print ("Kata", katacek, "terdapat di dalam string");
            print ("String diubah menjadi : ");
            print (hasil, katacek);
def ubahKata():
    if pilihan == 3:
        kataubah = input("Masukan kata yang ingin diubah : ");
        kataganti = input("Masukan kata pengganti : ");

        print ("Anda akan mengubah kata", kataubah, "menjadi", kataganti, "sebanyak 1x");
        iyatidak = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ");
        if iyatidak == "yes":
            totalganti = int(input("Masukan jumlah total penggantian : "));
            print ("String berhasil diubah menjadi : ");

            ganti1 = kalimat.replace(kataubah, kataganti, totalganti)
            print (ganti1);
        elif iyatidak == "no":
            totalganti = 1
            print ("String berhasil diubah menjadi : ");

            ganti1 = kalimat.replace(kataubah, kataganti, totalganti)
            print (ganti1);
if pilihan == 1:
    hitungKata()
elif pilihan == 2:
    cekkata()
elif pilihan == 3:
    ubahKata()
