#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name} ({self.__class__.__name__}):\
 {self.height}cm, {self.age} days, "


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        self.shade: int | None = None
        self.produce_shade()

    def produce_shade(self) -> None:
        pi: float = 3.14
        self.shade = round(pi * (self.height / 100) ** 2)

    def get_info(self) -> str:
        return (
            f"{super().get_info()}"
            f"{self.trunk_diameter}cm diameter "
            f"\n{self.name} provides {self.shade} square meters of shade\n"
        )


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom_status: bool = False

    def bloom(self) -> None:
        self.bloom_status = True

    def get_info(self) -> str:
        info = f"{super().get_info()}{self.color} color "
        if self.bloom_status:
            info += f"\n{self.name} is blooming beautifully!\n"
        else:
            info += f"\n{self.name} is waiting to bloom...\n"
        return info


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = value

    def get_info(self) -> str:
        return (
            f"{super().get_info()}"
            f"{self.harvest_season} harvest "
            f"\n{self.name} is rich in {self.nutritional_value}\n"
        )


def main() -> None:
    print("=== Garden Plant Types ===")
    flower1: Flower = Flower("Rose", 25, 30, "red")
    flower2: Flower = Flower("Sunflower", 120, 50, "yellow")
    print(flower1.get_info())
    print(flower2.get_info())
    tree1: Tree = Tree("Oak", 500, 1825, 50)
    tree2: Tree = Tree("Birch", 450, 160, 50)
    print(tree1.get_info())
    print(tree2.get_info())
    vegetable1: Vegetable = Vegetable("Tomato", 80, 70, "summer", "vitamin C")
    vegetable2: Vegetable = Vegetable("Carrot", 20, 90, "autumn", "vitamin B")
    print(vegetable1.get_info())
    print(vegetable2.get_info())
    flower1.bloom()
    print(flower1.get_info())


if __name__ == "__main__":
    main()
