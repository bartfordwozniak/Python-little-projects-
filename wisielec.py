print("""                WiTaJ
                   w grze @$#
                    WISIELEC
                                             """)
import random
import sys

life = 10

bufor = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',]
used = []
hasla = []  # tu trzeba dodać listę haseł

def gramy():
    h = len(hasla)  # sprawdza ilość elementow w liście haseł
    guess = random.randint(0, h)  # losuje jedno haslo (liczbę elementu z listy hasel)
    print("Haseł w bazie: ", h)

    global a
    a = hasla[guess]
   
    # utworzenie bufora z odpowiednią ilością znaków '-'
    bufor = ['-'] * len(a)
    print("(", a, ")\n")
    
    j = 1
    while life != 0:
        for i in range(len(a)):  # poprawna pętla for
            print(bufor[i], end="")
            print(space, end="")
        print("\nPróba", j, ". ", end="")
        j += 1
        proba = str(input("Podaj literę\n"))
        if proba in alfabet:
            if proba in used:
                print("Tę literę już podał*ś.\n")
            else:
                used.append(proba)
            if proba in a:
                print("Dobrze! Ta litera jest w haśle ")
                for i in range(len(a)):
                    if proba == a[i]:
                        bufor[i] = proba
                print("\n")
            else:
                wisi()  # tu należy dodać funkcję wisi()
            
        else:
            print("niedozwolona litera\n")

def komp_gra():
    print("komp gra")
    litery = len (alfabet)
   # randint()

def gra():
    global life
    tryb_gry = int(input("Jako kto chcesz grać?\n1) Hasłodawacz\n2)Ten co może zawisnąć\n "))
    while tryb_gry not in [1, 2]:
        tryb_gry = int(input("Zła odpoweidź. \nJako kto chcesz grać?\n1) Hasłodawacz\n2)Ten co może zawisnąć \n"))

    if tryb_gry == 2:
        gramy()
