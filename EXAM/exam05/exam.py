"""Exam 5 (16.01.2025)."""


def count_digits(text: str) -> int:
    """
    Return the count of digits in a string.

    count_digits("123") => 3
    count_digits("a") => 0
    count_digits("") => 0
    count_digits("0a9r44") => 4
    """
    nr_amount = 0
    for char in text:
        if char.isdigit():
            nr_amount += 1
    return nr_amount


def capitalize_first_last_letters(text: str) -> str:
    """
    Take a string and capitalize the first and last letter of each word while keeping the rest of the letters in lowercase.

    capitalize_first_last_letters("hello") => "HellO"
    capitalize_first_last_letters("hello world") => "HellO WorlD"
    capitalize_first_last_letters("") => ""
    capitalize_first_last_letters("hello! 2024") => "Hello! 2024"

    word[-1] annab eraldi viimase tahe
    last_letter = word[-1].upper() viimane taht eraldi ja suur
    :param text: Input string in which you want to capitalize the first and last letters of each word. If there is a symbol after the letter, the letter is not capitalized.
    :return: Text where the size of the first and last letter of each word is changed.
    """
    # TERE => tere
    # x[0].lower() + x[1:].upper()
    words = text.split()
    result = ""
    # voi
    # result_list = []
    for word in words:
        word = word.capitalize()  #Hello
        last_letter = word[-1].upper()
        word = word[:-1] + last_letter  #Loikab viimase tahe maha ja lisab tehtud suure tahe
        result += word + " "  # tuhikud sonade vahele
        # result_list.append(word)
    # return " ".join(result_list)
    return result.rstrip()  # r strip votab paremalt tuhiku ara lopust

    # minu oma
    # capitalize_first = text.title()
    # words_listed = capitalize_first.split(" ")
    # fixed_words = ""
    # for word in words_listed:
    #     str = ""
    #     lenght = len(word)
    #     counter = 1
    #     for letter in word:
    #         if lenght == counter:
    #             if letter.isalpha():
    #                 letter_fix = letter.upper()
    #                 str += letter_fix
    #                 str += " "
    #                 break
    #             else:
    #                 str += letter
    #                 str += " "
    #                 break
    #         else:
    #             counter += 1
    #             str += letter
    #     fixed_words += str
    # return fixed_words.strip()


def pairwise_multiplication(data: list, result: int) -> list:
    """
    Find element pairs where their product is equal to the required result.

    Find all contiguous sublists of 2 elements in 'data' where the product of their elements is equal to 'result'.
    Return a list of all found sublists, in the same order they appeared in input list.

    Examples:
    pairwise_multiplication([3, 5, 10], 15)  ->  [[3, 5]]
    pairwise_multiplication([5, 3, 5, 2], 15)  ->  [[5, 3], [3, 5]]
    pairwise_multiplication([6, 2, 3, 4], 12)  ->  [[6, 2], [3, 4]]
    pairwise_multiplication([1, 6, 2, 3, 1], 6)  ->  [[1, 6], [2, 3]]

    :param data: list of integers.
    :param result: integer, the result of list's elements multiplication.
    return: list of 2-element sublists with the power of 'result'.
    """
    result_list1 = []
    for i in range(len(data)):  # saab indeksid nii data tuple check jaoks
        if i == len(data) - 1:  # viimase elemendiga ei kontrolli
            continue
        if data[i] * data[i + 1] == result:  # kohal i ja i jargmine element
            # . append([1, 2]) [data[i], data[i+1]
            result_list1.append([data[i], data[i + 1]])
    return result_list1

    # minu oma
    # check_against = 0
    # pairs = []
    # for n in data:
    #     if n * check_against == result:
    #         pair = [check_against, n]
    #         pairs.append(pair)
    #     check_against = n
    # return pairs


def word_lengths(text: str) -> dict:
    """
    Find all the words in the given text and place them in a dictionary where the key is based on the word's length.

    As per grammar rules, words are separated by spaces.
    However, the text may also contain the following punctuation marks: .,?!"() which may be at the beginning or end of the word.
    They are not taken into account when reading the word length.

    The output must be a dictionary whose keys are {x} letter words, where {x} represents the word length.
    The value of each key (length) is a list of words of that length.
    Words must be in lowercase letters and there must be no repeated words.
    The sequence must also be sorted alphabetically in descending order (b comes before a).
    The order of keys is not important.

    word_lengths("I love programming!") => {
        "1 letter words": ["i"],
        "4 letter words": ["love"],
        "11 letter words": ["programming"]
    }
    word_lengths("it is (so) COOL cool") => {
        "2 letter words": ["is", "so", "it"],
        "4 letter words": ["cool"]
    }
    word_lengths("I don't know") => {
        "1 letter words": ["i"],
        "5 letter words": ["don't"]
        "4 letter words": ["know"]
    }

    :param text: given text
    :return: a dictionary of words sorted by their length
    """
    words = text.split()  # list kus sonad on splititud
    cleaned_words = []
    for word in words:
        word = word.lower()
        clean_word = ""
        for letter in word:
            if letter not in '.,?!"()':
                clean_word += letter
        cleaned_words.append(clean_word)
    result = {}
    for word in cleaned_words:
        key = f"{len(word)} letter words"
        if key not in result:
            result[key] = [word]
        else:
            result[key].append(word)
    return result

    # minu oma
    # result = {}
    # words_list = text.split(" ")
    # for word in words_list:
    #     word1 = word.lower()
    #     if not word1.isalpha():
    #         word_fix = ""
    #         for letter in word1:
    #             if letter.isalpha():
    #                 word_fix += letter
    #         lenght_key = f"{len(word_fix)} letter words"
    #         if lenght_key not in result:
    #             result[lenght_key] = [word_fix]
    #         else:
    #             if word_fix not in result[lenght_key]:
    #                 result[lenght_key].append(word_fix)
    #     else:
    #         lenght_key = f"{len(word1)} letter words"
    #         if lenght_key not in result:
    #             result[lenght_key] = [word1]
    #         else:
    #             if word1 not in result[lenght_key]:
    #                 result[lenght_key].append(word1)
    # return result


def filter_recursively(nums: tuple[int, ...], num: int, cond: int) -> list[int]:
    """
    Filter and return a list of integers that satisfy a given condition.

    The solution has to be recursive.

    Args:
        nums: A tuple of integers to filter.
        num: The reference number to filter by.
        cond: The condition to filter by, where:
          - -1: less than `num`
          - 0: equal to `num`
          - 1: greater than `num`

    Returns:
        A list of integers that satisfy the specified condition.

    Raises:
        ValueError: If `cond` is not -1, 0 or 1.

    """
    if nums == ():  # kui tuhi annab tuhja tagasi
        return []
    if cond == -1:
        if nums[0] < num:
            return [nums[0]] + filter_recursively(nums[1:], num, cond)  # vaatad alati kohal 0 aka esimest kuna loikab alati selle maha jargmise check jaoks
    if cond == 1:
        if nums[0] > num:
            return [nums[0]] + filter_recursively(nums[1:], num, cond)
    if cond == 0:
        if nums[0] == num:
            return [nums[0]] + filter_recursively(nums[1:], num, cond)
    return [] + filter_recursively(nums[1:], num, cond)
    # filter_recursively(nums[1:], num, cond)  # loikab iga korraga uhe tuki algusest maha


def generate_uniids(names: tuple[tuple[str, str], ...]) -> list[str]:
    """
    Generate unique uni-ids based on the provided first and last names.

    The function ignores spaces in either first or last names.

    Uni-id follows these rules:

    - It is in lowercase.
    - It consists of two parts: a first part from the first name, and a second part from the last name.
    - The first part starts with the first letter of the first name.
    - The second part starts with the first letter of the last name.
    - It is unique for each person in the provided list of names.

    First, the function attempts to generate a six-letter uni-id, taking the first two letters of the first name,
    and the first four letters of the last name. For example, 'filast'.
    If the generated uni-id is not unique, the function tries variations to ensure uniqueness.
    To do this, the function takes one more character from the first name
    and one less character from the last name (until 5 letters from first, and 1 letter from last name).
    This operation is repeated until the rules are correct, and a suitable uni-id is found.
    If by doing so, no unique combination can be found,
    the function takes one letter from the first name and five characters from the last name.

    If no unique six-letter uni-id is found, the function generates uni-id as
    first name and last name, separated by a full stop, for example, 'first.last'.
    If this uni-id already exists, the function adds a number starting from one
    until it finds an unused one at the end of the generated uni-id, for example, 'first.last1'.

    In the case ("firstname", "lastname"), the following uniids can be created:
    filast
    firlas
    firsla
    firstl
    flastn
    firstname.lastname
    firstname.lastname1
    firstname.lastname2
    etc.

    In the case ("ab", "cd"), the combinations of name parts does not give 6-letter names,
    so the following uniids can be created:
    ab.cd
    ab.cd1
    ab.cd2
    etc.

    Args:
        names: A collection of tuples, each containing a first name and a last name.

    Returns:
        A list of unique uni-ids generated from the input names.

    """
    result = []
    for name in names:
        first, last = name  # jagab ara eraldi first ja last name muutujasse
        first = first.lower()
        last = last.lower()

        uniids = [
            first[:2] + last[:4],
            first[:3] + last[:3],
            first[:4] + last[:2],
            first[:5] + last[:1],
        ]
        for i in range(1, 10):
            uniids.append(f"{first}.{last}.{i}")

        for uniid in uniids:
            if "." not in uniid and len(uniid) != 6:
                continue
            if uniid not in result:
                result.append(uniid)
                break
    return result

    # minu lahendus
    # complete_uniids = []
    # for full_name in names:
    #     first_name, last_name = full_name
    #     uniid = ""
    #     first = first_name.lower()
    #     last = last_name.lower()
    #     letter_count = 0
    #     chars = ""
    #     for letter in first:
    #         if letter_count == 2:
    #             uniid += chars
    #             chars = ""
    #             letter_count = 0
    #         else:
    #             chars += letter
    #             letter_count += 1
    #
    #     for letter in last:
    #         if letter_count == 4:
    #             uniid += chars
    #             chars = ""
    #         else:
    #             chars += letter
    #             letter_count += 1
    #     complete_uniids.append(uniid)
    #
    # return complete_uniids


class Donut:
    """Donut class."""

    def __init__(self, filling: str, icing: str):
        """
        Donut class constructor.

        :param filling: donut filling
        :param icing: donut icing
        """
        self.filling = filling
        self.icing = icing

    # tee ise juurde et saaks kontrollida kas matchivad for pack donuts by icing and filling
    # vaja sest muidu ei saa dictionarisse sorteerida tuupi jargi kuna muidu compareid lic malu addresse
    def __eq__(self, other):
        """Eq et saaks key jaoks kontrollida kas on samad vaartused."""
        return self.filling == other.filling and self.icing == other.icing

    #  kui teed eq pead ka hash tegema sellele
    def __hash__(self):
        """Kuna kasutad eq on vaja hash teha."""
        return hash((self.filling, self.icing))


class DonutFactory:
    """Donut factory class."""

    def __init__(self):
        """Donut factory class constructor."""
        self.donut_list = []

    def add_donuts(self, donuts: list):
        """
        Add list of fresh donuts to already existing ones.

        :param donuts: list of donuts to add
        :return:
        """
        # minu oma
        # for donut in donuts:
        #     self.donut_list.append(Donut(donut.filling, donut.icing))

        self.donut_list.extend(donuts)
        # self.donu_list += donuts

    def get_donuts(self) -> list:
        """
        Return list of all donuts present on the line at the moment.

        :return: list of all donuts
        """
        return self.donut_list

    def pack_donuts_by_filling_and_icing(self) -> dict:
        """
        Return dict with donuts divided by filling and icing.

        Dict key must be represented as tuple of filling and icing and value as list of donuts with
        given filling and icing.
        {(filling, icing): [donut1, donut2]}

        After packing, the production line for donuts should be empty (everything is packed).

        :return: dict
        """
        result = {}
        for donut in self.donut_list:
            key = (donut.filling, donut.icing)
            if key not in result:
                result[key] = []
            result[key].append(donut)
        self.donut_list = []  # parast seda pidi clear olema
        return result

    def sort_donuts_by_icing_and_filling(self) -> list:
        """
        Return list of donuts sorted by icing in alphabetical order and then by filling in alphabetical order.

        :return: sorted list of donuts
        """
        return sorted(self.donut_list, key=lambda donut: (donut.icing, donut.filling))

    def get_most_popular_donut(self) -> dict:
        """
        Return dict with icing and filling of the most popular donut.

        {'icing': most_pop_donut_icing, 'filling': most_pop_donut_filling}
        If there are several icing-filling combinations with the same amount of donuts,
        use the one which icing is alphabetically lower (a comes before b).

        Hint: you could use the result similar to pack_donuts_by_filling_and_icing method,
        but you cannot empty the production line of donuts.
        So, a common custom method can help here, which returns the dict.
        The most popular combination is the one element of the dict which has the most donuts
        (len on dict value is the highest).

        :return: dict with icing and filling of most pop donut
        """
        donut_dict = self.pack_donuts_by_filling_and_icing()
        best_count = 0
        best_pair = None
        for key, value in donut_dict.items():
            if len(value) > best_count:
                best_count = len(value)
                best_pair = (key, value)
            if len(value) == best_count:
                if key < best_pair[0]:  # tahestikus a on vaiksem kui b
                    best_pair = key  # aint ees pool olev alles jatta
        return {"icing" : best_pair[0], "filling" : best_pair[1]}
        # result = min(donut_dict.items(), key=lambda x: (-len(x[1]), x[0][0]))
        # vt mis votme vaartusel on koige pikem list
        pass

    def get_donuts_by_flavour(self, flavour: str) -> list:
        """
        Get list of donuts that have the same icing or filling as given in method parameter.

        :return: list of donuts with the given flavour.
        """
        result = []
        for donut in self.donut_list:
            if donut.icing == flavour or donut.filling == flavour:
                result.append(donut)
        return result


class Item:
    """Item class."""

    def __init__(self, item_id: int, name: str, quantity: int):
        """
        Initialize a new Item.

        :param item_id: ID of the item
        :param name: Name of the item
        :param quantity: Quantity of the item
        """
        self.name = name
        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity


        if item_id < 0:
            self.item_id = 0
        else:
            self.item_id = item_id


    def __repr__(self) -> str:
        """
        Return a string representation of the Item.

        :return: current item as string
        """
        return f"({self.name},{self.item_id}): {self.quantity}"

    def set_quantity(self, quantity: int):
        """
        Set the quantity of the item.

        :param quantity: New quantity of the item
        """
        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity

    def get_id(self) -> int:
        """
        Return the ID of the item.

        :return: ID of the item
        """
        return self.item_id

    def get_name(self) -> str:
        """
        Return the name of the item.

        :return: Name of the item
        """
        return self.name

    def get_quantity(self) -> int:
        """
        Return the quantity of the item.

        :return: Quantity of the item
        """
        return self.quantity


class StorageLocation:
    """Storage location class."""

    def __init__(self, location_id: int, capacity: int):
        """
        Initialize a new StorageLocation for the Items.

        :param location_id: ID of the location
        :param capacity: Maximum capacity of the location
        """
        self.location_id = location_id
        self.capacity = capacity
        self.items = []
        self.used = 0

    def add_item(self, item: Item) -> bool:
        """
        Add an item to the storage location.

        Storage location has to have enough space left for the new items

        :param item: New items to be added
        :return: boolean indicating whether the new items were added
        """
        if isinstance(item, Item):
            if item.quantity < self.capacity:
                self.capacity -= item.quantity
                self.items.append(item.item_id)
                self.used += item.quantity
                return True
        return False

    def remove_item(self, item_id: int, quantity: int) -> bool:
        """
        Remove specified amount of item from the storage location.

        Verify that the location has enough of items left to remove

        :param item_id: ID of the item to be removed
        :param quantity: Amount of items to be removed
        :return: boolean indicating whether the item was removed
        """
        if item_id in self.items:
            self.capacity += quantity
            self.used -= quantity
            return True

    def get_available_space(self) -> int:
        """
        Get the amount of available space in the storage location.

        :return: amount of free space
        """
        return self.capacity

    def get_item_amount(self, item_id: int) -> int:
        """
        Get the amount of item in the storage location.

        :param item_id: ID of the item
        :return: amount of item
        """
        pass

    def get_stored_item_ids(self) -> set:
        """
        Get the IDs of the stored items in the storage location.

        :return: IDs of the stored items
        """
        pass

    def get_id(self) -> int:
        """
        Get the ID of the storage location.

        :return: ID of the storage location
        """
        pass

    def get_item(self, item_id: int) -> Item:
        """
        Get the Item instance present in the storage location.

        :param item_id: ID of the item to be retrieved
        :return: Item or None if the item with the given ID was not found
        """
        pass


class Warehouse:
    """Warehouse class."""

    def __init__(self, name: str, address: str):
        """
        Initialize a warehouse.

        :param name: Name of the warehouse
        :param address: Address of the warehouse
        """
        pass

    def __repr__(self) -> str:
        """
        Return a representation of the warehouse.

        :return: String representation of the warehouse
        """
        pass

    def add_storage_location(self, location: StorageLocation) -> bool:
        """
        Add a storage location to the warehouse.

        Warehouse can't contain multiple locations with same id

        :param location: Location to be added to the warehouse
        :return: boolean indicating whether the location was added
        """
        pass

    def remove_storage_location(self, location_id: int) -> bool:
        """
        Remove a storage location from the warehouse.

        Location has to be in the warehouse to be removed

        :param location_id: ID of the location to be removed
        """
        pass

    def add_item(self, item: Item) -> bool:
        """
        Add an item to the warehouse.

        The item should be added into a storage location in the warehouse where there is enough space to add the item

        :param item: Item to be added
        :return: boolean indicating whether the item was added
        """
        pass

    def remove_item(self, item_id: int, quantity: int) -> bool:
        """
        Remove given amount of item from the warehouse.

        Item can not be removed if the storage locations do not have enough of given item.

        :param item_id: ID of the item to be removed
        :param quantity: Quantity of the item to be removed
        :return: boolean indicating whether the item was removed
        """
        pass

    def get_inventory(self) -> dict:
        """
        Return dictionary where keys are item IDs and values are their amounts.

        :return: dictionary
        """
        pass

    def search_item(self, item_id: int) -> int:
        """
        Get the amount of item with the given ID in the warehouse.

        :param item_id: ID of the item
        :return: amount present in the warehouse
        """
        pass

    def get_largest_quantity(self) -> int:
        """
        Get the item amount for item with the highest amount in the warehouse.

        :return: Item amount present in the warehouse
        """
        pass

    def get_available_space(self) -> int:
        """
        Get the amount of free space in the warehouse.

        Free space in the warehouse is sum of free space of each storage location

        :return: amount of free space in the warehouse
        """
        pass

    def get_storage_locations(self) -> set:
        """
        Get a set of storage locations present in the warehouse.

        :return: set of storage locations
        """
        pass


class Shipment:
    """Shipment class."""

    def __init__(self, source_location: Warehouse, destination_location: Warehouse):
        """
        Initialize new shipment.

        :param source_location: Source warehouse
        :param destination_location: Destination warehouse
        """
        pass

    def add_item(self, item_id: int, quantity: int) -> bool:
        """
        Add item with quantity to the shipment.

        Quantity must be greater than zero to add the item to the shipment

        :param item_id: ID of the item
        :param quantity: quantity to add
        :return: boolean indicating whether the item was added to the shipment
        """
        pass

    def remove_item(self, item_id: int, quantity: int) -> None:
        """
        Remove item from the shipment.

        Item quantity must be greater than zero to remove.
        The shipment has to contain enough quantity of the item  to be removed

        :param item_id: ID of the item
        :param quantity: quantity to remove
        """
        pass

    def get_items(self) -> dict:
        """
        Get a dictionary containing all the items in the shipment.

        Keys are item ids and values are their quantities

        :return: dictionary containing all the items in the shipment
        """
        pass

    def process(self) -> bool:
        """
        Process the shipment.

        Verify that the source warehouse has enough items to be removed and
        that the destination warehouse has enough space for the items.
        If either is not true the shipment will not be processed

        :return: boolean indicating whether the shipment was successfully processed
        """
        pass


if __name__ == "__main__":
    print("count_digits:")
    print(count_digits("123"))  # -> 3
    print(count_digits("a"))  # -> 0
    print()

    print("capitalize_first_last_letters:")
    print(capitalize_first_last_letters("python exercises practice solution"))  # PythoN ExerciseS PracticE SolutioN
    print(capitalize_first_last_letters("IAIB 2023 program"))  # IaiB 2023 PrograM
    print()

    print("pairwise_multiplication")
    print(pairwise_multiplication([3, 5, 10], 15))  # ->  [[3, 5]]
    print(pairwise_multiplication([5, 3, 5, 2], 15))  # ->  [[5, 3], [3, 5]]
    print(pairwise_multiplication([6, 2, 3, 4], 12))  # ->  [[6, 2], [3, 4]]
    print(pairwise_multiplication([1, 6, 2, 3, 1], 6))  # [[1, 6], [2, 3]]
    print()

    print("word_lengths:")
    print(word_lengths("I love programming!"))
    # -> {"1 letter words": ["i"],  "4 letter words": ["love"], "11 letter words": ["programming"]}
    print(word_lengths("it is (so) COOL cool"))
    # ->  {"2 letter words": ["is", "so", "it"], "4 letter words": ["cool"]}
    print()

    print("filter_recursively:")
    nums = (1, 2, 3, 3, 4, 5)
    print(filter_recursively(nums, 3, 0))  # [3, 3]
    print(filter_recursively(nums, 3, 1))  # [4, 5]
    print(filter_recursively(nums, 3, -1))  # [1, 2]
    print()

    print("generate_uniids:")
    input_names = (("Ago", "Luberg"), ("Anton", "Menov"))
    actual = generate_uniids(input_names)
    print(actual)  # => ["aglube", "anmeno"]
    print()

    print("DonutFactory")
    donut_factory = DonutFactory()
    donut1 = Donut('chocolate', 'sugar')
    donut2 = Donut('caramel', 'chocolate')
    donut3 = Donut('cherry', 'marshmallow')
    donut4 = Donut('chocolate', 'sugar')
    donut5 = Donut('vanilla', 'cream')
    donut6 = Donut('vanilla', 'cream')
    donut7 = Donut('cherry', 'marshmallow')
    donut8 = Donut('chocolate', 'sugar')

    donuts = [donut1, donut2, donut3, donut4, donut5, donut6, donut7, donut8]

    donut_factory.add_donuts(donuts)

    assert donut_factory.get_donuts_by_flavour("marshmallow") == [donut3, donut7]
    assert donut_factory.get_most_popular_donut() == {'icing': 'sugar', 'filling': 'chocolate'}
    assert donut_factory.sort_donuts_by_icing_and_filling() == [donut2, donut5, donut6, donut3, donut7, donut1,
                                                         donut4, donut8]
    assert donut_factory.pack_donuts_by_filling_and_icing() == {
        ('chocolate', 'sugar'): [donut1, donut4, donut8],
        ('caramel', 'chocolate'): [donut2],
        ('cherry', 'marshmallow'): [donut3, donut7],
        ('vanilla', 'cream'): [donut5, donut6]
    }
    print()
    print("Warehouses:")
    # Warehouses
    hats = Item(1, "Hat", 10)
    print(hats)  # (Hat,1): 10
    coats = Item(2, "Coat", 15)
    print(coats)  # (Coat,2): 15

    location1 = StorageLocation(1, 20)

    print(location1.add_item(hats))  # True
    print(location1.add_item(coats))  # False -> not enough space

    location2 = StorageLocation(2, 100)
    warehouse1 = Warehouse("Main Warehouse", "Ontario, Canada")
    print(warehouse1)  # Main Warehouse, Ontario, Canada

    warehouse1.add_storage_location(location1)
    warehouse1.add_storage_location(location2)

    print(warehouse1.add_item(coats))  # True
    print(location2.get_stored_item_ids())  # {2}

    shoes = Item(3, "Shoes", 50)
    socks = Item(4, "Socks", 50)
    location3 = StorageLocation(1, 75)
    location4 = StorageLocation(2, 75)
    warehouse2 = Warehouse("Secondary Warehouse", "Minnesota, USA")
    warehouse2.add_storage_location(location3)
    warehouse2.add_storage_location(location4)
    warehouse2.add_item(shoes)
    warehouse2.add_item(socks)

    print(warehouse2.get_inventory())  # {3: 50, 4: 50}

    shipment = Shipment(warehouse2, warehouse1)
    shipment.add_item(3, 50)
    shipment.add_item(4, 50)
    print(shipment.process())  # False -> not enough space in destination

    shipment.remove_item(4, 25)
    print(shipment.get_items())  # {3: 50, 4: 25}
    print(shipment.process())  # True

    print(warehouse1.get_inventory())  # {2: 15, 3: 50, 4: 25}
    print(warehouse1.get_largest_quantity())  # 50
    print()
