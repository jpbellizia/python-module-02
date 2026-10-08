#!/usr/bin/env python3

def garden_operations(operation_number: int) -> None:
    """Run a faulty operation depending on operation_number."""
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "abc" + 1
    return


def test_error_types() -> None:
    """Show each error type being raised, caught and explained."""
    print("=== Garden Error Types Demo ===")
    for operation in range(5):
        print(f"Testing operation {operation}...")
        try:
            garden_operations(operation)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
