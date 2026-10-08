#!/usr/bin/env python3

class GardenError(Exception):
    """Base error for every garden problem."""

    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    """Error for problems with plants."""

    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Error for problems with watering."""

    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(is_wilting: bool) -> None:
    """Raise a PlantError if the plant is wilting."""
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water(water_level: int) -> None:
    """Raise a WaterError if the tank level is too low."""
    if water_level < 10:
        raise WaterError("Not enough water in the tank!")


def test_plant_error() -> None:
    """Catch a PlantError by its specific type."""
    print("\nTesting PlantError...")
    try:
        check_plant(True)
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def test_water_error() -> None:
    """Catch a WaterError by its specific type."""
    print("\nTesting WaterError...")
    try:
        check_water(2)
    except WaterError as error:
        print(f"Caught WaterError: {error}")


def test_all_garden_errors() -> None:
    """Show that catching GardenError also catches its subclasses."""
    print("\nTesting catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        check_water(2)
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def main() -> None:
    """Run every custom error demo."""
    print("=== Custom Garden Errors Demo ===")
    test_plant_error()
    test_water_error()
    test_all_garden_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
