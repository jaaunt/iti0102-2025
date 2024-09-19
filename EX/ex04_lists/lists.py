"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).
    """
    return all_phones.split(",")


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).
    """
    return []


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).
    """
    return []


def search_by_brand(all_phones: str, brand: str) -> list:
    """
    Search for phones by brand.

    The search is case-insensitive.
    """
    return []


def search_by_model(all_phones: str, model: str) -> list:
    """
    Search for phones by model.

    The search is case-insensitive.
    """
    return []


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

