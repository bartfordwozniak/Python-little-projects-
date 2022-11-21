
#niedokoczony jeden tryb gry


import random as r

def introduction():
    print ("Hej,...yyyy\n")
    name = input = ("Podaj swoje imię:\n")
    print ("Hej," + name + "\n")
    return NULL

def mode_choosing():    
    print ("Chcesz zgadywać czy wybrać liczbę?\n")
    mode = input ("  1. Zgadywać\n  2. Wybieram liczbę\n")
    if mode != 1 or 2:
        mode = input("Zła odpowidź. Podaj liczbę 1 lub 2. \nPodanie innej odpowiedzi zakończy grę.\n")
    return (mode)

def player_is_guessing():
    goal = r.randint(0,100)
    answear = -1
    trys = 1 
    while answear != goal:
        answear = input ("Twoja myśl?\n")
        trys += 1
    if answear > goal:
        print("szukana liczba jest mniejsza")
        
    if answear < goal:
        print("szukana liczba jest większa")
        
    elif answear == goal:
        print("gg. zajeło ci to" + trys + "prób")

def ai_is_guessing():
    for x in range(0,100):
        TAB[x] = x
    a = 0
    b = 100
    
    while player_num != guess:
        guess = (TAB[a] + TAB[b])/2
        player_numb = input("czy" + guess + "to twoja liczba?\n 1. Tak\n 2. Nie\n")
    
        if player_numb == 1:
            print("super.gg")
        elif player_numb == 2:
            high = input("CZy większa?\n 1. Tak\n 2. Nie")
            if high == 1:
                print ("khem")

mode_choosing()

if mode == 1:
    player_is_guessing()
    
elif mode == 2:
    ai_is_guessing() 
