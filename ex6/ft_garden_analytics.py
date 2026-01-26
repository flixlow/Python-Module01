#!/usr/bin/env python3

import random


class GardenManager:
    def __init__(self) -> None:
        self.gardens: dict[str, Garden] = {}

    class GardenStats:
        def __init__(self, garden):
            self.garden = garden

        def calculate_stats(self) -> tuple[int, int, dict]:
            total_plants = len(self.garden.plants_list)
            total_growth = self.garden.total_growth
            plant_types = {"Plant": 0, "FloweringPlant": 0, "PrizeFlower": 0}
            for plant in self.garden.plants_list:
                if isinstance(plant, PrizeFlower):
                    plant_types["PrizeFlower"] += 1
                elif isinstance(plant, FloweringPlant):
                    plant_types["FloweringPlant"] += 1
                else:
                    plant_types["Plant"] += 1
            return total_plants, total_growth, plant_types

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        garden_manager = cls()
        return garden_manager

    def add_garden(self, owner_name: str) -> None:
        if owner_name in self.gardens.keys():
            print(f"Error : {owner_name} already has a garden.")
        else:
            self.gardens.update({owner_name: Garden(owner_name)})

    @staticmethod
    def validate_height(height: int) -> bool:
        return height > 0

    def height_validation_test(self) -> bool:
        for garden in self.gardens.values():
            for plant in garden.plants_list:
                if not GardenManager.validate_height(plant.height):
                    return False
        return True

    def get_garden_manager_infos(self):
        scores = []
        for garden in self.gardens.values():
            stats = GardenManager.GardenStats(garden)
            _, _, plant_types = stats.calculate_stats()
            total_height = sum(plant.height for plant in garden.plants_list)
            result = total_height
            result += plant_types["Plant"]
            result += plant_types["FloweringPlant"] * 5
            result += plant_types["PrizeFlower"] * 10
            scores.append(f"{garden.owner_name}: {result}")
        print("Garden scores - " + ", ".join(scores))
        print(f"\nTotal gardens managed: {len(self.gardens)}")


class Garden:
    def __init__(self, owner_name: str) -> None:
        self.owner_name: str = owner_name
        self.plants_list: list[Plant] = []
        self.total_growth: int = 0

    def add_plant(self, name: str, height: int, color: str | None = None,
                  prize: int | None = None) -> None:
        if color is None and prize is not None:
            print("PrizeFlower needs a color")
            return
        if color is None:
            self.plants_list.append(Plant(name, height))
        elif color is not None and prize is None:
            self.plants_list.append(FloweringPlant(name, height, color))
        elif color is not None and prize is not None:
            self.plants_list.append(PrizeFlower(name, height, color, prize))
        print(f"Added {name} to {self.owner_name}'s garden")

    def get_garden_infos(self):
        print(f"=== {self.owner_name}'s Garden Report ===")
        for plant in self.plants_list:
            print(plant.get_infos())
        print()

        stats = GardenManager.GardenStats(self)
        total_plants, total_growth, plant_types = stats.calculate_stats()
        print(f"Plants added: {total_plants}, Total growth: {total_growth}cm")
        print(f"Plant types: {plant_types['Plant']} regular, "
              f"{plant_types['FloweringPlant']} flowering, "
              f"{plant_types['PrizeFlower']} prize flowers")

    def grow_all_plants(self):
        for plant in self.plants_list:
            random_growth = random.randrange(1, 3)
            self.total_growth += random_growth
            plant.grow(random_growth)


class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.dead: bool = False

    def get_infos(self) -> str:
        return f"{self.name}: {self.height}cm"

    def plant_death(self) -> None:
        """set the plant as death status"""
        self.dead = True

    def grow(self, add_cm: int = 1):
        self.height += add_cm
        print(f"{self.name} grew {add_cm}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color
        self.bloom_status: bool = False

    def get_infos(self):
        if self.bloom_status:
            bloom = "(blooming)"
        else:
            bloom = "(not blooming)"
        return f"{super().get_infos()}, {self.color} flowers {bloom}"

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

    def get_infos(self) -> str:
        return f"{super().get_infos()}, Prize points: {self.prize}"

    def favorite_prize_flower(self) -> None:
        """Define this plant as part of your favorites ones"""
        if self.is_favorite is False:
            self.is_favorite = True


def main():
    print("=== Garden Management System Demo ===")
    manager = GardenManager.create_garden_network()
    manager.add_garden("Bob")
    manager.add_garden("Alice")

    alice_garden = manager.gardens["Alice"]
    alice_garden.add_plant("Oak Tree", 100, None, None)
    alice_garden.add_plant("Rose", 25, "red", None)
    alice_garden.add_plant("Sunflower", 50, "yellow", 10)
    print()
    bob_garden = manager.gardens["Bob"]
    bob_garden.add_plant("Birch Tree", 200, None, None)
    bob_garden.add_plant("Poppy", 30, "red", None)
    bob_garden.add_plant("Edelweiss", 10, "white", 25)
    print()
    print(f"{alice_garden.owner_name} is helping all plants grow...")
    alice_garden.grow_all_plants()
    print()
    alice_garden.get_garden_infos()
    # bob_garden.get_garden_infos()
    print()
    print("Height validation test:", manager.height_validation_test())
    manager.get_garden_manager_infos()


if __name__ == "__main__":
    main()
