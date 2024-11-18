"""Cars."""
from collections import Counter
import json


class Car:
    """Car class."""

    def __init__(self, make: str, model: str, fuel_consumption: float, features: list[str]):
        """
        Initialize a Car object.

        :param make: The make of the car.
        :param model: The model of the car.
        :param fuel_consumption: The fuel consumption of the car in liters per 100 kilometers.
        :param features: The features of the car.
        """
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.features = features

    def __eq__(self, other):
        """Check if two cars are equal. Don't change this method."""
        return type(other) is self.__class__ and \
            self.make == other.make and \
            self.model == other.model and \
            self.fuel_consumption == other.fuel_consumption and \
            self.features == other.features

    def __hash__(self) -> int:
        """Allow a Car object to be used as a key in a dictionary. Don't change this method."""
        return hash((self.make, self.model, self.fuel_consumption, tuple(self.features)))

    def __repr__(self) -> str:
        """Return a string representation of the Car object. It is not necessary to change this method."""
        return f'{self.make} {self.model}'


def sort_cars_by_make(cars: list[Car]) -> list[Car]:
    """
    Sort the given list of cars by make alphabetically.

    If multiple cars have the same make, sort them by model alphabetically.
    If those cars also have the same model, then the order of those cars doesn't matter.

    :param cars: The list of cars to sort.
    :return: The sorted list of cars.
    """
    return sorted(cars, key=lambda car: (car.make.lower(), car.model.lower()))  # sorted tagastab uue sorteeritud loendi,
    # key lambda anonuumne aka ilma nimeta vaike funktsioon mis sel juhul teeb molemad loweriks et ei oleks case sensitive,
    # key naitab mille jargi toimub sorteerimine, antud juhul auto mark ja mudel


def find_cars_by_make_and_model(cars: list[Car], make: str, model: str) -> list[Car]:
    """
    Find all cars with the given make and model. The order of the cars in the returned list does not matter.

    :param cars: The list of cars to search through.
    :param make: The given make.
    :param model: The given model.
    :return: The list of cars with the given make and model.
    """
    result = []
    for car in cars:
        if car.make.lower() == make.lower() and car.model.lower() == model.lower():  # case insensitive
            result.append(car)
    return result


def find_cars_by_feature(cars: list[Car], feature: str) -> list[Car]:
    """
    Find all cars that have the given feature.

    Sort the resulting list of cars by make alphabetically. If multiple cars have the same make,
    sort them by model alphabetically. If those cars also have the same model, then the order
    of those cars doesn't matter.

    :param cars: The list of cars to search through.
    :param feature: The given feature.
    :return: The list of cars that have the specified feature.
    """
    result = []
    for car in cars:
        car_features = car.features  # get the feature list for the car thats being looked at
        lower_features = map(str.lower, car_features)  # map() allplies str.lower to every string int the car feature list :)

        if feature.lower() in lower_features:
            result.append(car)  # if the features match (NOT CASE SENSITIVE) add to the result list

    return sort_cars_by_make(result)


def fuel_needed(car: Car, distance: int) -> float:
    """
    Calculate the amount of fuel needed for a given distance based on the car's fuel consumption.

    :param car: The car object representing the vehicle.
    :param distance: The distance in kilometers for which the fuel amount is calculated.
    :return: The amount of fuel needed in liters (don't use rounding).
    """
    return (car.fuel_consumption / 100) * distance
# / 100 kuna fuel consumption oli antud 100 km jaoks so see arvutab 1km oma


def calculate_average_fuel_consumption(cars: list[Car]) -> float:
    """
    Calculate the average fuel consumption of the given cars.

    The average fuel consumption is the sum of the fuel consumption of all the cars divided by the number of cars.

    :param cars: The list of cars to calculate the average fuel consumption for.
    :return: The average fuel consumption of the given cars.
    """
    total_fuel = 0
    if not cars:
        return 0.0  # if the car list is empty

    for car in cars:
        total_fuel += car.fuel_consumption  # add every cars fuel consumtion together

    average_fuel = total_fuel / len(cars)  # all the cars fuel cost divided by how many cars were on the list#
    return average_fuel


def most_popular_feature(cars: list[Car]) -> str:
    """
    Find the most popular feature among the given cars.

    The most popular feature is the feature that occurs the most times among all the cars.
    If multiple features occur the same number of times, return any of them.

    :param cars: The list of cars to search through.
    :return: The most popular feature among the given cars.
    """
    all_features_list = []

    for car in cars:  # for every car
        for feature in car.features:  # check every feature for that car
            all_features_list.append(feature)  # add it to the list

    if not all_features_list:  # if no features got added to the list
        return None  # just incase

    feature_counts = Counter(all_features_list)  # count how many times every feature occurs
    most_frequent_feature = feature_counts.most_common(1)  # counts.most_common(1) returnib listi koige rohkem esinenud featureitest tuplena kujul (feature, count) kui on more than 1 pannakse listi
    if most_frequent_feature:
        return most_frequent_feature[0][0]  # returns the first one from the list (starts counting form 0) aka the most common
    else:
        return None  # if there is no most common feature


def write_cars_to_file(cars: list[Car], file_name: str):
    """
    Write the given list of cars to the given file in JSON format, using indent=2.

    The cars should be written as a list of dictionaries, where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.
    lang="python" class="code highlight js-syntax-highlight language-python dark" data-canonical-lang="python" data-sourcepos="154:1-322:3" id="code-74">

    :param cars: The list of cars to write to the file.
    :param file_name: The name of the file to write the cars to.
    """
    # convert Car objects to dictionery
    cars_dict = [{
        'make': car.make,
        'model': car.model,
        'fuel_consumption': car.fuel_consumption,
        'features': car.features
    } for car in cars]  # for every car so every car will have a dictionary formated like that and they are all collected into a list

    with open(file_name, 'w') as f:
        json.dump(cars_dict, f, indent=2)
    # opens in write mode (w), with so closed after use,
    # json.dump writes the list of dictionaries in the file indent makes the stair part fore readibility likes
    # [
    #   {
    #      make


def read_cars_from_file(file_name: str) -> list[Car]:
    """
    Read a list of cars from the given file in JSON format.

    The file should contain a list of dictionaries where each dictionary represents a car.
    The keys of the dictionaries should be the attributes of the car and the values should be
    the values of the attributes. The order of the cars in the list should stay the same.

    :param file_name: The name of the file to read the cars from.
    :return: The list of cars read from the file.
    """
    with open(file_name, 'r') as f:  # opens in read more (r)
        cars_dict = json.load(f)  # reads the json data and covnert it to list of dict

    cars = []
    for car in cars_dict:  # for every car get the attributes
        make = car['make']
        model = car['model']
        fuel_consumption = car['fuel_consumption']
        features = car['features']

        car_object = Car(make, model, fuel_consumption, features)  # make a car object w alll the attributes
        cars.append(car_object)
    return cars


if __name__ == '__main__':
    list_of_cars = [Car('BMW', 'X5', 12.3, ['leather', 'heated seats', 'GPS']),
                    Car('BMW', 'X6', 7.2, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A6', 9.93, ['leather', 'heated seats', 'panorama', 'GPS']),
                    Car('Audi', 'A7', 15.21, ['leather', 'heated seats', 'panorama', 'sport package']),
                    Car('Mercedes', 'S500', 10.6, ['leather', 'panorama', 'sport package',
                                                   'premium sound system'])]

    print(list_of_cars)  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]
    print(sort_cars_by_make(list_of_cars))  # [Audi A6, Audi A7, BMW X5, BMW X6, Mercedes S500]
    print()

    print(find_cars_by_make_and_model(list_of_cars, 'BMW', 'X6'))  # [BMW X6]
    print(find_cars_by_feature(list_of_cars, 'panorama'))  # [Audi A6, Audi A7, BMW X6, Mercedes S500]
    print()

    print(fuel_needed(list_of_cars[0], 150))  # 18.45; may be different due to floating point arithmetic errors
    print(calculate_average_fuel_consumption(list_of_cars))  # 11.048
    print()

    print(most_popular_feature(list_of_cars))  # leather
    write_cars_to_file(list_of_cars, 'cars.json')
    print(read_cars_from_file('cars.json'))  # [BMW X5, BMW X6, Audi A6, Audi A7, Mercedes S500]
