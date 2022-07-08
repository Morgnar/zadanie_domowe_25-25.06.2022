"""
1.2 mid
Napisz funkcję, która zwróci z napisu środkowy znak lub pusty napis, jeśli nie ma środkowego
znaku:
assert "b" == mid("abc")
assert "" == mid("abbc")
"""


def mid(tekst):
    tekst2 = tekst.replace(" ", "")
    x = len(tekst2)
    print(tekst2)

    if x % 2 == 0:
        print("Parzysta liczba liter - brak środkowego znaku!")
        return print("")

    else:
        print("Nieparzysta liczba - mozna wyznaczyc znak srodkowy")
        znak_mid = ((x - 1) / 2) + 1
        y = int(znak_mid)
        z = tekst2[y - 1]
        return print(z)
            #f"Znakiem srodkowym podanego tekstu jest: {tekst2[y - 1]}"


mid('aabaa')
mid('asj dsk fdas lfh')
