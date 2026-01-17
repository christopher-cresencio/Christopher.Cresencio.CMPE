import math


def get_capacitance_by_material(Permeability, Area, Distance):
    dielectricCon = 8.864 * 10e-12
    Capacitance = (Permeability * dielectricCon * Area) / Distance
    print("Capacitance of Material is:", Capacitance)
    return Capacitance


def get_capacitance_by_CV(Charge, Voltage):
    Capacitance = Charge / Voltage
    print("Capacitance of Material:", Capacitance, "F")
    return Capacitance


def get_capacitance_by_Current(Capacitance, dvoverdt):
    ic = Capacitance * dvoverdt
    print("Capacitor Current:", ic)
    return ic


def get_capacitive_reactance(frequency, capacitance):
    reactance = 1 / (2* math.pi * frequency * capacitance)
    print("Capacitive Reactance is: ", reactance)
    return reactance
