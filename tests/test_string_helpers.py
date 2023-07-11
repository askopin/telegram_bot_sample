from telegram_bot.helpers.string_helpers import clear_ranges, StringRange

def test_clears_single_range():
    assert clear_ranges("qwerty", [StringRange(0,1)]) == "werty"
    assert clear_ranges("qwerty", [StringRange(1,1)]) == "qerty"
    assert clear_ranges("qwerty", [StringRange(5,1)]) == "qwert"
    assert clear_ranges("qwerty", [StringRange(1,4)]) == "qy"
    assert clear_ranges("qwerty", [StringRange(0,6)]) == ""

def test_clears_empty_range():
    assert clear_ranges("qwerty", []) == "qwerty"
    assert clear_ranges("", []) == ""

def test_clears_range_from_empty_string():
    assert clear_ranges("", [StringRange(0,1)]) == ""
    assert clear_ranges("", [StringRange(0,1), StringRange(1,2)]) == ""
    
def test_clears_multiple_ranges():
    ranges = [
        StringRange(0,1),
        StringRange(1,1),
    ]

    assert clear_ranges("qwerty", ranges) == "erty"

    ranges = [
        StringRange(1,2),
        StringRange(4,1),
    ]

    assert clear_ranges("qwerty", ranges) == "qry"

def test_clears_multiple_ranges_in_random_order():
    ranges = [
        StringRange(4,1),
        StringRange(1,2)
    ]

    assert clear_ranges("qwerty", ranges) == "qry"