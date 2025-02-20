import math

radio= float(input("Radio del círculo: "))
perimetro = 2* math.pi *radio
area = math.pi * radio ** 2

print(f"\nCírculo de radio {radio}:")
print(f"Perímetro: {perimetro: .2f}")
print(f"Área: {area: .2f}")
altura = float(input("Altura del cilindro: "))
volumen = area * altura

print(f"Volumen del cilindro: {volumen: .2f}")
