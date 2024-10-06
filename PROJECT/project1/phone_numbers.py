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


def get_first_correct_number(names: list[str], numbers: list[str], name: str) -> str | None:
    """Get the first valid number for a name from the list."""
    for i in range(0, len(numbers)):
        if names[i].lower() in name.lower():
            if is_valid(numbers[i]):
                return numbers[i]
    return None


def correct_numbers(numbers: list[str]) -> list[str]:
    """Check if number is correct and try to fix it if it isnt."""
    fixed_numbers = []
    for number in numbers:
        clean_number = remove_unnecessary_chars(number)
        if clean_number and is_valid(clean_number):  # on puhastatud ja valid nr
            fixed_numbers.append(clean_number)
        elif clean_number and len(clean_number) >= 7 and " " not in clean_number:  # ei sisalda uleliigseid asju on at least 7 pikk ja ei sisalda " "
            fixed_numbers.append(add_country_code(clean_number))
    return fixed_numbers


def get_names_of_contacts_with_correct_numbers(names: list[str], numbers: list[str]) -> list[str]:
    name_valid_nr = []
    for i in range(0,len(numbers)):
        if is_valid(numbers[i]):
            name_valid_nr.append(namesvvv[i])
    return name_valid_nr


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

    print(get_first_correct_number(["Alice Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"], "Alice Smith"))
    # ["Alice Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"], "Alice Smith" => "+372 1234567"
    print(get_first_correct_number(["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith"))
    # ["alice Smith", "Alice Smith", "ALICE Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234567890", "+44 1234567"], "Alice Smith" => "+1 234567890"
    print(get_first_correct_number(["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "Alice Smith"))
    # ["Alice Smith", "Alice Smith", "Alice Smith", "Alice Smith"], ["555-1234", "+372 123456", "+1 234-567890", "+44 123AA567"], "Alice Smith" => None

    print(correct_numbers(["+372 12345", "1234567", "+111 23456789", "456"]))
    # ["+372 12345", "1234567", "+111 23456789", "456"] => ["+372 1234567", "+111 23456789"]
    print(correct_numbers(["1234567", "+1 234567890", "5551234", "+372 51234567", "+372 59876543"]))
    # ["1234567", "+1 234567890", "5551234", "+372 51234567", "+372 59876543"] => ["+372 1234567", "+1 234567890", "+372 5551234", "+372 51234567", "+372 59876543"]
    print(correct_numbers(["+372 123456", "+44 1234567AAA", "555-1234"]))
    # ["+372 123456", "+44 1234567AAA", "555-1234"] => ["+44 1234567", "+372 5551234"]
    print(correct_numbers(["555-1234", "123", "AAAAA"]))
    # ["555-1234", "123", "AAAAA"] => ["+372 5551234"]
    print(correct_numbers(["5234", "123", "A8AA", "+1 12345"]))
    # ["5234", "123", "A8AA", "+1 12345"] => []

    print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"]))
    # ["ALICE Smith", "Bob Brown", "Carol White"], ["+372 1234567", "555-1234", "+1 234567890"] => ["Alice Smith", "Carol White"]
    print(get_names_of_contacts_with_correct_numbers(["Alice Smith", "Bob Brown", "Carol White"], ["+372 123456", "555-1234", "*1 234567890"]))
    # ["Alice Smith", "Bob Brown", "Carol White"], ["+372 123456", "555-1234", "*1 234567890"] => []
    print(get_names_of_contacts_with_correct_numbers(["ALICE Smith", "Bob Brown", "alice smith"], ["+372 1234567", "555-1234", "+1 234567890"]))
    # ["ALICE Smith", "Bob Brown", "alice smith"], ["+372 1234567", "555-1234", "+1 234567890"] => ["Alice Smith", "Alice Smith"]
