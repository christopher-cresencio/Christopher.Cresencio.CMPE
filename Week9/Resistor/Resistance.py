import math

def get_resistance_of_material(resistivity, length, area):
    resistance = resistivity * (length / area)
    print("Resistance of material is: ", resistance)
    return resistance


def get_resistance_by_ohmslaw(voltage, current):
    resistance =  voltage / current
    print("Resistance of material is: ", resistance, "Ω")
    return resistance
