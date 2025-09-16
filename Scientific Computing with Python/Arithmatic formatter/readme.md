# Arithmetic Formatter  

This project is part of **FreeCodeCamp’s Scientific Computing with Python Certification**.  
It implements the `arithmetic_arranger` function, which arranges arithmetic problems vertically and side-by-side, similar to how students solve them on paper.  

---

## Features  

### arithmetic_arranger Function  

The function takes a list of arithmetic problems and returns them formatted vertically.  
It can optionally display the answers when a second argument is set to `True`.  

#### Rules  

- Maximum of **5 problems**.  
  - If more are provided, return:  
    ```
    Error: Too many problems.
    ```  

- Only **addition (+)** and **subtraction (-)** are allowed.  
  - If another operator is used, return:  
    ```
    Error: Operator must be '+' or '-'.
    ```  

- Operands must contain **only digits**.  
  - If not, return:  
    ```
    Error: Numbers must only contain digits.
    ```  

- Operands must be at most **4 digits long**.  
  - If exceeded, return:  
    ```
    Error: Numbers cannot be more than four digits.
    ```  

#### Formatting  

- Numbers are right-aligned.  
- A single space between the operator and the operand.  
- Each problem separated by **four spaces**.  
- A line of dashes under each problem equal to its width.  
- If `True` is passed as the second argument, answers are displayed under the dashes.  

---

## Example Usage  

```python
print(arithmetic_arranger(
    ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
))

print(arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True
))
```

Output:


   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474


Requirements
Python 3.x
No external libraries required

