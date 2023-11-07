"""
Jūsų rankose dvi dėžutės, kurių išoriniai matmenys yra a1, b1, c1 ir a2, b2, c2. 
Matmenys yra sveikieji skaičiai, neviršijantys 100. 
Viena dėžutė telpa į kitą, jeigu jos matmenys nors vienu vienetu yra mažesni užkitos dėžutės atitinkamus matmenis. 
Dėžutes galima vartyti. Galimos kelios situacijos: pirmoji telpa antrojoje, antroji telpa pirmojoje, 
abi vienodų matmenų, dėžutės nepalyginamos. Parašykite programą dviem dėžutėms palyginti
"""

a1 = int(input("Įveskite pirmos dėžutės a matmenį: "))
b1 = int(input("Įveskite pirmos dėžutės b matmenį: "))
c1 = int(input("Įveskite pirmos dėžutės c matmenį: "))
a2 = int(input("Įveskite antros dėžutės a matmenį: "))
b2 = int(input("Įveskite antros dėžutės b matmenį: "))
c2 = int(input("Įveskite antros dėžutės c matmenį: "))

dezes1 = sorted([a1, b1, c1])
dezes2 = sorted([a2, b2, c2])

if dezes1[0] < dezes2[0] and dezes1[1] < dezes2[1] and dezes1[2] < dezes2[2]:
    print('Pirmoji dėžė telpa antrojoje')
elif dezes2[0] < dezes1[0] and dezes2[1] < dezes1[1] and dezes2[2] < dezes1[2]:
    print('Antroji dėžė telpa pirmojoje')
elif dezes1 == dezes2:
    print('Abi dėžutės turi vienodus matmenis')
else:
    print('Dėžutės nepalyginamos')