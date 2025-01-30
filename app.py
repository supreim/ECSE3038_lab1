def parallel(resistances):
    total = 0;
    for resistance in resistances:
        total += 1/resistance
    total = round(1/total, 3)
    print(f"{total} ohms")

def potential_divider(volt, resistances):
    pass
def temperature_check(temp,unit):
    pass

parallel([330,1000,2200])