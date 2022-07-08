"""
1.3 check online statues
Napisz funkcję, która zliczy ile osób ma zadany status
statuses = {
"Alice": "online",
"Bob": "offline",
"Eve": "online",
}
assert count_status(statuses, "online") == 2
assert count_status(statuses, "offline") ==

"""


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Luke": "",

}


def count_status(statuses, status):
    licznik = 0
    for index in statuses:
        if statuses[index] == status:
            licznik += 1

    return licznik


count_status(statuses, "online")
