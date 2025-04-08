#!/usr/bin/env python3
"""
main.py - Test script for mean_var_std.calculate() function

This script demonstrates the usage of the calculate() function from mean_var_std.py
by running several test cases and displaying their results in a readable format.
"""

from mean_var_std import calculate

def print_results(result_dict):
    """Pretty-print the results dictionary in a human-readable format.
    
    Args:
        result_dict (dict): Dictionary containing the calculation results
                           in the format returned by calculate()
    """
    for key, value in result_dict.items():
        print(f"{key.title() + ':':<20} {value}")

def run_test_case(test_input, case_number=None):
    """Run a single test case and display the results.
    
    Args:
        test_input (list): List of 9 numbers to test
        case_number (int, optional): Test case number for display purposes
    """
    if case_number:
        print(f"\n{' Test Case ' + str(case_number) + ' ':-^50}")
    else:
        print(f"\n{' Test Case ':-^50}")
    
    print(f"Input: {test_input}")
    try:
        result = calculate(test_input)
        print("\nResults:")
        print_results(result)
    except ValueError as e:
        print(f"\nError: {e}")

def main():
    """Main function to execute test cases for the calculate() function."""
    # Standard test cases (valid inputs)
    standard_tests = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8],  # Sequential numbers
        [2, 6, 2, 8, 4, 0, 1, 5, 7],   # Random numbers
        [9, 1, 5, 3, 3, 3, 2, 9, 0],   # Repeated numbers
        [5, 5, 5, 5, 5, 5, 5, 5, 5]    # All identical numbers
    ]
    
    # Edge cases (invalid inputs)
    edge_cases = [
        [1, 2, 3, 4, 5],              # Too few elements
        list(range(10)),               # Too many elements
        ['a', 'b', 'c', 1, 2, 3, 4, 5, 6]  # Non-numeric elements
    ]
    
    print("="*50)
    print(" TESTING MEAN_VAR_STD.CALCULATE() FUNCTION ")
    print("="*50)
    
    # Run standard test cases
    print("\nSTANDARD TEST CASES (VALID INPUTS):")
    for i, test_input in enumerate(standard_tests, 1):
        run_test_case(test_input, i)
    
    # Run edge cases
    print("\nEDGE CASES (INVALID INPUTS):")
    for i, test_input in enumerate(edge_cases, len(standard_tests)+1):
        run_test_case(test_input, i)
    
    print("\n" + "="*50)
    print(" TESTING COMPLETE ")
    print("="*50)

if __name__ == "__main__":
    main()
