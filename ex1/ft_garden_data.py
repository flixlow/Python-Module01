#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int = 0, age: int = 0) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    plant_list = [plant1, plant2, plant3]
    for plant in plant_list:
        print(plant.get_info())


def main():
    ft_garden_data()


if __name__ == "__main__":
    main()
