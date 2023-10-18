def celsius_fahrenheit(celsius):
    formula = (celsius * 9/5) + 32
    return formula


def celsius_kelvin(celsius):
    formula = celsius + 273.15
    return formula


if __name__ == '__main__':
    celsius_fahrenheit()
    celsius_kelvin()
    