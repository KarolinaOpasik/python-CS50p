def main():
    time = input("What time is it? ")
    meal_time = convert(time)
    if 7 <= meal_time <= 8:
        print("breakfast time")
    elif 12 <= meal_time <= 13:
        print("lunch time")
    elif 18 <= meal_time <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    time = time.split(":")
    minutes = int(time[0]) * 60 + int(time[1])
    hours = minutes / 60
    return hours

if __name__ == "__main__":
    main()
