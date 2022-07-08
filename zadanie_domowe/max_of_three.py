"""
1.7 max of three
Napisz funkcję (lub funkcje), która zwróci maksymalną spośród 3 liczb. W rozwiązrozwiązaniu skorzystaj
tylko z możliwośći definiowania funkcji i używania w nich operatorów porównania

"""


def max_of_three(x, y, z):
    top = 0
    if x > y:
        top = x
        if z > top:
            top = z
            return top
        else:
            return top

    else:
        top = y
        if z > top:
            top = z
            return top
        else:
            return top


print(max_of_three(34, 122, 25))
