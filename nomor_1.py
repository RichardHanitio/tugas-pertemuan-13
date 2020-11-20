from os import system
system("cls")

satuan = ["","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan"]
def terbilang (n) :
    #base
    if n%1>0 :
        #apabila terdapat desimal
        str_n = str(n)
        cari_letak_koma = str_n.find(".")
        angka_belakang_koma = str_n[cari_letak_koma+1:]
        angka_depan_koma = str_n[:cari_letak_koma]
        int_angka_belakang_koma = int(angka_belakang_koma)
        int_angka_depan_koma = int(angka_depan_koma)

        return terbilang(int_angka_depan_koma)+" koma "+terbilang(int_angka_belakang_koma)

    elif n<10 :
        #satuan
        return satuan[int(n)]

    #rekursi
    elif n>=1_000_000_000_000 :
        #triliunan
        return terbilang(n//1_000_000_000_000)+" triliun "+terbilang(n%1_000_000_000_000)

    elif n>=1_000_000_000 :
        #miliaran
        return terbilang(n//1_000_000_000)+" miliar "+terbilang(n%1_000_000_000)

    elif n>=1_000_000 :
        #jutaan
        return terbilang(n//1_000_000)+" juta "+terbilang(n%1_000_000)

    elif n>=1_000 :
        #ribuan
        if n//1_000==1 : #seribuan
            return "seribu "+terbilang(n%1_000)
        else : #dua ribuan keatas
            return terbilang(n//1_000)+" ribu "+terbilang(n%1_000)

    elif n>=100 :
        #ratusan
        if n//100==1 :   #seratusan
            return "seratus "+terbilang(n%100)
        else :  #dua ratusan keatas
            return terbilang(n//100)+" ratus "+terbilang(n%100)

    elif n>=20 :
        #puluhan
        return terbilang(n//10)+" puluh "+terbilang(n%10)

    else :
        #belasan
        if n==10 : return "sepuluh"
        elif n==11 : return "sebelas"
        else : return terbilang(n%10)+" belas" 
    
#input output
n = float(input("Masukkan sebuah bilangan : "))
print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")