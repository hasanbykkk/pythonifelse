# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


x=50
y=30
c=20

adres=input("gönderilecek adresi yazınız")
ağırlık=int(input("ağırlığı giriniz"))
teslim = input("hızlı teslim mi yavaş teslim mi ")

cevap = "h" or "y"

if ağırlık>25:
    print("fiyatınız",x+y,)
elif  cevap=="h" and ağırlık>25:
    print("fiyatınız",x+y+c,)
elif cevap=="y"and ağırlık<25:
    print("fiyatınız",x,)
elif cevap=="h"and ağırlık<25:
    print("fiyatınız",x+c,)




