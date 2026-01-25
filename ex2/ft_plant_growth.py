#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.plant_age = age
        self.growth = 0

    def grow(self):
        self.growth += 1
        self.height += 1
        self.age()

    def age(self):
        self.plant_age += 1

    def get_info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, {self.plant_age} days old")


def ft_plant_growth():
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 100, 45)
    plant_list = [plant1, plant2]
    print("=== Day 1 ===")
    for plant in plant_list:
        print(plant.get_info())
    for day in range(7):
        for plant in plant_list:
            plant.grow()
    print("=== Day 7 ===")
    for plant in plant_list:
        print(plant.get_info())
    for plant in plant_list:
        print(f"[{plant.name}] Growth this week: +{plant.growth}cm")


def main():
    ft_plant_growth()


if __name__ == "__main__":
    main()
