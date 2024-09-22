"""Phone inventory vol 2."""


def add_phone_quantity(phone_info: tuple, update: tuple) -> tuple:
    """
    Update tuple, if updated data brand and model exist.

    Given a tuple containing a phone brand, its models, and quantities,
    and an update tuple, return the updated data or empty tuple if brand and/or model doesn't exist.
    """
    # enniku muutuja jargi jaotamine
    brand, model_list, quantity_tuple = phone_info
    second_brand, second_model, second_quantity = update

    if second_brand == brand:
        if second_model in model_list:
            model_index = model_list.index(second_model)  # leiab mudeli indexi esimene voi teine

            # quanity muudab listiks et seda saaks muuta
            quantity_list = list(quantity_tuple)

            # uuuenda quanity vastavalt kas on esimene voi teine mudel
            quantity_list[model_index] += second_quantity

            # quanity list tagasi tupleks
            updated_quantity_tuple = tuple(quantity_list)

            # tagasta data uuendatud kogusega
            return (brand, model_list, updated_quantity_tuple)
    return ()


def highest_quantity_brand(phones: list[tuple]) -> str:
    """
    Find brand with most models.

    Given a tuple containing phone brand data, return the brand with the highest total quantity of models.
    If there is a tie, return the one that appears first in the input list.
    """
    max_quantity = 0
    max_brand = ""

    for brand, models, quantities in phones:
        total_quantity = sum(quantities)  # arvutab uhe brandi kogu koguse

        if total_quantity > max_quantity:  # kui see kogus on suurem kui eelmisel uuendab muutujaid kui ei laheb lic jargmise juurde
            max_quantity = total_quantity
            max_brand = brand

    return max_brand


def phone_list_as_string(phone_list: list) -> str:
    """
    Create a list of phones.

    The input list is in the same format as the result of phone_brand_and_models function.
    The order of the elements in the string is the same as in the list.
    """
    phones = []  # paneb koik listi et telefone ei tuleks uuesti sarnaseid
    result = []  # mis lopus returnitakse

    for brand, models in phone_list:
        for model in models:
            phone = f"{brand} {model}"  # uheks soneks
            if phone not in phones:  # kontrollib et ei tuleks kahte sama telefoni
                phones.append(phone)
                result.append(phone)

    return ",".join(result)  # Join the entries with commas


if __name__ == '__main__':
    print(add_phone_quantity(("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                             ("Apple", "iPhone 11", 1)))
    # ("Apple", ["iPhone 11", "iPhone 12"], (501, 300))

    print(add_phone_quantity(("Apple", ["iPhone 11", "iPhone 12"], (500, 300)), ("Nokia", "3310", 10)))
    # ()

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (500, 300)),
                                  ("Samsung", ["Galaxy S20", "Galaxy S21"], (600, 400)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (200, 100))]))
    # Samsung

    print(highest_quantity_brand([("Apple", ["iPhone 11", "iPhone 12"], (100, 50)),
                                  ("Samsung", ["Galaxy S20", "Galaxy S21"], (110, 40)),
                                  ("Google", ["Pixel 4", "Pixel 5"], (70, 30))]))
    # Apple

    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))
    # IPhone 11,Google Pixel
    print(phone_list_as_string([['IPhone', ['11']], ['Google', ['Pixel']]]))
    # IPhone 11,Google Pixel
    print(phone_list_as_string([['HTC', ['one']]]))
    # HTC one
