#!/usr/bin/python3

#Adrian Kucharski

def kalkulator():
    print("Wybierz operację:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    
    wybor = input("Podaj numer operacji: ")
    
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    
    if wybor == '1':
        print(f"Wynik: {a} + {b} = {a + b}")
    elif wybor == '2':
        print(f"Wynik: {a} - {b} = {a - b}")
    elif wybor == '3':
        print(f"Wynik: {a} * {b} = {a * b}")
    elif wybor == '4':
        if b != 0:
            print(f"Wynik: {a} / {b} = {a / b}")
        else:
            print("Błąd: Dzielenie przez zero!")
    else:
        print("Nieprawidłowy wybór!")

if __name__ == "__main__":
    kalkulator()
