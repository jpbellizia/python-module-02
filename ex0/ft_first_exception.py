#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Only to convert the temperature str -> int"""
    return int(temp_str)


def test_temperature() -> None:
    """Test input_temperature with two values"""
    print("=== Garden Temperature ===")
    for data in ["25", "abc"]:
        print(f"\nInput data is '{data}'")
        try:
            temperature = input_temperature(data)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
