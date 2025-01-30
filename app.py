def parallel(resistances):
    total = 0;
    for resistance in resistances:
        total += 1/resistance
    total = round(1/total, 3)
    print(f"{total} ohms")
    return total 

def potential_divider(volt, resistances):
    volt_drops = []
    total_resistance = 0
    for resistance in resistances:
        total_resistance += resistance 
    
    current = volt/total_resistance

    print("CIRCUIT DETAILS")
    print(f"Voltage {volt}v ")
    print(f"Current {current} A")
    print(f"Total resistance {total_resistance}ohms\n")
    print("Resistance        Voltage Drop")
    for resistance in resistances: 
        v_drop = round(current*resistance,2)
        volt_drops.append(v_drop)
        print(f"{resistance}ohms     ->    {v_drop}v")
    return (volt,total_resistance,current,volt_drops)
    
def temperature_check(temp,unit):
    pass

# parallel([330,1000,2200])
potential_divider(9,[3000,1000])