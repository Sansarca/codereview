'''
Користувач вводить рядок, що містить римський запис числа. Напишіть функцію, що повертає це число у арабському записі. Виведіть результат.
У випадку помилкового вводу виведіть повідомлення про помилку.
(Римські позначення цифр: M=1000, D=500, C=100, L=50, X=10, V=5, I=1. Жоден символ не може повторюватися понад 3 рази підряд.)зи підряд.)
'''
import re

re_rom = re.compile("^[MDCLXVI]+$")
regex = re.compile((r'^.*(.)(\1)(\1).*$'))
n = "Y"
while n == "Y":
    def if_number(text):
        for i in text:
            if bool(re_rom.match(text)):

                if bool(regex.match(text)):
                    print("Invalid char.")

                    break

                else:
                    return text
            else:
                print("Invalid char.")

                break



    print("Input romanian number:")
    a = input()
    RR=True
    a = if_number(a)
    arab=int(0)
    if bool(a):
        for i in a:
            if i=="M":
                arab+=1000
            elif i=="D":
                arab+=500
            elif i== "C":
                arab+=100
            elif i == "L":
                arab += 50
            elif i=="X":
                arab+=10
            elif i=="V":
                arab+=5
            elif i=="I":
                arab+=1
        print(arab)
    
    n = input("Press Y to restart,else press any key.")