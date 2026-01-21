#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = None
        self.__age = None
        self.set_height(height)
        self.set_age(age)
        if self.get_height() is not None and self.get_age() is not None:
            print(f"Plant created: {self.name}")
            print(f"Height updated: {self.get_height()} cm [OK]")
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_height(self) -> int:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, height_entry: int) -> None:
        if height_entry < 0:
            print(f"Invalid operation attempted: height {height_entry}cm [REJECTED]")
            print("Security: Negative height rejected")
            return
        self.__height = height_entry

    def set_age(self, age_entry: int) -> None:
        if age_entry < 0:
            print(f"Invalid operation attempted: age {age_entry} days [REJECTED]")
            print("Security: Negative age rejected")
            return
        self.__age = age_entry


def main():
    plant = SecurePlant("Rose", -10, -10)


if __name__ == "__main__":
    main()
