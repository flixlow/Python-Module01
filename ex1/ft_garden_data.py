#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.p_name = name
        self.p_height = height
        self.p_age = age

    def get_info(self):
        print(f"{self.p_name}: {self.p_height}cm, {self.p_age} days old")


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("sunflower", 80, 45)
    plant3 = Plant("cactus", 15, 120)
    plant1.get_info()
    plant2.get_info()
    plant3.get_info()


def main():
    ft_garden_data()


if __name__ == "__main__":
    main()
