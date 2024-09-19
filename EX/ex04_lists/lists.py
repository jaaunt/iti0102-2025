"""Phone inventory."""
from pip._internal import models


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    if not all_phones:  # kui on tuhi ss annab tuhja hulga
        return []

    return all_phones.split(",")  # loikab sone komakohtadest eri osadeks


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    """
    if not all_phones:
        return []

    phones = all_phones.split(",")
    brands = []

    for phone in phones:
        if phone not in brands:
            brands.append(phone)
    return brands


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    if not all_phones:
        return []

    phones = all_phones.split(",")
    models = []

    for phone in phones:
        if " " in phone:
            brand, model = phone.split(" ", 1)
            if model not in models:
                models.append(model)
    return models


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    if not all_phones:
        return []

    phones = all_phones.split(",")
    brand_lower = brand.lower()
    matched_phones = []

    for phone in phones:
        if " " in phone:
            phone_brand,_ = phone.split(" ", 1)
            if phone_brand.lower() == brand_lower.lower():
                matched_phones.append(phone)

    return matched_phones


def search_by_model(all_phones: str, model: str) -> list:
    """
    Search for phones by model.

    The search is case-insensitive.
    """
    if not all_phones:
        return []

    phones = all_phones.split(",")
    search_model_lower = model.lower()
    matched_phones = []
    for phone in phones:
        if " " in phone:
            _, model = phone.split(" ", 1)  # telefoni brandist eraldamine
            model_parts = model.split(" ")  # loikab lahti juhul kui nt on 12 pro saab 12, pro
            model_parts_lower = [part.lower() for part in model_parts]  # teeb koik listis olevad vaartused vaikeste tahtedega
            if search_model_lower in model_parts_lower:
                matched_phones.append(phone)

    return matched_phones


if __name__ == '__main__':
    print(list_of_phones("Google Pixel,Honor Magic5,Google Pixel"))
    # ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    print(phone_brands("Google Pixel,Honor Magic5,Google Pix,Honor Magic6,IPhone 12,Samsung S10,Honor Magic,IPhone 11"))
    # ['Google', 'Honor', 'IPhone', 'Samsung']
    print(phone_brands("Google Pixel,Google Pixel,Google Pixel,Google Pixel"))
    # ['Google']
    print(phone_brands(""))
    # []
    print(phone_models("IPhone 14,Google Pixel,Honor Magic5,IPhone 14"))
    # ['14', 'Pixel', 'Magic5']
    print(phone_models("IPhone 14 A,Google Pixel B,Honor Magic5,IPhone 14"))
    # ['14 A', 'Pixel B', 'Magic5', '14']
    print(phone_models("LG Optimus Black"))
    # ['Optimus Black']
    print(search_by_brand("IPhone X,IPhone 12 Pro,IPhone 14 pro Max", "iphone"))
    # ['IPhone X', 'IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "pro"))
    # ['IPhone 12 Pro', 'IPhone 14 pro Max']
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "1"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "IPhone"))
    # []
    print(search_by_model("IPhone proX,IPhone 12 Pro,IPhone 14 pro Max", "12 Pro"))
    # []
