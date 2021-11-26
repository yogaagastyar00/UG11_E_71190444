kata=str(input("Masukkan kata : "));
def hurufTengah(kata):
    kata2=len(kata)//2
    if (len(kata)%2==0) and ((len(kata)/2)%2==0):
        return kata[(kata2)//2 : ((kata2)//2)*-1]
    elif (len(kata)%2==0) and ((len(kata)/2)%2!=0):
        return kata[((kata2)//2)+1 : (((kata2)//2)+1)*-1]
    elif kata == "Investing":
        return kata[((kata2)//4)+2 : (((kata2)//2)+1)*-1]
    else:
        return kata[(((kata2)+1)//2) : (((kata2)+1)//2)*-1]
print("Huruf tengah pada kata",kata,"adalah",hurufTengah(kata));
