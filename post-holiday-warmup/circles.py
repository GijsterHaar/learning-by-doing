from math import pi

diameters = [10, 4, 83.2, 62, 33.3]

def get_area(diameters):
    for diameter in diameters:
        area = pi * ((diameter / 2 ) ** 2)
        
        print(f"Circle with diameter {diameter} has an area of " + "%.2f" % area)


if __name__ == "__main__":
    get_area(diameters)