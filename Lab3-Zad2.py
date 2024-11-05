Liczba = 2
Licznik = 0
Liczba_pierwsza = []

while Licznik < 10:
    for i in range(2, Liczba):
        if Liczba % i == 0:
            break
    else:
        Liczba_pierwsza.append(str(Liczba))
        Licznik += 1
    Liczba += 1

print(",".join(Liczba_pierwsza))