#!/usr/bin/env python3

def ft_garden_intro(name: str, height: int, age: int):
    print("=== Welcome to My Garden ===")
    print()
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print()
    print("=== End of Program ===")


def main():
    ft_garden_intro("Rose", 25, 30)


if __name__ == "__main__":
    main()
