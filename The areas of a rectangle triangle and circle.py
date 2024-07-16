# В зависимости от того, что выберет пользователь, вычислить площадь либо прямоугольника, либо треугольника, либо круга.
# Если выбраны прямоугольник или треугольник, то надо запросить длины сторон, если круг, то его радиус.

from math import sqrt
from math import pi

print("Enter the number of figures:\n1. Rectangle\n2. Triangle\n3. Circle")
figure = input("Enter the number: ")

if figure == '1':

    print("Вы выбрали прямоугольник, введите длины сторон")
    length = int(input("Enter the length: "))
    width = int(input("Enter the width: "))

    square = length * width
    print(f"Square {square}")

elif figure == '2':

    print("Вы выбрали треугольник, введите длины сторон: ")
    side_1 = int(input("Enter the first side: "))
    side_2 = int(input("Enter the second side: "))
    side_3 = int(input("Enter the third side: "))

    half_meter = (side_1 + side_2 + side_3) / 2
    square = sqrt(half_meter * (half_meter - side_1) * (half_meter - side_2) * (half_meter - side_3))
    print(f"Square {square}")

elif figure == '3':

    print("Вы выбрали круг, введите радиус круга")
    R = int(input("Enter the radius: "))

    square = pi * R ** 2
    print(f"Square {square}")

else:
    print("Incorrect input")
