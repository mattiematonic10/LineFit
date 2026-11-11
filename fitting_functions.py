def linear(m,x,b):
    y = m*x +b
    return y

def slope_units(x_units, y_units):
    if x_units != 's':
        x_units= x_units.rstrip('s')
    if y_units != 's':
        y_units = y_units.rstrip('s')     
    units = y_units + "/" + x_units
    return units

def print_equation(m,b,y_units,x_units):
    print("The equation of the line is: y=", m, slope_units(x_units, y_units),"+", b, y_units)
    

