"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """
    total_uppercase = 0
    total_lowercase = 0
    total_number = 0

    for character in letter:  #  kontrollib iga numbri/tahe labi
        if character.isupper():
            #  kontrollib kas on uppercase, kui on lisab 1 to total_uppercase kogusele
            total_uppercase += 1
        elif character.islower():
            #  kui on lowercase lisab 1 to total_lowercase kogusele
            total_lowercase += 1
        elif character.isdigit():
            #  kui on nr lisab selle numbri to total_number
            total_number += int(character)  #  makes sure see liidab numbrina

    #  reeglid mida kontrollitakse
    rule1 = total_uppercase > total_lowercase
    rule2 = total_number <= total_uppercase
    rule3 = total_number >= total_lowercase

    return rule1 and rule2 and rule3



if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True
