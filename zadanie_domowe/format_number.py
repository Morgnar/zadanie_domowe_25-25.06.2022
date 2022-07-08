"""
1.1 Separatory tysięcy
Napisz funkcję format_number, która przyjmie nieujemne liczby i zwróci napis, w którym liczba
będzie sformatowana tak, by tysiące były rozdzielane przecinkiem
assert format_number(1000000) == '1,000,000'
"""


def format_number(cyfra):
    cyfra_nowa = int(cyfra)
    print(f"{cyfra_nowa:,}")
    return cyfra_nowa


print(type(format_number(1343423200000)))
print(str(format_number(1343423200000)))