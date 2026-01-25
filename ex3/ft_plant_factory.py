#!/usr/bin/env python3

class Plant:
    created = 0

    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
        Plant.created += 1

    def get_info(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"

    @staticmethod
    def get_created() -> str:
        return f"Total plants created: {Plant.created}"


def plant_factory(data: list[dict]) -> list[Plant]:
    plant_created = []
    for plant_data in data:
        plant = Plant(plant_data["name"],
                      plant_data["height"],
                      plant_data["age"])
        plant_created.append(plant)

    return plant_created


def main():
    data = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120}
    ]
    plants = plant_factory(data)
    print("=== Plant Factory Output ===")
    for plant in plants:
        print(plant.get_info())
    print(Plant.get_created())


if __name__ == "__main__":
    main()
