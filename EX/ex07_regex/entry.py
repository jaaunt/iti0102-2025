"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first name, last name, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first name and last name begin with a capital letter and are followed by at least one lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the first part
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    name_pattern = r"([A-Z][a-z]+)([A-Z][a-z]+)"  # first and last name
    id_pattern = r"(\d{11})"  # id kood 11 nr
    phone_pattern = (r"(\+\d{3}"  # area kood
                     r"\s*"  # tuhik nende vahel
                     r"\d{7,8})")  # nr osa
    date_pattern = r"(\d{2}-\d{2}-\d{4})"

    # otsib koiki neid str-ist
    name_match = re.search(name_pattern, row)  # find all kuna ees ja pere nimi
    id_code_match = re.search(id_pattern, row)
    phone_match = re.search(phone_pattern, row)
    date_match = re.search(date_pattern, row)

    first_name = name_match.group(1) if name_match else None
    last_name = name_match.group(2) if name_match else None
    id_code = id_code_match.group(0) if id_code_match else None
    phone_number = phone_match.group(0) if phone_match else None
    date = date_match.group(0) if date_match else None

    if phone_number is None:  # if theres no nr with area code maybe theres one without area code
        phone_row = row.replace(id_code, "")
        phone_pattern_no_code = r"\d{7,8}"
        phone_match_no_code = re.search(phone_pattern_no_code, phone_row)
        phone_number = phone_match_no_code.group(0) if phone_match_no_code else None

    address_start = 0
    if name_match:  # kui midagi on olemas vaatab kaugust ja kas see oli kaugemal et enne et ei hakataks lugema liiga vara
        address_start = name_match.end()
    if id_code_match:
        address_start = max(address_start, id_code_match.end())
    if phone_match:
        address_start = max(address_start, phone_match.end())
    if date_match:
        address_start = max(address_start, date_match.end())

    adress = row[address_start:]  # teeb substring rowst alates leitud adressi algus punktist
    if not adress:
        adress = None

    return first_name, last_name, id_code, phone_number, date, adress


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # (None, None, '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
