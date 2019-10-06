class Measures():
    allowed_measure_types = [
        ("weight", "weight (e.g. grams, libs"),
        ("capacity", "capacity (e.g. liters, gallons)"),
        ("length", "length (e.g. centimeters, inches)"),
        ("absolute", "pure number (e.g. 3 leaves)"),
        ("energy", "energy (kilojoule, calories)"),
        ("extra", "extra (e.g. a pinch of, to taste)")
    ]

    reference_units = {
        "weight": "g",
        "capacity": "l",
        "length": "m",
        "energy": "kcal"
    }

    units = {
        # 1g equals
        "weight": {
            "g": {
                "conversion": 1,
                "long_name": "gram"
            },
            "kg": {
                "conversion": 0.001,
                "long_name": "kilogram"
            },
            "mg": {
                "conversion": 1000,
                "long_name": "milligram"
            },
            "lb": {
                "conversion": 0.00220462,
                "long_name": "pound"
            },
            "oz": {
                "conversion": 0.0352739200000000003,
                "long_name": "ounce"
            },
        },

        # 1l equals
        "capacity": {
            "l": {
                "conversion": 1,
                "long_name": "liter"
            },
            "ml": {
                "conversion": 1000,
                "long_name": "milliliter"
            },
            "dl": {
                "conversion": 10,
                "long_name": "deciliter"
            },
            "us_legal_cup": {
                "conversion": 4.1666690666667,
                "long_name": "US legal cup"
            },
            "us_l_gal": {
                "conversion": 0.26417199999924750875,
                "long_name": "US liquid gallon"
            },
            "us_l_pint": {
                "conversion": 2.11337599999398,
                "long_name": "US liquid pint"
            },
            "us_fl_oz": {
                "conversion": 33.81401599990368112,
                "long_name": "US fluid ounce"
            },
            "imp_cup": {
                "conversion": 3.51951,
                "long_name": "imperial cup"
            },
            "imp_gal": {
                "conversion": 0.219969,
                "long_name": "imperial gallon"
            },
            "imp_pint": {
                "conversion": 0.219969,
                "long_name": "imperial pint"
            },
            "imp_fl_oz": {
                "conversion": 35.1951,
                "long_name": "imperial fluid ounce"
            },
        },
        # 1m equals
        "length": {
            "m": {
                "conversion": 1,
                "long_name": "meter"
            },
            "cm": {
                "conversion": 100,
                "long_name": "centimeter"
            },
            "mm": {
                "conversion": 1000,
                "long_name": "millimeter"
            },
            "ft": {
                "conversion": 3.28084,
                "long_name": "foot"
            },
            "in": {
                "conversion": 39.3701,
                "long_name": "inch"
            },
        },

        # 1 kcal equals
        "energy": {
            "cal": {
                "conversion": 1000,
                "long_name": "kilogram"
            },
            "kcal": {
                "conversion": 1,
                "long_name": "kilocalorie"
            },
            "kj": {
                "conversion": 4.184,
                "long_name": "kilojoule"
            },
        }
    }
    units["weight"]["Kg"] = units["weight"]["kg"]
    units["length"]["″"] = units["length"]["in"]
    units["energy"]["kJ"] = units["energy"]["kj"]
    units["energy"]["KJ"] = units["energy"]["kj"]
    units["energy"]["Kj"] = units["energy"]["kj"]
    units["energy"]["KCal"] = units["energy"]["kcal"]

    def __init__(self, measure, unit, unit_type=None):
        if unit_type is None:
            for unit_type_ in Measures.units.keys():
                if unit in Measures.units[unit_type_].keys():
                    unit_type = unit_type_
            if unit_type is None:
                raise KeyError(f"Unit {unit} not found."
                               f" Available: {[unit_ for unit_type_ in Measures.units.keys() for unit_ in Measures.units[unit_type_].keys()]}")

        self.__assert_unit_exists__(unit, unit_type)
        self.__unit_type__ = unit_type
        self.__unit__ = unit
        self.set_measure(measure)

    @staticmethod
    def __assert_unit_exists__(unit, unit_type):
        if unit_type not in Measures.units.keys():
            raise KeyError(f"Measure type {unit_type} not found. Available: {Measures.units.keys()}")
        elif unit not in Measures.units[unit_type].keys():
            raise KeyError(
                f"Measure unit {unit} not found for type {unit_type}. Available: {Measures.units[unit_type].keys()}")

    def convert_to(self, dest_unit):
        self.__assert_unit_exists__(dest_unit, self.__unit_type__)
        return self.__inner_val__ * Measures.units[self.__unit_type__][dest_unit]["conversion"]

    def val(self):
        return self.__inner_val__ * Measures.units[self.__unit_type__][self.__unit__]["conversion"]

    def unit(self):
        return self.__unit__

    def long_unit_name(self):
        return Measures.units[self.__unit_type__][self.__unit__]["long_unit_name"]

    def unit_type(self):
        return self.__unit_type__

    def set_measure(self, measure):
        self.__inner_val__ = measure / Measures.units[self.__unit_type__][self.__unit__]["conversion"]

    def set_unit(self, dest_unit):
        self.__assert_unit_exists__(dest_unit, self.__unit_type__)
        self.__unit__ = dest_unit

    def __str__(self):
        return f"{self.val()}{self.unit()}"
