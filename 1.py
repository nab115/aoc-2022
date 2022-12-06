def a():
    data = open("1.txt", "r").read()

    max_cal = 0
    elves = data.split("\n\n")

    for elf in elves:
        temp = sum(int(i) for i in elf.split())
        if temp > max_cal:
            max_cal = temp

    print(max_cal)

def b():
    data = open("1.txt", "r").read()

    elves_food = [sum(int(food) for food in elf.split()) for elf in data.split("\n\n")]
    elves_food.sort(reverse=True)

    print(sum(elves_food[0:3]))



if __name__ == "__main__":
    a()
    b()