# Kto jest ojcem?

import time

vader = {"Bartosz" : "Robert",
         "Syn" : "Ojciec",
         "Luke" : "Vader"}
menu = 1
while menu != 0:
    quest = int(input ("""
1. Szukaj parę ojciec-syn
2. Zmien dane
3. Dodaj dane
4. Usun dane
0. Zakoncz
"""))
    if (quest == 1):
        term = input("\nJakie nazwisko wyszukać?")
        if term in vader:
            luke = vader[term]
            print("\n", term, " jego ojcem jest ", luke, ".\n")
        else:
            print("Brak danych.")

    elif (quest == 2):
        term = input("Jakie dane zmienić?")
        if term in vader:
            luke = input("Kto?")
            vader[term] = luke
            print("Zmieniono.")
        else:
            ("Termin nie istnieje w bazie danych.")

    elif (quest == 3):
        term = input("Dodawanie nowego połączenia.\nJakie dane syna (imię)? ")
        if term not in vader:
            luke = input("\nImię ojca?")
            vader[term] = luke

    elif (quest == 4):
        term = input("Kogo kropnąć szefie? (syn)")
        if term in vader:
            del vader[term]
            print(term," z ojcen nie ma już na liście.")
        else:
            print("Terminu nie ma na liście.")

    elif (quest == 0):
        menu = 0

print("Okej.....")
input("\nENTER to end")








            
