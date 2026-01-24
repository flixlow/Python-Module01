#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, \
{self.age} days, ", end="")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        self.shade: int | None = None
        self.produce_shade()

    def produce_shade(self) -> None:
        pi: float = 3.14
        height = self.height
        self.shade = round(pi * height * height)

    def get_info(self) -> None:
        super().get_info(), print(f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.shade} square meters of shade\n")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom_status: bool = False

    def bloom(self) -> None:
        self.bloom_status = True

    def get_info(self) -> None:
        super().get_info(), print(f"{self.color} color")
        if self.bloom_status is True:
            print(f"{self.name} is blooming beautifully!\n")
        else:
            print(f"{self.name} is waiting to bloom...\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = value

    def get_info(self) -> None:
        super().get_info(), print(f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}\n")


def main() -> None:
    print("=== Garden Plant Types ===")
    flower1: Flower = Flower("Rose", 25, 30, "red")
    flower2: Flower = Flower("Sunflower", 120, 50, "yellow")
    flower1.get_info()
    flower2.get_info()
    tree1: Tree = Tree("Oak", 500, 1825, 50)
    tree2: Tree = Tree("Birch", 450, 160, 50)
    tree1.get_info()
    tree2.get_info()
    vegetable1: Vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    vegetable2: Vegetable = Vegetable("Carrot", 70, 90, "automn", "C")
    vegetable1.get_info()
    vegetable2.get_info()
    flower1.bloom()
    flower1.get_info()


if __name__ == "__main__":
    main()
