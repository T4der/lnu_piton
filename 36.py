x = float(input(" Введіть першу координату :"))
print(" x =", x)
y = float(input("Введіть другу координату :"))
print(" y =", y)
x0 = float(input(" Введіть першу координату центра круга :"))
print(" x0=", x0)
y0 = float(input("Введіть другу координату центра круга :"))
print(" y0 =", y0)
r = float(input("Введіть радіус круга :"))
print(" r =", r)



if (x - x0)**2 + (y - y0)**2 <= r**2:
    print("ця точка належить кругу")
elif (x - x0)**2 + (y - y0)**2 >= r**2:
    print("ця точка не належить кругу")