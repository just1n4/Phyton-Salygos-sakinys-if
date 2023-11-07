"""
Duoti du skaičiai. Didesniojo skaičiaus reikšme reikia priskirti kintamajam DID, 
o mažesniojo –kintamajam MAZ. 
Jei skaičiai lygūs išveskite atitinkamą pranešimą.
"""

Skaicius1 = int(input('Iveskite pirmą skaiciu: '))
Skaicius2 = int(input('Iveskite antrą skaiciu: '))
if Skaicius1 > Skaicius2:
    did = Skaicius1
    maz = Skaicius2
    print(f'{did} yra didesnis skaicius negu {maz}')
elif Skaicius1 < Skaicius2:
    maz = Skaicius1
    did = Skaicius2
    print(f'{maz} yra mazesnis negu {did}')
else:
    print('Ivesti skaiciai lygus')