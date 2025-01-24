# Question1

class Dikdortgen:
    def __init__(self,genislik,yukseklik):
        self.genislik=genislik
        self.yukseklik=yukseklik
    def alan_hesapla(self):
        return self.genislik*self.yukseklik
    def cevre_hesapla(self):
        return (self.genislik+self.yukseklik)*2
    def __repr__(self):
        return f'Dikdortgenin Alani : {self.genislik*self.yukseklik} \nDikdortgenin Cevresi : {(self.genislik+self.yukseklik)*2}'
#print(Dikdortgen(5,7))
dikdortgen1=Dikdortgen(8,8)
dikdortgen2=Dikdortgen(9,9)
print(dikdortgen1.alan_hesapla())
print(dikdortgen2.cevre_hesapla())

# Question2

class Okul():
    def __init__(self,ad,kurulus_yili,ogrenciler=None,ogretmenler=None):
        self.ad=ad
        self.kurulus_yili=kurulus_yili
        self.ogrenciler={}
        self.ogretmenler={}
    def yeni_ogrenci_ekle(self,ogrenci_adi,sinif):
        self.ogrenciler[ogrenci_adi]=sinif
        print(f'\n{ogrenci_adi} isimli ogrenci {sinif} sinifina kaydolmustur.')
    def yeni_ogretmen_ekle(self,ogretmen_adi,brans):
        self.ogretmenler[ogretmen_adi]=brans
        print(f'\n{ogretmen_adi} isimli ogretmen {brans} bransi icin okula kaydolmustur')
    def ogrenci_listesini_goruntule(self):
        print(f'Okuldaki ogrenciler :', self.ogrenciler)
    def ogretmen_listesini_goruntule(self):
        print(f'Okuldaki ogretmenler :', self.ogretmenler)

okul=Okul('Werhere University','2019')

while True:
    okul.yeni_ogrenci_ekle(input('\nYeni Ogrencinin Adini Giriniz :'),input('Yeni Ogrencinin Sinifini Giriniz :'))
    okul.ogrenci_listesini_goruntule()

    okul.yeni_ogretmen_ekle(input('\nYeni Ogretmenin Adini Giriniz :'),input('Yeni Ogretmenin Bransini Giriniz :'))
    okul.ogretmen_listesini_goruntule()


# Question3

class Shape():
    def __init__(self,genislik,yukseklik):
        self.genislik=genislik
        self.yukseklik = yukseklik
class Dikdortgen(Shape):
    def __init__(self,genislik,yukseklik):
        super().__init__(genislik,yukseklik)
    def alan_hesapla(self):
        print(f'Dikdirtgenin alani : {self.genislik*self.yukseklik}')
class Kare(Shape):
    def __init__(self,genislik,yukseklik):
        super().__init__(genislik,yukseklik)
    def alan_hesapla(self):
        return self.genislik**2
kare = Kare(5,5)
dikdortgen = Dikdortgen(10,5)
dikdortgen.alan_hesapla()
print('Kare alani : ',kare.alan_hesapla())


# Question4

class Arac:
    def __init__(self,marka,model,yil):
        self.marka=marka
        self.model = model
        self.yil = yil
class AraziAraci(Arac):
    def __init__(self,marka,model,yil,dort_ceker):
        super().__init__(marka,model,yil)
        self.dort_ceker=dort_ceker
class SporAraba(Arac):
    def __init__(self,marka,model,yil,max_hiz):
        super().__init__(marka, model, yil)
        self.max_hiz = max_hiz
arac1= Arac('Ford','Mustang','1967')
arac2= AraziAraci('Ford','Ranger','2024','Var')
arac3= SporAraba('Simsek','Mcqueen','2006','318 km/saat')

print(vars(arac1))
print(vars(arac2))
print(vars(arac3))



# Question5

class Customer:
    def __init__(self,name,surname,tc_identification,phone):
        self.name = name
        self.surname=surname
        self.tc_identification=tc_identification
        self.phone=phone
    def display_information(self):
        print(f'\nMusteri Adi: {self.name}\nMusteri Soyadi: {self.surname}\nMusteri Tc Numarasi: {self.tc_identification}\nMusteri Numarsi: {self.phone}')


class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone,account_number,balance):
        super(). __init__(name,surname,tc_identification,phone)
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        self.balance+=amount
        print(f'\nHesaba {amount} EUR yatirilmistir. Yeni hesap bakiyesi : {self.balance} EUR')
    def money_check(self,amount):
        if self.balance >= amount:
            self.balance-=amount
            print(f'\nHesaptan {amount} EUR cekilmistir. Yeni hesap bakiyesi : {self.balance} EUR')
        else:
            print('\nYetersiz bakiye')
    def display_balance(self):
        print(f'\nHesap bakiyesi : {self.balance} EUR')


customer=Account('Haluk','YILDIRIM','12345678901','0212 123 45 67','9999',20000)

customer.deposit(500)
customer.display_balance()
customer.display_information()
customer.money_check(1000)
