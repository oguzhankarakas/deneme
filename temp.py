#Oguzhan Python Giriş

sozluk = dict()


while True:
    urun_ismi = input("Ürün ismini girin:")
    if(urun_ismi == 'quit'):
        break
    urun_adedi = input("Ürün adedini girin:")
    sozluk[urun_ismi] =   urun_adedi

    
print(sozluk)

"""
#Örnek Uygulamalar

#Elektrik Devresi

# V = I.R

pil = float(input("Volt değerini girin:"))
direnc = float(input("Direnç Değerini girin:"))

I = pil / direnc

print("{} Amper".format(I))


#a^2+b^2 = c^2 (Dik üçgenin hipotenüsünü bulma)
a = int(input("a kenarını girin:"))
b = int(input("b kenarını girin:"))

hipotenus = a**2 + b**2

print(hipotenus**0.5)



#DERS 8 iNPUT("fONKSİYONU VE ÖZELLİKLER")


#Kök bulduran program
#b2-4ac
#-b-kökdelta/2a
#-b+kökdelta/2a

a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

delta = b**2-4*a*c

x1= (-b - delta **0.5)/(2 * a)
x2= (-b + delta **0.5)/(2 * a)

print('Birinci kök : {}\n İkinci kök : {}\n'.format(x1,x2))


x2 = int(input("x^2li terimin katsayısını girin:"))
x1 = int(input("x'li terimin katsayısını girin:"))
sabit = int(input("sabit değerini girin:"))

delta = (x1**2) - (4*x2*sabit)
print(delta)
kök1 =  (-x1 - (delta**0.5))/2*x2
kök2 =  (-x1 + (delta**0.5))/2*x2
print("kök 1 = {}\nkök 2 = {}".format(kök1,kök2))


#IMDB puanı yazan program
film = []

film_ismi = input("Arama:")
imdb_puanı = float(input("IMDB puanını girin"))
film.append(film_ismi)
film.append(imdb_puanı)
print("Filmin ismi: {}\nFilm IMDB puanı: {}".format(film_ismi,imdb_puanı))

#Kullanıcı girişli iki sayıyı toplayan program örneği
sayi1 = int(input("birinci sayıyı girin:"))
sayi2 = int(input("ikinci sayıyı girin"))
print(sayi1 + sayi2)


sayı = float(input("Bir ondalıklı sayı girin:"))
print(sayı*5)


sayı = int(input("Sayı Girin:"))
print(sayı*3)


isim= input("İsminizi Giriniz:")
print(type(isim))
print(isim)






#DERS 7 Sözlük(dictionary) Veri Tipleri


restoran_menusu = {"pilav":5,  "kofte": 10}
print(restoran_menusu.items())
print(restoran_menusu.keys())
print(restoran_menusu.values())
muzik_grupları = {"MFÖ":{"gül":"Güllerin İçinden"},"Duman": {"Senden Daha Güzel","Öyle Dertli"},"Barış Manço":{"Alla beni pulla beni","Gülpembe"}}
print(muzik_grupları["MFÖ"]["gül"])


telefon_rehberi = {"Oğuzhan Karakaş":"506-355-1770", "ali veli":"3030000030030"}
telefon_rehberi["deniz"] = "02301230102"
print(telefon_rehberi)


sozluk = {"Sayılar":[[0,1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[0,2,4,6,8],[1,3,5,7,9]]}
print(sozluk["Sayılar"][3])


sozluk = {"beş":5,"Ali":"Diyarbakır"}
print(sozluk["Ali"])

sözlük = {"Galatasaray":20,"Fenerbahçe":19,"Beşiktaş":16,"Trabzonspor":6}
print(sözlük["Fenerbahçe"])





#DERS 6 Demet(Tuple) Veri Tipleri

demet = (1,2,3,4,5,6)

print(demet.index(3))

demet = "oguzhan"
demet = tuple(demet)








#DERS 5 liste Veri Tipleri

liste = [[1,2,3],4,5,6,[7,8,9]]

print(liste[4][1]) Liste içindeki listeye erişmek

liste.sort(reverse=True) alfabetik sıraya göre tersten sıralar
liste.sort(reverse=True) Büyükten küçüğe sıralar
liste.sort() küçükten büyüğe liste elemanlarını sıralar
print(liste[2])
liste.append(6) 6 değerini ekler
liste.append(8) 8 " " 
liste.pop() sondaki değeri çıkartır
liste.pop(2) 3 sayısını çıkarır 0,1,2 oalrak sayılır


liste = [1,2,3,4,5]
liste2 = [6,7,8,9,10]

liste3=liste+liste2

liste3 = liste3 + ["Mehmet"]
 liste3 = liste3*3 da kullanılabilir
print(liste3)



liste = [1,2,3,4,5,6,7,8,9,10]
print(liste[4::])



kral = "Oguzhan"
liste = list(kral)
liste[0] = "m" 
print(liste)

metin = ""
for i in liste:
    metin += i
    print(metin)
    
    

isim = "Abdullah"
print(isim[0])
liste = [1,2,3,4,5,6,7]



liste = [1,2,3,4,5,6,7]
liste[0] = 31
print(liste)

bos_liste= []
print(bos_liste)

print(len(liste))


liste = [1,2,3,4,5,6,"oguz"]
print(type(liste))



#DERS 4 Yıldızlı Parametreler

def goster(*args):
    
    for i in args:
        print(i)
        
goster(1,2,3,4,5,6)


print(*"GALATASARAY")
print(*"TBMM", sep = ".")

sayılar = [x for x in range(1,100) if x % 5 == 1]
print(sayılar)
örnek uygulama
#DERS 3.1 print fonksiyonu


dosya = open("kayıt.txt","w")
print("1-Oğuzhan Karakaş", file = dosya, flush = True)
#yada dosya.close() kullan flush = True



#DERS 3 print fonksiyonu 

def topla(y):
    toplam = 0
    for n in y:
        print(n)
        toplam += n
    return toplam
x = range(11)
print(topla(x))


def sayılarıtopla(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam

print(sayılarıtopla(1,2,3,4,5,6,7,8,9,10))


print("%s kadar korona vakası %s ölüme yol açar" % ("14000000",31))



basit yazımlar







aralara nokta koyar
print(*"TBMM",sep = ".")

"""
 



# DERS 2 Veri Dönüşümleri


"""
a = "bu sayı 4000"
print(int(a[8:12])*3)


a = "4000"
print(int(a)*3) str değerini float veya ine çevirme

a = 39
print(float(a)) floata çevirme


a=42.4 
 print(int(a)) int sayıya çevirme

"""


#Giriş Dersleri 1
"""a = "nahzuğO"
print(a[::-1])
düzelterek yazma"""


"""a = "O*ğ*u*z*h*a*n*K*a*r*a*k*a*ş"
print(a[::2])
Yıldızları kaldırıp sadece yazıyı aldım
"""




"""
a = "Oğuzhan"
b = "Karkaş"
c = "mühendis"
print(a+b+c)"""

# ::2 2şer atlayarak yazar 
# geri doğru yazma atlayarak print(a[::-1])
# print(len(a)) Karakter sayısı tespit etme
#print(a[0]) 0ıncı karakteri gösterir


"""
a =3*4 + 20/5 - (4+2)
parantez,çarpma,bölme
print(a)


a = 3
b = 4
print(a**b) üslü sayı göterme

# Dairenin Alanını Bulma


a = 5
b= 10 

#Yer değiştirme a,b = b,a

a += 5
print(a)
 
"""


