# business_rules.py

MIN_NIGHTS = 4
LONG_STAY_NIGHTS = 14
REGULAR_DISCOUNT = 0.06
LONG_STAY_DISCOUNT = 0.18
NO_DISCOUNT = 0.0
CLEANING_FEE = 40.0
CLEANING_LIMIT = 300.0
CREDIT_CHECK_LIMIT = 2000.0
WELCOME_PACKAGE_MIN_NIGHTS = 5
WELCOME_PACKAGE_MIN_TOTAL = 1000.0


def calculate_room_cost(nightly_rate: float, nights: int) -> float:
    """Returns the room cost before any discount"""
    return nightly_rate * nights


def get_stay_discount(nights: int, corporate: bool = False) -> float:
    """Returns the discount percentage based on the number of nights and corporate status"""
    if nights >= LONG_STAY_NIGHTS:
        return LONG_STAY_DISCOUNT
    elif nights >= MIN_NIGHTS or corporate:
        return REGULAR_DISCOUNT
    else:
        return NO_DISCOUNT


def calculate_stay_total(
    nightly_rate: float, nights: int, corporate: bool = False
) -> float:
    """Returns the total cost of the stay after applying any applicable discounts"""
    room_cost = calculate_room_cost(nightly_rate, nights)
    discount = get_stay_discount(nights, corporate)
    discounted = room_cost * (1 - discount)
    if discounted <= CLEANING_LIMIT:
        return discounted + CLEANING_FEE
    return discounted


def requires_credit_check(total: float) -> bool:
    """Returns True if the total cost meets or exceeds the credit check limit, otherwise False"""
    return total >= CREDIT_CHECK_LIMIT


def gets_welcome_package(nights: int, total: float) -> bool:
    """Returns True if the guest is eligible for a welcome package, otherwise False"""
    return nights > WELCOME_PACKAGE_MIN_NIGHTS and total >= WELCOME_PACKAGE_MIN_TOTAL


def total_reserved(stays: list) -> float:
    """Returns the total cost of all stays in the list"""
    total = 0.0

    for stay in stays:
        total += calculate_stay_total(
            stay["nightly_rate"], stay["nights"], stay.get("corporate", False)
        )
    return total


def largest_stay(stays: list) -> str:
    """Returns the name of the guest with the largest total stay cost"""
    largest = 0.0
    largest_guest = ""

    for stay in stays:
        nightly_rate = stay["nightly_rate"]
        nights = stay["nights"]
        corporate = stay.get("corporate", False)
        total = calculate_stay_total(nightly_rate, nights, corporate)
        if total > largest:
            largest = total
            largest_guest = stay["guest"]

    return largest_guest


def format_stay_line(
    guest: str, total: float, credit_check: bool, welcome_package: bool
) -> str:
    """Returns a formatted string for the stay line"""
    credit_check_str = "no"
    if credit_check:
        credit_check_str = "yes"

    welcome_package_str = "no"
    if welcome_package:
        welcome_package_str = "yes"

    return f"{guest}: ${total:.2f} | credit check: {credit_check_str} | welcome package: {welcome_package_str}"
