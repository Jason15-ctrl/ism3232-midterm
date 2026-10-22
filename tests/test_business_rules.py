from business_rules import (
    calculate_room_cost,
    calculate_stay_total,
    format_stay_line,
    get_stay_discount,
    gets_welcome_package,
    largest_stay,
    requires_credit_check,
    total_reserved,
)


def test_room_cost():
    assert round(calculate_room_cost(100.00, 3), 2) == 300.00


def test_discount_under_4_nights():
    assert get_stay_discount(3) == 0.0


def test_discount_4_nights():
    assert get_stay_discount(4) == 0.06


def test_discount_13_nights():
    assert get_stay_discount(13) == 0.06


def test_discount_14_nights():
    assert get_stay_discount(14) == 0.18


def test_discount_corporate():
    assert get_stay_discount(2, True) == 0.06


def test_cleaning_fee_under_limit():
    assert round(calculate_stay_total(100.00, 2), 2) == 240.00


def test_cleaning_fee_at_limit():
    assert round(calculate_stay_total(150.00, 2), 2) == 340.00


def test_cleaning_fee_over_limit():
    assert round(calculate_stay_total(150.50, 2), 2) == 301.00


def test_credit_check():
    assert requires_credit_check(2500.00) is True


def test_credit_check_under():
    assert requires_credit_check(1999.99) is False


def test_credit_check_boundary():
    assert requires_credit_check(2000.00) is True


def test_welcome_package_under_nights():
    assert gets_welcome_package(5, 1500) is False


def test_welcome_package_over_nights():
    assert gets_welcome_package(6, 1500) is True


def test_welcome_package_under_total():
    assert gets_welcome_package(6, 999.99) is False


def test_welcome_package_boundary_total():
    assert gets_welcome_package(6, 1000) is True


def test_total_reserved():
    recs = [
        {"nightly_rate": 100.00, "nights": 2},
        {"nightly_rate": 150.00, "nights": 2},
    ]
    assert round(total_reserved(recs), 2) == 580.00


def test_largest_stay():
    stays = [
        {"guest": "A", "nightly_rate": 100, "nights": 2},
        {"guest": "B", "nightly_rate": 150, "nights": 3},
    ]
    assert largest_stay(stays) == "B"


def test_largest_stay_tie():
    stays = [
        {"guest": "A", "nightly_rate": 100, "nights": 2},
        {"guest": "B", "nightly_rate": 100, "nights": 2},
    ]
    assert largest_stay(stays) == "A"


def test_largest_stay_empty():
    stays = []
    assert largest_stay(stays) == ""


def test_format_stay_line():
    line = format_stay_line("A", 1000.00, True, False)
    assert line == "A: $1000.00 | credit check: yes | welcome package: no"


def test_format_stay_line_opposite():
    line = format_stay_line("B", 500.00, False, True)
    assert line == "B: $500.00 | credit check: no | welcome package: yes"
