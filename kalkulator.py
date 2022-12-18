import tkinter as tk
import math

# Funkcja obliczająca wynik działania
def oblicz():
  # Pobieranie danych wejściowych z pól tekstowych
  a = float(pole_a.get())
  b = float(pole_b.get())
  dzialanie = pole_dzialanie.get()
  # Obliczanie wyniku
  if dzialanie == "+":
    wynik = a + b
  elif dzialanie == "-":
    wynik = a - b
  elif dzialanie == "*":
    wynik = a * b
  elif dzialanie == "/":
    wynik = a / b
  elif dzialanie == "^":
    wynik = a ** b
  elif dzialanie == "log":
    wynik = math.log(a, b)
  elif dzialanie == "sqrt":
    wynik = math.sqrt(a)
  elif dzialanie == "sin":
    wynik = math.sin(a)
  # Wyświetlanie wyniku w polu tekstowym
  pole_wynik.delete(0, tk.END)
  pole_wynik.insert(0, str(wynik))

# Tworzenie okna głównego
okno = tk.Tk()
okno.title("Kalkulator naukowy")

# Tworzenie pól tekstowych
pole_a = tk.Entry(okno)
pole_b = tk.Entry(okno)
pole_dzialanie = tk.Entry(okno)
pole_wynik = tk.Entry(okno)

# Tworzenie przycisków
przycisk_oblicz = tk.Button(okno, text="Oblicz", command=oblicz)

# Umieszczanie elementów w oknie
ppole_b.grid(row=0, column=2)
przycisk_oblicz.grid(row=1, column=1)
pole_wynik.grid(row=2, column=1)

# Uruchomienie pętli głównej
okno.mainloop()
