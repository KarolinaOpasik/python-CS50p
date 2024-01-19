expression = input("Expression: ")
x, y, z = expression.split(" ")

if y == "+":
    solution = int(x) + int(z)
elif y == "-":
    solution = int(x) - int(z)
elif y == "*":
    solution = int(x) * int(z)
else:
    solution = int(x) / int(z)

print(float(solution))
