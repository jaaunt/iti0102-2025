"""Project 1"""
def add_country_code(number: str) -> str:
    if not "+" in number:
        return "+372 " + number
    return number

if __name__ == '__main__':
    print(add_country_code("1234567"))  # "1234567" => "+372 1234567"
    print(add_country_code("+372 1234567"))  # "+372 1234567" => "+372 1234567"