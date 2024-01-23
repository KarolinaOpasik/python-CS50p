# https://cs50.harvard.edu/python/2022/psets/4/professor/

import random

def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level)
        answer = int(input(f"{x} + {y} = "))
        solution = x + y
        correct_answer = f"{x} + {y} = {solution}"
        if answer != solution:
            print("EEE")
            for _ in range(2):
                answer = int(input(f"{x} + {y} = "))
                if answer == solution:
                    score += 1
                else:
                    print("EEE")
            print(correct_answer)
        else:
            score += 1
            continue
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in (1, 2, 3):
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()
