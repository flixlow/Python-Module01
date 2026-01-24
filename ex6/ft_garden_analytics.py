#!/usr/bin/env python3

class GardenManager:
    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}

    class GardenStats:
        def __init__(self):
            pass

    @classmethod
    def create_garden_network(cls, names):
        garden_manager = cls()
        for name in names:
            garden_manager.add_garden(name)
        return garden_manager

    def add_garden(self, owner_name: str) -> None:
        if owner_name in self.gardens.keys():
            print(f"Error : {owner_name} already has a garden.")
        self.gardens.update({owner_name: Garden(owner_name)})


class Garden:
    def __init__(self, owner_name: str) -> None:
        self.name: str = owner_name
        self.plants_dict: dict[int, Plant] = {}
        self.next_id = 0

    def add_plant(self, name: str, height: int, color: str | None,
                  prize: int | None) -> None:
        if color is None:
            self.plants_dict[self.next_id] = Plant(name, height)
        elif prize is None:
            self.plants_dict[self.next_id] = FloweringPlant(
                name, height, color)
        else:
            self.plants_dict[self.next_id] = PrizeFlower(
                name, height, color, prize)
        self.next_id += 1


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.dead: bool = False

    def plant_death(self) -> None:
        """set the plant as death status"""
        self.dead = True


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.bloom_status: bool = False

    def blooming(self) -> None:
        """allow you to let the flower blooms"""
        if self.bloom_status is False:
            self.bloom_status = True


class PrizeFlower(FloweringPlant):
    """Create a Flower which has received prizes"""
    def __init__(self, name: str, height: int, color: str, prize: int) -> None:
        super().__init__(name, height, color)
        self.prize: int = prize
        self.is_favorite: bool = False

    def favorite_prize_flower(self) -> None:
        """Define this plant as part of your favorites ones"""
        if self.is_favorite is False:
            self.is_favorite = True


def main():
    print("=== Garden Management System Demo ===")
    manager = GardenManager()
    manager.add_garden("Alice")
    manager.add_garden("Bob")
    alice_garden = manager.gardens["Alice"]
    alice_garden.add_plant("Oak", 100, None, None)
    alice_garden.add_plant("Rose", 25, "red", None)
    alice_garden.add_plant("Sunflower", 50, "yellow", 10)
    bob_garden = manager.gardens["Bob"]
    bob_garden.add_plant("Birch", 200, None, None)
    bob_garden.add_plant("Poppy", 30, "red", None)
    bob_garden.add_plant("Edelweiss", 10, "white", 25)
    for garden_name, garden in manager.gardens.items():
        print(f"\nGarden: {garden_name}")
        for plant_id, plant in garden.plants_dict.items():
        print(f"  ID {plant_id}: {plant.name}, Height: {plant.height}")


if __name__ == "__main__":
    main()
