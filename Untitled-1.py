while True:
#burada kodun sürekliliğini sağladık
    def İsimSoyisimBulma():
        isim = input("isminizi girin:")
        #kullanıcıdan ismini aldık
        soyisim = input("soyisiminizi girin:")
        #kullanıcıdan soy ismini aldık
        isimsoyisim = isim +" "+ soyisim
        #kullanıcının ismi ile soy ismini birleştirdik
        print(isimsoyisim)
        #birleştirdiğimiz isimleri yazdırdık
    İsimSoyisimBulma()
