import math

def get_inductor_value_of_material(relativeP, Permeability, turns, area, length):
    inductance = (relativeP * Permeability * turns * area) / length
    print("Inductance of material is: ", inductance)
    return inductance

def get_inductive_reactance(frequency, inductance):
    reactance = 2 * math.pi * frequency * inductance
    print("Inductive Reactance is: ", reactance)
    return reactance
