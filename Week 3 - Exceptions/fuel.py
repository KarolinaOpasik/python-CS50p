while True:
    try:
        fraction = input("Fraction: ")
        answer = fraction.split("/")
        x = int(answer[0])
        y = int(answer[1])
        if x > y:
            continue
        break
    except (ValueError, ZeroDivisionError):
        continue

fuel = round(x / y * 100)

if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:
    print(str(fuel) + "%")
