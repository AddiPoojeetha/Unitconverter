def convert_unit(value, unit_from, unit_to):
    if unit_from == "mm" and unit_to == "cm":
        return value / 10
    elif unit_from == "cm" and unit_to == "mm":
        return value * 10
    elif unit_from == "cm" and unit_to == "m":
        return value / 100
    elif unit_from == "m" and unit_to == "cm":
        return value * 100
    elif unit_from == "m" and unit_to == "km":
        return value / 1000
    elif unit_from == "km" and unit_to == "m":
        return value * 1000
    elif unit_from == "km" and unit_to == "mi":
        return value * 0.621371
    elif unit_from == "mi" and unit_to == "km":
        return value * 1.60934

    elif unit_from == "g" and unit_to == "kg":
        return value / 1000
    elif unit_from == "kg" and unit_to == "g":
        return value * 1000
    elif unit_from == "kg" and unit_to == "lb":
        return value * 2.20462
    elif unit_from == "lb" and unit_to == "kg":
        return value / 2.20462
    elif unit_from == "lb" and unit_to == "oz":
        return value * 16
    elif unit_from == "oz" and unit_to == "lb":
        return value / 16
    else:
        return "Invalid conversion."

print(convert_unit(100, "cm", "m")) 
print(convert_unit(2.5, "lb", "kg"))  
print(convert_unit(500, "kg", "oz"))  
