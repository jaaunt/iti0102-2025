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


def remove_unnecessary_chars(number: str) -> str:
    """Remove unnecessary characters from number."""
    has_code = number.startswith("+") and " " in number  # vaatab kas on voimalik koha kood
    nr_part = ""
    code_part = ""
    for char in number:
        if char.isdigit():
            if has_code:
                code_part += char
            else:
                nr_part += char
        elif char == " ":
            if has_code and code_part:  # kui on maakonna kood ja koodi osas on numbrid muudel juhtudel ei tee midagi
                code_part += char  # lisab selle tuhiku
                has_code = False  # lopetab koodi ossa nr lugemise
            continue

    if code_part and nr_part:  # kui molemad osad pole tuhi str ss paneb koha koodi ette pluss
        return "+" + code_part + nr_part
    else:  # muudel juhtudel lihtsalt liidab koik numbrid
        return code_part + nr_part


def get_last_numbers(numbers: list[str], n: int) -> list[str]:
    """Get last numbers of the list."""
    if n <= 0:
        return []
    elif n >= len(numbers):
        return numbers
    else:
        return numbers[-n:]


if __name__ == '__main__':
    print(add_country_code("1234567"))  # "1234567" => "+372 1234567"
    print(add_country_code("+372 1234567"))  # "+372 1234567" => "+372 1234567"

    print(is_valid("+372 1234567"))  # "+372 1234567" => True
    print(is_valid("+1 1234567"))  # "+1 1234567" => True
    print(is_valid("+3721234567"))  # "+3721234567" => False
    print(is_valid("+372 123456"))  # "+372 123456" => False
    print(is_valid("+372A12345*7"))  # "+372A12345*7" => False

    print(remove_unnecessary_chars("+372 *1234567a"))  # "+372 *1234567a" => "+372 1234567"
    print(remove_unnecessary_chars("+++37ooo2 1234+AAA567"))  # "+++37ooo2 1234+AAA567" => "+372 1234567"
    print(remove_unnecessary_chars(" 123+h n456!7"))  # " 123+h n456!7" => "1234567"
    print(remove_unnecessary_chars("+abc 55fd"))  # "+abc 55fd" => "55"
    print(remove_unnecessary_chars("+abc   ++ "))  # "+abc   ++ " => ""
    print(remove_unnecessary_chars("+372 adbbcc%$"))  # "+372 adbbcc%$" => "372"

    print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 2))  # ["+372 1234567", "1234567", "+1 234567890"], 2 => ["1234567", "+1 234567890"]
    print(get_last_numbers(["+372 1234567"], 3))  # ["+372 1234567"], 3 => ["+372 1234567"]
    print(get_last_numbers(["+372 1234567", "1234567", "+1 234567890"], 0))  # ["+372 1234567", "1234567", "+1 234567890"], 0 => []
