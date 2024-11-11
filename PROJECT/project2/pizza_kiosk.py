"""Project 2."""


def is_correct_name(ingredient: str) -> bool:
    """
    Funktsioon kontrollib, kas koostisosa nimetus on õigesti kirjutatud, ning tagastab vastavalt True või False.

    Nimetus ei tohi sisaldada erisümboleid, numbreid ega suurtähti.
    Samuti ei tohi nimetus olla tühi sõne.
    :param ingredient:
    :return:
    """
    return ingredient.isalpha() and ingredient.islower() and len(ingredient) > 0
# on aint tahed aint vaiketahed ja pole tuhi peavad koik true olema


def fix_names(ingredients: list) -> list:
    """
    Funktsioon peab iga järjendis oleva sõne ära parandama.

    Tagastada tuleb järjend õigesti kirjutatud sõnedest.
    Sõned peavad olema kirjutatud läbivalt väikese tähega (suured tähed peab väikesteks tegema) ning ei tohi sisaldada erisümboleid ega numbreid.
    Samuti ei või sõne olla tühi.
    :param ingredients:
    :return:
    """
    pass


def pizza_at_index(pizzas: list, pizza: str) -> str:
    """
    Funktsioon peab leidma järjendist pitsa, mille indeksiks on antud pitsa esinemiste arv selles järjendis, ning tagastama selle.

    Kui antud indeksiga elementi ei eksisteeri, tagasta tühi sõne.
    Näide: pizza_at_index(["pepperoni", "kanapitsa", "juustupitsa"], "juustupitsa") -> "kanapitsa" (järjendis on 1 juustupitsa, seega indeksiks on 1)
    :param pizzas:
    :param pizza:
    :return:
    """
    pass


def format_orders(nr_order: list) -> dict:
    """
    Ette on antud järjend sõnedest. Üks sõne on kujul “tellimuse_number&tellimus”, näiteks “5&kanapitsa”.

    Funktsioon peab koostama sõnastiku kõikidest tellimustest, kus võtmeks on tellimuse number täisarvuna ning väärtuseks on tellimus väikeste tähtedega.
    Sõnastik peab jääma samasse järjekorda kui etteantud järjend.
    Näide: format_orders(["5&kanapitsa", "1&pepperoni", "20&MeXican"]) -> {5: "kanapitsa", 1: "pepperoni", 20: "mexican"}
    :param nr_order:
    :return:
    """
    pass


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
    pass


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
    pass


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
    pass


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
    pass

if __name__ == '__main__':
    print(is_correct_name("sugar"))  # True
    print(is_correct_name("Sugar"))  # False
    print(is_correct_name("sugar1"))  # False
    print(is_correct_name("sug@r"))  # False
    print(is_correct_name(""))  # False