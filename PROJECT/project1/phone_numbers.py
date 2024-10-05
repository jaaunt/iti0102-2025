"""Project 1."""


def add_country_code(number: str) -> str:
    """Add country code to number."""
    if not number.startswith('+'):
        return "+372 " + number
    return number


def is_valid(number: str) -> bool:
    """Check if number is valid."""
    if not number.startswith('+'):
        return False
    if " " in number:
        parts = number.split(" ", 1)
        if (parts[0].isdigit or "+") and len(parts[1]) >= 7 and parts[1].isdigit():
            return True
    return False


if __name__ == '__main__':
    print(add_country_code("1234567"))  # "1234567" => "+372 1234567"
    print(add_country_code("+372 1234567"))  # "+372 1234567" => "+372 1234567"

    print(is_valid("+372 1234567"))  # "+372 1234567" => True
    print(is_valid("+1 1234567"))  # "+1 1234567" => True
    print(is_valid("+3721234567"))  # "+3721234567" => False
    print(is_valid("+372 123456"))  # "+372 123456" => False
    print(is_valid("+372A12345*7"))  # "+372A12345*7" => False
