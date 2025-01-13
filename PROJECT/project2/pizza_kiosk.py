"""Project 2."""
import re


def is_correct_name(ingredient: str) -> bool:
    """
    Funktsioon kontrollib, kas koostisosa nimetus on õigesti kirjutatud, ning tagastab vastavalt True või False.

    Nimetus ei tohi sisaldada erisümboleid, numbreid ega suurtähti.
    Samuti ei tohi nimetus olla tühi sõne.
    :param ingredient:
    :return:
    """
    return ingredient.isalpha() and ingredient.islower() and len(ingredient) > 0
# on aint tahed aint vaiketahed ja pole tuhi peavad koik true olemav


def fix_names(ingredients: list) -> list:
    """
    Funktsioon peab iga järjendis oleva sõne ära parandama.

    Tagastada tuleb järjend õigesti kirjutatud sõnedest.
    Sõned peavad olema kirjutatud läbivalt väikese tähega (suured tähed peab väikesteks tegema) ning ei tohi sisaldada erisümboleid ega numbreid.
    Samuti ei või sõne olla tühi.
    :param ingredients:
    :return:
    """
    fixed_ingredients = []  # parandatud nimede list

    for ingredient in ingredients:
        # kui on juba korrektne pane kohe listi
        if is_correct_name(ingredient):
            fixed_ingredients.append(ingredient)
        else:
            ingredient_lower = ingredient.lower()  # paneb lowercase
            ingredient_chars = []  # kogub aint tahed listi
            for char in ingredient_lower:
                if char.isalpha():
                    ingredient_chars.append(char)
            # paneb koik leitud tahed uhte sonasse
            clean_ingredient = ''.join(ingredient_chars)
            # kui on clean ingridient olemas aka pole tuhi ss paned fixed listi
            if clean_ingredient:
                fixed_ingredients.append(clean_ingredient)

    return fixed_ingredients


def pizza_at_index(pizzas: list, pizza: str) -> str:
    """
    Funktsioon peab leidma järjendist pitsa, mille indeksiks on antud pitsa esinemiste arv selles järjendis, ning tagastama selle.

    Kui antud indeksiga elementi ei eksisteeri, tagasta tühi sõne.
    Näide: pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa") -> "kanapitsa" (järjendis on 1 juustupitsa, seega indeksiks on 1)
    :param pizzas:
    :param pizza:
    :return:
    """
    indeks = pizzas.count(pizza)  # count loeb mitu sulgudes oleva vaartusega liiget on

    # index ei saa olla negatiivne ning suurem kui listi pikkus
    if 0 <= indeks < len(pizzas):
        return pizzas[indeks]
    # any other case annab tagasi tuhja sone
    else:
        return ""


def format_orders(nr_order: list) -> dict:
    """
    Ette on antud järjend sõnedest. Üks sõne on kujul “tellimuse_number&tellimus”, näiteks “5&kanapitsa”.

    Funktsioon peab koostama sõnastiku kõikidest tellimustest, kus võtmeks on tellimuse number täisarvuna ning väärtuseks on tellimus väikeste tähtedega.
    Sõnastik peab jääma samasse järjekorda kui etteantud järjend.
    Näide: format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]) -> {5: "kanapitsa", 1: "pepperoni", 20: "mexican"}
    :param nr_order:
    :return:
    """
    orders_dict = {}

    for order in nr_order:
        order_nr, order_item = order.split('&')  # jagab ara nriks ja sisuks selle margi kohapeal

        order_nr = int(order_nr)  # teeb strist numbriks
        order_item = order_item.lower()

        orders_dict[order_nr] = order_item  # paneb dictionarisse order_nr on key item value
        # kui key pole veel dictionaris teeb uue entry selle key jaoks

    return orders_dict
# NB see tootab oigesti ainult juhtudel kui keyd ei kordu muidu updateib ara uue ja kustutab vana


def calculate_income(prices: str) -> float:
    """
    Aita kioskil päevatulu välja arvutada.

    Ette on antud sõne, mis sisaldab päeva jooksul müüdud tellimuste hindasid, mis on üksteisest eraldatud suvalise koguse erisümbolitega.
    Hinnad koosnevad alati neljast numbrist, kus punkt eraldab täis- ja murdarvu osa.
    Kui punkt on kusagil mujal erisümbolite keskel, siis see ei ole seotud hinnaga.
    Sõnes ei ole numbreid, mis pole seotud hinnaga.
    Tagastada tuleb hindade summa ujukomaarvuna.
    Lahendus peab olema rekursiivne.
    Näide: calculate_income("15.03*05.99|)=01.20&.$50.37") -> 72.59
    :param prices:
    :return:
    """
    # peab otsima koik numbrid kujul xx.xx ja need kokku liitma
    if not prices:
        return 0.0  # kui tuhi hulk annab 0

    nr_pattern = r"(\d{2}\.\d{2})"  # \d otsib digiteid sel juhul kaks jarjest \. otsib literally punkti
    match = re.match(nr_pattern, prices)  # leiab matchiva rn

    if match:
        price = float(match.group())  # teeb leitud nr ujukoma arvuks
        return price + calculate_income(prices[match.end():])  # [match.end():] loikab leitud matchi jupi price stringist valja
    # liidab juba leitud hinnale jargmise leitud hinnale kuni lopp

    else:
        return calculate_income(prices[1:])  # prices[1:] loikab price string essa tahe ara, ning laheb tagasi kontrollima ilma selleta (loikab ara koik mis pole num pohimotteliselt)
    # lahendab rekursiivselt kuni lopuni


def switch_keys_and_values(pizza_orders: dict) -> dict:
    """
    Ülesandeks on vahetada ära sõnastiku võtmed ja väärtused.

    Ette antud sõnastikus on võtmeks pitsa nimi ning väärtuseks järjend kõikidest tellimuste numbritest, mis sisaldavad seda pitsat.
    Sõnastik tuleb teha selliseks, et võtmeks oleks tellimuse number ning väärtuseks järjend pitsadest, mis on selles tellimuses.
    Näide: {"kanapitsa": [1, 5, 3, 4], "juustupitsa": [1, 2], "pepperoni": [1, 5, 3]}
    -> {1: ["kanapitsa", "juustupitsa", "pepperoni"], 5: ["kanapitsa", "pepperoni"], 3: {"kanapitsa", "pepperoni"], 4: ["kanapitsa"], 2: ["juustupitsa"]}
    :param pizza_orders:
    :return:
    """
    switched_dict = {}  # uus dict switchitud versioon
    # pizza, orders jagab pizza_orders kahte muutujasse pizza pitsade nimed, orders nr list
    for pizza, orders in pizza_orders.items():  # .items() annab sel juhul tagasi paaridena nii: "kanapitsa": [1, 5, 3, 4] -> ("kanapitsa", [1, 5, 3, 4])
        # votab pizzade kaupa
        for order in orders:  # vaatab koik orderite nr labi
            # listis olevad nr ukshaaval
            if order not in switched_dict:  # kui seda nr veel dictionaris pole
                switched_dict[order] = []  # teeb numbri jaoks tuhja listi kuhu pizza lisada
            switched_dict[order].append(pizza)  # lisab pizza praegu vaadatava order nr juurde, kuna vaadatakse algul pizzade haaval ss kuni list lopuni on sama pizza
        # nr listi loppedes laheb jargmise pizzaga edasi ja lisab need jne jne

    return switched_dict  # selles dict on keyks nr pizza asemel


def count_ingredients(menu: dict, order: list) -> dict | None:
    """
    Funktsioon saab sisendiks sõnastiku, milles võtmeks on pitsa nimetus ja väärtuseks koostisosade järjend, ning järjendi tellimuste nimetustest.

    Funktsioon loeb kokku, kui palju iga koostisosa tellimuse jaoks vaja läheb ja tagastab tulemuse sõnastikuna.
    Kui tellimuses on mõni pitsa, mida sõnastikus pole, tagasta tühi sõnastik.
    Näide: count_ingredients({"margarita": ["juust", "tomat", "kaste"], "pepperoni": ["juust", "kaste", "pepperoni"]}, ["margarita", "margarita", "pepperoni"])
    -> {"juust": 3, "kaste": 3, "tomat": 2, "pepperoni": 1}
    :param menu:
    :param order:
    :return:
    """
    ingredient_dict = {}  # tuhi dict kuhu saab koostisosad ja nende kogused koguda kujul 'juust': 3

    for pizza in order:
        if pizza not in menu:
            return {}  # kui tellimuses on pizza mida pole menuus annab tuhja dict

        ingredients = menu[pizza]  # votab koostisosade listi menuust vastavalt praegu vaadatavale pizzale

        for ingredient in ingredients:  # vaatab koik koostisosad ukshaaval listis labi
            if ingredient in ingredient_dict:
                ingredient_dict[ingredient] += 1  # kui seda koostisosa oli juba varem dictis ss liidab ingridientile kuuluvale valuele 1
            else:
                ingredient_dict[ingredient] = 1  # kui polnud lisab ingridienti dicti ja annab value aka koguse 1

    return ingredient_dict


def match_pizzas_with_prices(pizzas: list, prices: list) -> list:
    """
    Funktsioon eemaldab pitsade järjendist valesti kirjutatud või korduvad pitsade nimetused.

    Valesti kirjutatud nimetused sisaldavad suurtähti, numbreid või erisümboleid.
    Kui peale seda on pitsade ja hindade järjendid sama pikad, tagastada järjend ennikutest, kus esimene element on pitsa nimetus, teine hind.
    Kui järjendid on erineva pikkusega, tagasta tühi järjend.
    NB! Pitsade järjekord on oluline
    Näide: match_pizzas_with_prices(["pepperoni", "margarita", "ch7eese", "cheese", "margarita"], [3.99, 4.99, 3.99])
    -> [("pepperoni", 3.99), ("margarita", 4.99), ("cheese", 3.99)]
    :param pizzas:
    :param prices:
    :return:
    """
    valid_pizzas = []
    for pizza in pizzas:
        if pizza.isalpha() and pizza.islower() and pizza not in valid_pizzas:  # on aint tahed, on aint vaiketahed, ja pole varem listis juba et ei tekiks korduvaid elemente
            valid_pizzas.append(pizza)

    if len(valid_pizzas) != len(prices):  # kui korrektne pitsade list pole hinna listiga sama pikk annab tuhja list
        return []

    return list(zip(valid_pizzas, prices))  # paneb pizza paari priceiga lic jarjest nt selle naite puhul (pepperoni, 3.49) tupllesse


if __name__ == '__main__':
    print(is_correct_name("sugar"))  # True
    print(is_correct_name("Sugar"))  # False
    print(is_correct_name("sugar1"))  # False
    print(is_correct_name("sug@r"))  # False
    print(is_correct_name(""))  # False

    print(fix_names(["Sugar", "Flour?", "Salt2", "", "Eggs&", "tomato"]))
    # Output: ["sugar", "flour", "salt", "eggs", "tomato"]

    print(pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa"))
    # Output: "kanapitsa" (kuna "juustupitsa" ilmuub korra, so index on 1 ehk teine listis kuna index algab 0-ist)
    print(pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa", "juustupitsa"], "juustupitsa"))
    # Output: "juustupitsa"

    print(format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]))
    # Output: {5: "kanapitsa", 1: "pepperoni", 20: "mexican"}

    print(calculate_income("15.03*05.99|)=01.20&.$50.37"))
    # Output: 72.59

    pizza_orders = {
        "kanapitsa": [1, 5, 3, 4],
        "juustupitsa": [1, 2],
        "pepperoni": [1, 5, 3]
    }
    print(switch_keys_and_values(pizza_orders))
    # output {
    #    1: ["kanapitsa", "juustupitsa", "pepperoni"],
    #    5: ["kanapitsa", "pepperoni"],
    #    3: ["kanapitsa", "pepperoni"],
    #    4: ["kanapitsa"],
    #    2: ["juustupitsa"]
    # }

    menu = {
        "margarita": ["juust", "tomat", "kaste"],
        "pepperoni": ["juust", "kaste", "pepperoni"]
    }
    order = ["margarita", "margarita", "pepperoni"]
    print(count_ingredients(menu, order))
    # output: {'juust': 3, 'tomat': 2, 'kaste': 3, 'pepperoni': 1}

    print(match_pizzas_with_prices(pizzas=["pepperoni", "margarita", "ch7eese", "cheese", "margarita"], prices=[3.99, 4.99, 3.99]))
    # output: [("pepperoni", 3.99), ("margarita", 4.99), ("cheese", 3.99)]
