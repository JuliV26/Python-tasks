class RomanNumbers:
    def __init__(self, number):
        if not (1 <= number <= 3999):
            raise ValueError("Number out of range (1-3999)")
        self.number = number

    def to_roman(self):
        roman_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }
        num = self.number
        result = ""

        for value, symbol in roman_map.items():
            while num >= value:
                result += symbol
                num -= value
        return result

    def from_roman(self, roman_str):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        prev = 0

        for char in reversed(roman_str):
            value = roman[char]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        return total
    
r = RomanNumbers(14)
print(r.to_roman())
print(r.from_roman("XIV"))

