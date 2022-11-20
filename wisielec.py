print("""                WiTaJ
                   w grze @$#
                    WISIELEC

                                             """)
#from random
import random
import sys
life = 10

bufor = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ',]


def gramy():
    h = len(hasla)                 # sprawdza ilość elementow w liście haseł
    guess = random.randint(0, h)    #losuje jedno haslo ()liczbę elementu z listy hasel
    print("Haseł w bazie: ", h)

    global a
    a = hasla[guess]
   
    
    for i in range (0, len(a)):
       # bufor[i] = '-'
        bufor.insert(i, '-')
        i += 1

   # bufor = [len (hasla[len(hasla)])]
 #   bufor [f]            #bufor to lista o tej samej liczbie elementów co haslo ale pusta lista
    
  
    print("(", a, ")\n")
   # print()
 
    
    while life != 0:
        for i in range(0, len(a)):
            print(bufor[i], end="") #bufor to lista z samymi - ilości liter hasla
            print(space, end="")
            i += 1
        j = 1
        print("\nPróba", j, ". ", end="")
        j += 1
        proba = str(input("Podaj literę\n"))
        if proba in alfabet:
            if proba in used:
                print("Tę literę już podał*ś.\n")
            else:
                used.append(proba)                                  
            #    proba = used[i]
                if proba in a:
                    print("Dobrze! Ta litera jest w haśle ")
                   # for i in range(1, len(bufor)):
                     #   if proba == a[i]:
                    w = a.index(proba, 0, 30) 
                    print("na ", w+1, " miejscu.\n")
                    a[w] = proba                                         #zmiana danych, porównywanie ascii ???
                        #i =+ 1

                else:
                    wisi()
            
        else:
                print("niedozwolona litera\n")
              
    





def komp_gra():
    print("komp gra")
    litery = len (alfabet)
   # randint()






    
def  gra():
    global life
    tryb_gry = int(input("Jako kto chcesz grać?\n1) Hasłodawacz\n2)Ten co może zawisnąć\n "))
    while tryb_gry not in [1, 2]:
        tryb_gry = int(input("Zła odpoweidź. \nJako kto chcesz grać?\n1) Hasłodawacz\n2)Ten co może zawisnąć \n"))

 #   trudnosc = int(input("Łatwo (1) czy trudno (2)?\n"))
   # while trudnosc not in [1, 2]:
     #   trudnosc = int(input("Zła odpoweidź. \nŁatwo (1) czy trudno (2)?\n"))

    if tryb_gry == 2:
        gramy()
    else:
        komp_gra()




        
space = " "
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'z' ,' y', 'x', space ]
used = []
hasla = ['bobolak', 'strumien','logika','pwr','poniedzialkow']




def wisi():
    global life
    if life == 10:
        print("""



                                                                      
----------------------------------------------------

    """)
    elif life == 9:
        print("""


                                                  
                                                       
                                                       
                                                       |
                                                       |                                                 
----------------------------------------------------
    """)
    elif life == 8:
        print("""


                                 
                                                     
                                                       |
                                                       |
                                                       |
                                                       |                                                 
----------------------------------------------------

 """)
    elif life == 7:
        print("""


                                    
                                                     
                                                       |
                                                       |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 6:
        print("""


                                    
                                                      \|/
                                                       |
                                                       |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 5:
        print("""


                                    ===========
                                                      \|/
                                                       |
                                                       |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

""")
    elif life == 4:
        print("""



                                    ===========
                                           |          \|/
                                                       |
                                                       |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 3:
        print("""



                                    ===========
                                           |         \|/
                                           o         |
                                                       |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 2:
        print("""



                                    ===========
                                           |          \|/
                                           o          |
                                            |          |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 1:
        print("""



                                    ===========
                                           |          \|/
                                           o          |
                                           /|\         |
                                                      /|\
                                                    /  |  \                                                
----------------------------------------------------

 """)
    elif life == 0:
        print("""



                                    ===========
                                           |          \|/
                                           o          |
                                           /|\         |
                                            /\        /|\
                                                     / |  \                                                
----------------------------------------------------

 """)
    life -= 1        
    
gra()
if tryb_gry == 2:
    print("ble")
    gramy()
    
