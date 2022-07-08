"""
1.5 angram
stwórz funkcję, która sprawdzi, czy dwa teksty są anagramami
assert is_anagram("typhoon", "opython") == True
assert is_anagram("Alice", "Bob") == False

"""


def is_anagram(tekst1, tekst2):
    x = sorted(tekst1)
    y = sorted(tekst2)

    if x == y:
        return True
    else:
        return False


print(is_anagram("bokej", "jebok"))
print(is_anagram("askjf", "akjsbf"))
