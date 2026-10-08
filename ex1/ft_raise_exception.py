#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    """Convert the temperature only if is on the interval 0 to 40 Celsius"""
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature() -> None:
    """Test input_temperature with valid, invalid and extreme data."""
    print("=== Garden Temperature Checker ===")
    for data in ["25", "abc", "100", "-50"]:
        print(f"\nInput data is '{data}'")
        try:
            temperature = input_temperature(data)
            print(f"Temperature is now {temperature}°C")
        except ValueError as error:
            print(f"Caught input_temperature error: {error}")
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
