#!/usr/bin/env python3

class Plant:
    created = 0

    def __init__(self, name, starting_height, starting_age):
        self.name = name
        self.height = starting_height
        self.age = starting_age
        Plant.created += 1

    def get_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")

    def get_created(self):
        print(f"Total plants created: {self.created}")


def plant_factory():
    print("=== Plant Factory Output ===")
    data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120}
    ]
    for pdict in data:
        plant = Plant(pdict["name"], pdict["height"], pdict["age"])
        plant.get_info()
    plant.get_created()


def main():
    plant_factory()


if __name__ == "__main__":
    main()
