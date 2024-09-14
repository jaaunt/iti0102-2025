"""Control number."""


def control_number(encrypted_string: str) -> bool:
    """
    Given encrypted string that has a control number in the end of it, return True if correct, else False.

    Calculating the correct control number:
    1. Start the calculation from 0.
    2. Add 1 for every lowercase occurrence.
    3. Add 2 for every uppercase occurrence.
    4. Add 5 for any of the following symbol occurrences: "?!@#".
    Other symbols/letters/digits don't affect the result.

    NB! If for example the number you come up with is 25, you only have to check the last two digits of the string.
    e.g. control_number("?!?!#4525") -> True, because it ends with 25.

    :param encrypted_string: encrypted string
    :return: validation
    """
    ctrl_num = 0  # kontroll number
    spc_symbols = "?!@#"   # sumbolid mis lisavad vaartusi

    for char in encrypted_string:
        if char.islower():
            ctrl_num += 1  # kui on lowercase lisab kontroll numbrile 1
        elif char.isupper():
            ctrl_num += 2  # kui on uppercase lisab 2
        elif char in spc_symbols:
            ctrl_num += 5  # kui on sumbolite sones siis lisab 5 numbrile
        else:
            ctrl_num += 0

    # kontrollib kontroll numbri pikkust
    ctrl_num_lenght = len(str(ctrl_num))

    if ctrl_num_lenght == 2 and encrypted_string[-2:].isdigit():  # kontrollib loppeks 2 numbriga
        last_digit = int(encrypted_string[-2:])  # votab kaks viimast numbrit
        last_ctr = ctrl_num % 100  # votab 2 viimast kontroll numbrist
    elif ctrl_num_lenght >= 1 and encrypted_string[-1:].isdigit():  # sama asi aga kui lopus on ainult 1 number
        last_digit = int(encrypted_string[-1:])
        last_ctr = ctrl_num % 10
    else:
        return False
    return last_ctr == last_digit


if __name__ == '__main__':
    print(control_number("mE0W5"))  # True
    print(control_number("SomeControlNR?20"))  # False
    print(control_number("False?Nr9"))  # False
    print(control_number("#Hello?!?26"))  # True
    print(control_number("3423982340000000.....///....0"))  # True
    print(control_number("#Shift6"))  # False
