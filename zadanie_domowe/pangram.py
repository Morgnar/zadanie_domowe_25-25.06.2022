"""
1.11 pangram
Napisz funkcję, która sprawdzi, czy napis jest pangramem.

"""



#tekst = 'O mógłże sęp chlań wyjść furtką bździn'
#tekst = 'Chwyć małżonkę, strój bądź pleśń z fugi'
tekst = "Jadą, jadą misie"


def pangram(yes_or_no):
    alfabet = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó',
               'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
    tekst2 = tekst.lower()
    for i in alfabet:
        test = "NIE"
        if tekst2.count(i) >= 1:
            continue
        else:
            test = "TAK"
            break
    if test == "TAK":
        return False
    else:
        return True


print(pangram(tekst))