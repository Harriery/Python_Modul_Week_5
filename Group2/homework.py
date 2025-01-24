"""
#Question3: Create a "Shape" class. Under this class, create two subclasses, the "Rectangle" and "Square" classes.

class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Rectangle(Shape):
    def __init__(self, width, height):
        Shape.__init__(self,width, height)  
                
    def alan_hesapla(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, width,):
        Shape.__init__(self,width,width)
        
    def alan_hesapla(self):
        return self.width * self.width

ornek1 = Rectangle(5, 10)
print(ornek1.alan_hesapla())
ornek2 = Square(5)
print(ornek2.alan_hesapla())    """   


"""#Question4: Create a "Vehicle" class in Python. Make sure this class has the following properties:


class Vehicle():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
#arac=Vehicle('Toyota','Corolla','2020')
class OffRoadVehicle(Vehicle):
    def __init__(self,make,model,year,four_wheel_drive):
        Vehicle. __init__(self,make,model,year)
        self.four_wheel_drive=four_wheel_drive

class SportsCar(Vehicle):
    def __init__(self,make,model,year,max_speed):
        Vehicle. __init__(self,make,model,year)
        self.max_speed=max_speed


arazi_araci = OffRoadVehicle('Jeep', 'Wrangler', 2021, True)
print("Marka:",arazi_araci.make,
      "Model:",arazi_araci.model,
      "Aracin yili:",arazi_araci.year,
      "Dort ceker:",arazi_araci.four_wheel_drive)

spor_araba=SportsCar('Lamborghini','Huracan',2024,350 )
print("Marka:",spor_araba.make,
      "Model:",spor_araba.model,
      "Aracin Yili:",spor_araba.year,
      "Max Hiz:",spor_araba.max_speed)"""




#Question5: Create a "Customer" class and an "Account" class. Let the "Account" class inherit from the "Customer" class and represent a customer's bank account information.

class Customer():
    def __init__(self,name,surname,tc,phone):
        self.name = name
        self.surname = surname
        self.tc = tc
        self.phone = phone

    def display_information(self):
        print(f"Müşteri Adı: {self.name}")
        print(f"Müşteri Soyadı: {self.surname}")
        print(f"Müşteri TC No: {self.tc}")
        print(f"Müşteri Telefon Numarası: {self.phone}")

class Account(Customer):
    def __init__(self,name,surname,tc,phone,accountNumber,balance):
        Customer. __init__(self,name,surname,tc,phone)
        self.accountNumber=accountNumber
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"hesabiniza {amount} tl yatirildi.Guncel bakiyeniz{self.balance}")


    def money_check(self,amount):
        if amount<self.balance:
            self.balance-=amount
            print(f"Hesabinizdan {amount}tl cekildi.Guncel bakiyeniz{self.balance}")

        else:
            print("yetersiz bakiye")

    def display_balance(self):
        print(f"Hesap bakiyesi:{self.balance} TL")

print("Musteri bilgilerini giriniz:")
name=input("Ad:")
surname=input("Soyad:")
tc=input("TC kimlik no:")
phone=input("Telefon no:")


print("\nHesap bilgilerini giriniz:")
accountNumber=input("Hesap numarasi:")
balance=float(input("Bakiye:"))

account=Account(name,surname, tc, phone, accountNumber, balance)
while True:
    print("Islemler")
    print("1.Musteri bilgilerini goruntule:")
    print("2.Hesap bakiyesi goruntule:")
    print("3.Para yatir:")
    print("4.Para cek:")
    print("5.Cikis")
    choice=input("1 ile 5 arasi bir islem seciniz:")

    if choice=="1":
        account.display_information()
    elif choice=="2":
        account.display_balance()
    elif choice=="3":
        amount=float(input("Yatirmak istediginiz tutar:"))
        account.deposit(amount)
    elif choice=="4":
        amount=float(input("Cekmak istediginiz tutar:"))
        account.money_check(amount)
    elif choice=="5":
        break
    else:
        print("Gecersiz islem")