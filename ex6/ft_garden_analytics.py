#!/usr/bin/env python3

class GardenManager:
    """Global garden manager"""
    def __init__(self):
        self.garden: list[Garden] = []
        self.garden_index: int = 0

    class GardenStats:
        def __init__(self):
            pass

    @classmethod
    def create_garden_network(cls, gardens):
        gam = cls()
        gam.garden = gardens
        return gam


class Garden:
    def __init__(self, owner_name):
        pass


class Plant:
    """parent class for plant"""
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self.height: int = height
        self.age: int = age


class FloweringPlant(Plant):
    pass


class PrizeFlower(FloweringPlant):
    pass


def main():
    print("=== Garden Management System Demo ===")
    gam = GardenManager.create_garden_network(["bob", "alice"])
    print(gam.garden)


if __name__ == "__main__":
    main()
