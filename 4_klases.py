"""
Giraitės mokykloje yra keturios dešimtos klasės: a, b, c ir d. 
Direktorius atlieka analizę, nori surasti geriausiai besimokančią dešimtokų klasę, 
pasižiūrėti, keliais balais kiekvienos kitos klasės vidurkis yra mažesnis už geriausiai besimokančios klasės vidurkį.
Parašykite programą, kuri surastų, koks yra didžiausias vidurkis ir keliais balais skiriasi likusių klasių vidurkiai 
nuo geriausiai besimokančios klasės vidurkio.
"""

a = float(input('Iveskite pirma skaiciu: '))
b = float(input('Iveskite antra skaiciu: '))
c = float(input('Iveskite trecia skaiciu: '))
d = float(input('Iveskite ketvirta skaiciu: '))

didziausias_vidurkis = max(a, b, c, d)
skirtumas_a = didziausias_vidurkis - a 
skirtumas_b = didziausias_vidurkis - b 
skirtumas_c = didziausias_vidurkis - c 
skirtumas_d = didziausias_vidurkis - d 

print('Didziausias vidurkis: ', didziausias_vidurkis)

if skirtumas_a == 0:
    print('Kitu klasiu vidurkiai skiriasi: ', skirtumas_b, skirtumas_c, skirtumas_d)
elif skirtumas_b == 0:
    print('Kitu klasiu vidurkiai skiriasi: ', skirtumas_a, skirtumas_c, skirtumas_d)
elif skirtumas_c == 0:
    print('Kitu klasiu vidurkiai skiriasi: ', skirtumas_a, skirtumas_b, skirtumas_d)
elif skirtumas_d == 0:
    print('Kitu klasiu vidurkiai skiriasi: ', skirtumas_a, skirtumas_b, skirtumas_c)

