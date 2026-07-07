# FreeCodeCamp: Scientific Computing with Python - Solutions Suite

## 1. Project Overview
This repository serves as a comprehensive collection of solutions for the **Scientific Computing with Python** certification from [freeCodeCamp](https://www.freecodecamp.org/). The projects cover a wide array of fundamental and intermediate programming concepts, including algorithmic logic, string manipulation, Object-Oriented Programming (OOP), data structures, and statistical simulations.

The primary objective of this suite is to demonstrate proficiency in Python for solving computational problems, managing data, and building modular, reusable code architectures.

---

## 2. Mono-repo / Sub-project Breakdown

This repository is structured as a mono-repo containing five distinct sub-projects, each located within the `Scientific Computing with Python/` directory.

### A. Arithmetic Formatter
*   **Purpose:** Automates the vertical arrangement of arithmetic problems to aid students in visualizing calculations.
*   **Files:**
    - `Scientific Computing with Python/Arithmatic formatter/formatter.py`: Main logic for the arithmetic arranger.
    - `Scientific Computing with Python/Arithmatic formatter/readme.md`: Specific project requirements and constraints.
*   **Tech Stack:** Python 3 (Core).
*   **Core Logic:** String parsing, conditional formatting, and error validation.

### B. Budget App
*   **Purpose:** A personal finance management tool that tracks deposits, withdrawals, and transfers across different categories while providing spending visualizations.
*   **Files:**
    - `Scientific Computing with Python/Budget App/budget.py`: Contains the `Category` class and `create_spend_chart` function.
    - `Scientific Computing with Python/Budget App/readme.md`: Detailed specifications for the budget tracker.
*   **Tech Stack:** Python 3 (OOP).
*   **Core Logic:** Class-based state management, ledger tracking, and ASCII-based data visualization.

### C. Polygon Calculator
*   **Purpose:** A geometric utility suite for calculating properties of rectangles and squares.
*   **Files:**
    - `Scientific Computing with Python/Polygon calculator/main.py`: Definitions for `Rectangle` and `Square` classes.
    - `Scientific Computing with Python/Polygon calculator/readme.md`: Geometry logic specifications.
*   **Tech Stack:** Python 3 (OOP, Inheritance).
*   **Core Logic:** Class inheritance, method overriding, and ASCII shape rendering.

### D. Probability Calculator
*   **Purpose:** A statistical tool that estimates the probability of specific outcomes in a random draw scenario using Monte Carlo simulations.
*   **Files:**
    - `Scientific Computing with Python/Probability Caclculator/main.py`: Implements the `Hat` class and the Monte Carlo `experiment` function.
    - `Scientific Computing with Python/Probability Caclculator/readme.md`: Statistical simulation requirements.
*   **Tech Stack:** Python 3 (Math, Random, Deep Copy).
*   **Core Logic:** Stochastic simulations, deep object cloning, and frequency analysis.

### E. Time Calculator
*   **Purpose:** A temporal arithmetic tool that adds durations to start times, accounting for AM/PM transitions and multi-day rollovers.
*   **Files:**
    - `Scientific Computing with Python/Time calculator/time_calculator.py`: Logic for temporal arithmetic and day calculation.
    - `Scientific Computing with Python/Time calculator/readme.md`: Time formatting rules and examples.
*   **Tech Stack:** Python 3 (Core).
*   **Core Logic:** Time-base conversion (12h to 24h), modulo arithmetic, and string formatting.

---

## 3. Exhaustive Feature List

### Arithmetic Formatter
- **Input Validation:**
    - Limits to a maximum of 5 problems.
    - Restricts operators to addition (+) and subtraction (-).
    - Ensures operands contain only digits.
    - Enforces a 4-digit maximum per operand.
- **Dynamic Formatting:**
    - Right-aligns numbers based on the longest operand in the pair.
    - Automatically calculates and renders dash separators.
    - Supports optional answer display via a boolean flag.
    - Maintains precisely four spaces between adjacent problems.

### Budget App
- **`Category` Class Features:**
    - `deposit`: Records amounts with optional descriptions.
    - `withdraw`: Validates funds before deducting; returns success status.
    - `get_balance`: Real-time balance retrieval.
    - `transfer`: Inter-category movement of funds with automated ledger descriptions.
    - `check_funds`: Utility method for balance validation.
- **Visualization:**
    - Custom `__str__` method for a formatted, aligned ledger view.
    - `create_spend_chart`: Generates a vertical bar chart showing spending distribution percentages (rounded down to the nearest 10%).

### Polygon Calculator
- **`Rectangle` Class:**
    - Attributes: `width`, `height`.
    - Area, Perimeter, and Diagonal calculations.
    - `get_picture`: ASCII representation of the shape (limited to 50x50 to prevent overflow).
    - `get_amount_inside`: Calculates how many instances of another shape can fit within the current one.
- **`Square` Class:**
    - Inherits from `Rectangle`.
    - Synchronized side management (setting width also updates height and vice versa).

### Probability Calculator
- **`Hat` Class:**
    - Dynamic initialization using keyword arguments (e.g., `red=5, blue=2`).
    - `draw`: Randomly removes balls from the hat; handles cases where draw amount exceeds current contents.
- **Simulation Engine (`experiment` function):**
    - Performs N trials of drawing balls.
    - Uses deep copies to ensure each trial starts with the same initial state without mutating the original object.
    - Calculates probability based on the ratio of successful matches to total trials.

### Time Calculator
- **Core Functionality:**
    - Adds hours and minutes to a start time.
    - Handles AM to PM and PM to AM transitions.
- **Advanced Features:**
    - **Day Rollover:** Displays "(next day)" or "(n days later)".
    - **Weekday Tracking:** Optional argument to provide a starting day (e.g., "Monday"), with the function returning the correctly calculated resulting day.
    - **Case-Insensitivity:** Handles "mOnDay" or "tUESday" gracefully.

---

## 4. Technical Architecture & Tech Stack

- **Language:** Python 3.x
- **Programming Paradigm:**
    - **Functional/Procedural:** Used in `Arithmetic Formatter` and `Time Calculator`.
    - **Object-Oriented (OOP):** Heavily utilized in `Budget App`, `Polygon Calculator`, and `Probability Calculator`.
- **Key Modules:**
    - `random`: Used for drawing balls in the Probability Calculator.
    - `copy`: Specifically `copy.deepcopy` to maintain state integrity during simulations.

### Design Patterns
- **Inheritance:** The `Square` class inherits from `Rectangle`, demonstrating "Is-A" relationship and code reuse.
- **Simulation Pattern:** The Monte Carlo method is used in the Probability Calculator to approximate values that are difficult to calculate analytically.

---

## 5. Under-the-Hood Optimizations

- **String Buffering:** In `Arithmetic Formatter`, lines are constructed as lists and joined at the end to improve performance over repeated string concatenation.
- **Efficient State Management:** The `Budget App` uses a single list of dictionaries (`ledger`) to maintain a complete history while calculating balance on the fly or via a cached attribute.
- **Input Normalization:** The `Time Calculator` converts 12-hour times to 24-hour "minutes since midnight" internally to simplify mathematical operations, before converting back to the 12-hour format for the user.
- **Memory Integrity:** Use of `copy.deepcopy` in the `Probability Calculator` prevents side effects across multiple simulation trials, ensuring statistical accuracy.
- **Robust Error Handling:** Custom error messages are returned as strings in `Arithmetic Formatter` to comply with specific project requirements and provide user-friendly feedback.

---

## 6. Setup & Installation Instructions

### Prerequisites
- Python 3.6 or higher installed on your system.

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/freecodecamp-practices.git
    cd freecodecamp-practices
    ```

2.  **Environment Setup:**
    No external dependencies (like `pip` packages) are required for these projects as they rely on the Python Standard Library.

### Running the Projects
Each sub-project can be run individually. Note: File paths reflect the actual (sometimes misspelled) directory names in the repository.

- **Arithmetic Formatter:**
  ```bash
  python3 "Scientific Computing with Python/Arithmatic formatter/formatter.py"
  ```
- **Budget App:**
  ```bash
  python3 "Scientific Computing with Python/Budget App/budget.py"
  ```
- **Polygon Calculator:**
  ```bash
  python3 "Scientific Computing with Python/Polygon calculator/main.py"
  ```
- **Probability Calculator:**
  ```bash
  python3 "Scientific Computing with Python/Probability Caclculator/main.py"
  ```
- **Time Calculator:**
  ```bash
  python3 "Scientific Computing with Python/Time calculator/time_calculator.py"
  ```

---

## 7. Usage Examples

### Arithmetic Formatter
```python
from formatter import arithmetic_arranger
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
```

### Budget App
```python
from budget import Category, create_spend_chart
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
entertainment = Category("Entertainment")
food.transfer(50, entertainment)
print(food)
```

### Polygon Calculator
```python
from main import Rectangle, Square
rect = Rectangle(10, 5)
print(rect.get_area()) # 50
sq = Square(9)
print(sq.get_picture())
```

### Probability Calculator
```python
from main import Hat, experiment
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
```

### Time Calculator
```python
from time_calculator import add_time
print(add_time("11:06 PM", "2:02")) # 1:08 AM (next day)
print(add_time("8:40 AM", "12:00", "Saturday")) # 8:40 PM, Saturday
```
