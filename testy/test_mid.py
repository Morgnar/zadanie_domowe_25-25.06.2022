from zadanie_domowe.mid import mid

def test_mid():
    assert mid('aabaa') == "b"


def test_mid():
    assert mid('asj dsk fdas lfh') == "f"


def test_mid():
    assert mid('asakdk') == ''