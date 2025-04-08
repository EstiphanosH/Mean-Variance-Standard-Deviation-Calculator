import numpy as np

def calculate(lst):
    """Calculate statistical metrics from a 3x3 matrix.

    Args:
        lst (list): A list containing 9 numbers to be converted to a 3x3 matrix

    Returns:
        dict: Dictionary containing mean, variance, standard deviation,
              max, min, and sum for axes and flattened matrix

    Raises:
        ValueError: If input list doesn't contain exactly 9 elements
    """
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    try:
        arr = np.array(lst, dtype=np.float64).reshape(3, 3)
    except ValueError as e:
        raise ValueError("All elements must be numbers") from e
    
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),
            arr.mean(axis=1).tolist(),
            float(arr.mean())
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            float(arr.var())
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            float(arr.std())
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            float(arr.max())
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            float(arr.min())
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            float(arr.sum())
        ]
    }
    
    return calculations
