from zadanie_domowe.count_status import count_status
from zadanie_domowe.count_status import statuses

#def test_count_status():
 #   assert count_status(statuses, "online") == 2

def test_count_status():
    assert count_status(statuses, "offline") == 1

