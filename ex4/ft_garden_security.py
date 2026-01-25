#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int | None = None
        self.__age: int | None = None
        self.set_height(height)
        self.set_age(age)
        self.valid_input()

    def valid_input(self) -> None:
        if self.get_height() is not None and self.get_age() is not None:
            print(f"Plant created: {self.name}")
            print(f"Height updated: {self.get_height()} cm [OK]")
            print(f"Age updated: {self.get_age()} days [OK]\n")

    def get_height(self) -> None | int:
        return self.__height

    def get_age(self) -> None | int:
        return self.__age

    def set_height(self, height_entry: int) -> bool:
        if height_entry < 0:
            print(f"Invalid operation attempted: height {height_entry}cm\
 [REJECTED]")
            print("Security: Negative height rejected\n")
            return False
        self.__height = height_entry
        return True

    def set_age(self, age_entry: int) -> bool:
        if age_entry < 0:
            print(f"Invalid operation attempted: age {age_entry} days\
 [REJECTED]")
            print("Security: Negative age rejected")
            return False
        self.__age = age_entry
        return True

    def display(self) -> None:
        print(f"Current Plant: {self.name}\
 ({self.get_height()}cm, {self.get_age()} days)\n")


def main() -> None:
    plant: SecurePlant = SecurePlant("Rose", 25, 10)
    plant.display()
    plant.set_height(-1)


if __name__ == "__main__":
    main()
