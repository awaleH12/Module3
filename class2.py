PI = 3.14
radius = int(input("write radius: "))

def calculate_area(radius):
    area = radius * PI *radius
    print(area)

calculate_area(radius)


def calculate_area2():
    area2 = radius *PI * radius
    return area2

print(calculate_area2())


