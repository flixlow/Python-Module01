#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = None
        self.__age = None
    
    def get_height(self) -> int:
        return self.__height
    
    def get_age(self) -> int:
        return self.__age

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid height for {self.name}")
            return
        self.__height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid age for {self.name}")
            return
        self.__age = age

    def get_info(self) -> None:
        print(f"{self.name} {type(self)}: {self.get_height()}cm,\
{self.get_age()} days")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter
        self.shade: int | None = None

    def produce_shade(self) -> None:
        pi: float = 3.14
        self.shade = round(pi * {self.height} * {self.height})

    def get_info(self) -> None:
        print(f"{self.name} provides {self.shade} square meters of shade")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color: str = color
        self.bloom_status: bool = False

    def bloom(self) -> None:
        self.bloom_status = True

    def get_info(self) -> None:
        super().get_info()
        if self.bloom_status is True:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} is waiting to bloom...")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 season: str, value: str):
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = value

    def get_info(self) -> None:
        super().get_info()
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")


def main():
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 25, 30, "red")
    flower.get_info()
    tree = Tree("Oak", 500, 1825, 50)
    tree.get_info()
    vegetable = Vegetable("Tomato", 80, 90, "summer", "C")
    vegetable.get_info()


if __name__ == "__main__":
    main()
