"""
1.4 double letters
Stwórz funkcję, która sprawdzi, czy w zadanym tekście dwa identyczne znaki sąsiadują ze sobą
1
assert double_letters("ala") == False
assert double_letters("Hello") == True
assert double_letters("abc") == False
assert double_letters("nono") == False

"""
# Funkcja która by przy każdym kolejnym obrocie sprawdzała czy bierząca litera jest taka sama jak poprzednia..


def double_letters(tekst):
    x = len(tekst)
    zmienna = "NO"
    for i in range(0,x-1):
        if tekst[i] == tekst[i+1]:
            zmienna = "YES"

    if zmienna == "NO":
        return False
    elif zmienna == "YES":
        return True



print(double_letters("nono"))
print(double_letters("hello"))