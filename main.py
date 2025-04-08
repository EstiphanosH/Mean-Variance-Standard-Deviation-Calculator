
"""
Test script for mean_var_std.calculate() function
"""

from mean_var_std import calculate

def format_result(result):
    """Format the result dictionary for better readability."""
    formatted = {}
    for key, value in result.items():
        if isinstance(value, list):
            formatted[key] = [v if isinstance(v, list) else round(v, 4) for v in value]
        else:
            formatted[key] = round(value, 4)
    return formatted

def run_tests():
    """Execute test cases for calculate() function."""
    print("Running tests...\n")
    
    # Valid test cases
    valid_tests = [
        ([0, 1, 2, 3, 4, 5, 6, 7, 8], "Sequential numbers"),
        ([2, 6, 2, 8, 4, 0, 1, 5, 7], "Random numbers"),
        ([9, 1, 5, 3, 3, 3, 2, 9, 0], "Repeated numbers"),
        ([5, 5, 5, 5, 5, 5, 5, 5, 5], "All identical")
    ]
    
    # Invalid test cases
    invalid_tests = [
        ([1, 2, 3], "Too few elements"),
        (list(range(10)), "Too many elements"),
        (['a', 'b', 'c', 1, 2, 3, 4, 5, 6], "Non-numeric elements")
    ]
    
    # Run valid tests
    print("VALID INPUT TESTS:")
    for test, description in valid_tests:
        print(f"\nTest: {description}")
        print(f"Input: {test}")
        result = calculate(test)
        print("Result:")
        for k, v in format_result(result).items():
            print(f"{k:>20}: {v}")
    
    # Run invalid tests
    print("\nINVALID INPUT TESTS:")
    for test, description in invalid_tests:
        print(f"\nTest: {description}")
        print(f"Input: {test}")
        try:
            calculate(test)
        except ValueError as e:
            print(f"Expected Error: {str(e)}")

if __name__ == "__main__":
    run_tests()
