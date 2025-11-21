# My2ndProject

## Project Zero - 防呆計算機 (Safe Division Calculator)

This project implements a safe division function that prevents division by zero errors, ensuring safe calculations every time.

### Files

- **safe_division.py** - Contains the `safe_division(a, b)` function that safely divides two numbers
- **test_safe_division.py** - Comprehensive unit tests for the safe_division function

### Usage

```python
from safe_division import safe_division

# Normal division
result = safe_division(10, 2)  # Returns: 5.0

# Safe handling of division by zero
result = safe_division(10, 0)  # Returns: None (prevents error)

# Works with negative numbers
result = safe_division(-15, 3)  # Returns: -5.0
```

### Running Tests

To run the unit tests:

```bash
python3 -m unittest test_safe_division.py -v
```

### Features

✅ **Task One Complete**: Implemented `safe_division(a, b)` function that prevents division by zero  
✅ **Task Two Complete**: Generated comprehensive unit tests (18 test cases) covering:
- Basic division operations
- Division by zero handling
- Negative numbers
- Floating point numbers
- Edge cases

All tests pass successfully!