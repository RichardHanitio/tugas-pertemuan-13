from os import system
system("cls")

satuan = ["","one","two","three","four","five","six","seven","eight","nine"]

def terbilang(n):
    if n%1>0 :
        #apabila terdapat desimal
        str_n = str(n)
        cari_letak_koma = str_n.find(".")
        angka_belakang_koma = str_n[cari_letak_koma+1:]
        angka_depan_koma = str_n[:cari_letak_koma]
        int_angka_belakang_koma = int(angka_belakang_koma)
        int_angka_depan_koma = int(angka_depan_koma)

        return terbilang(int_angka_depan_koma)+" point "+terbilang(int_angka_belakang_koma)

    elif n<10 :
        #satuan
        return satuan[int(n)]
    
    elif n>=1_000_000_000 :
        #miliaran
        return terbilang(n//1_000_000_000)+" billion "+terbilang(n%1_000_000_000)

    elif n>=1_000_000 :
        #jutaan
        return terbilang(n//1_000_000)+" million "+terbilang(n%1_000_000)

    elif n>=1_000 :
        #ribuan
        return terbilang(n//1_000)+" thousand "+terbilang(n%1_000)

    elif n>=100 :
        #ratusan
        return terbilang(n//100)+" hundred "+terbilang(n%100)
    
    elif n>=20 :
        #puluhan
        if n//10==2 :
            return "twenty "+terbilang(n%10)
        elif n//10==3 :
            return "thirty "+terbilang(n%10)
        elif n//10==4 :
            return "forty "+terbilang(n%10)
        elif n//10==5 :
            return "fifty "+terbilang(n%10)
        else :
            return terbilang(n//10)+("ty "if n//10!=8 else "y ")+terbilang(n%10)

    else :
        #belasan
        if n==10 : return "ten"
        elif n==11 : return "eleven"
        elif n==12 : return "twelve"
        elif n==13 : return "thirteen"
        elif n==15 : return "fifteen"
        else : return terbilang(n%10)+ ("teen" if (n%10!=8) else "een")

#input output
n = float(input("Masukkan sebuah bilangan : "))
print(f"{n if n%1>0 else int(n)} -> {terbilang(n)}")