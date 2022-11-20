import time

points = 5
health = 1
stamina = 1
intelig = 1

input ("\t\t MENU \nKreator postaci ble ble role.\n Kliknij ENTER by kontynuować")


while points != 0:
    print("\n Pozostałych punktów: ", points)
    choice = int(input("""

           1. Dodaj punkt w zdrowie
           2. Dodaj punkt w kondycję
           3. Dodaj punkt w inteligencję
           4. Usuń pkt w zdrowie
           5. Usuń pkt w kon.
           6. Usuń pkt w inteligen.

           Co chcesz zrobić?\n"""))

    
    if (choice == 1):
        health += 1
        points -= 1
        
    elif (choice == 2):
        stamina += 1
        points -= 1
        
    elif (choice == 3):
        intelig += 1
        points -= 1

    elif (choice == 4):
        health -= 1
        points += 1
        
    elif (choice == 5):
        stamina -= 1
        points += 1
        
    elif (choice == 6):
        intelig -= 1
        points += 1

    else:
        print("nie ma takiej opcji")
        time.sleep(1.5)

    print("Obecne zdrowie:", health )
    print("Obecne kondycja:",  stamina )
    print("Obecna inteligencja:", intelig )

print ("\nWszystkie punkty zostały rozdane")
input ("ble ble ENTER daej!")

