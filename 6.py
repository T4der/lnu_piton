a = float(input("Введіть перший член геометричної прогресії: "))
b = float(input("Введіть знаменник геометричної прогресії: "))
c = int(input("Введіть кількість членів геометричної прогресії: "))

if a == 1:
    S = a * b
else:
    S = a * (1 - b**c) / (1 - b)

print("Сума геометричної прогресії: " S)
