#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

liczba = random.randint(1, 10)
#print("Wylosowana liczba: ", liczba)

for i in range(3):
    print("Próba", i + 1)
    odp = input("Jaką liczbę od 1 do 10 mam na myśli? Podaj liczbę: ")
    #print("Podałeś liczbę: ", odp)

    if liczba == odp:
        print("Brawo! Odgadłeś liczbę!")
        brake
    elif i == 2:
        print("Miałem na myśli liczbę", liczba)
    else:
        print("Niestety, nie udało się :( Podana liczba nie jest prawidłowa. Spróbuj jeszcze raz! :)")
