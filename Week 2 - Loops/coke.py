due = 50

while 0 < due <= 50:
    print("Amount due: ", due)
    coins = int(input("Insert coin: "))
    if coins in (5, 10, 25):
        due -= coins

change = 0 - due
print("Change owned:", change)
