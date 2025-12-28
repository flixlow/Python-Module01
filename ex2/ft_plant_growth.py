#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.pl_age = age
        self.growth = 0
        self.day = 1

    def grow(self):
        self.growth += self.height / self.pl_age
        self.height += self.height / self.pl_age

    def age(self):
        self.pl_age += 1
        self.day += 1

    def get_info(self):
        print(f"=== Day {self.day} ===")
        print(f"{self.name}: {round(self.height)}cm, {self.pl_age} days old")
        if self.day >= 7:
            print(f"Growth this week: +{round(self.growth)}cm")


def ft_plant_growth():
    plant1 = Plant("Rose", 25, 30)
    plant1.get_info()
    for day in range(6):
        plant1.grow()
        plant1.age()
    plant1.get_info()


def main():
    ft_plant_growth()


if __name__ == "__main__":
    main()

# plant2 = Plant("sunflower", 80, 45)
# plant3 = Plant("cactus", 15, 120)
