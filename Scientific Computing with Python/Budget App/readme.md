# Budget App  

This project is part of **FreeCodeCamp’s Scientific Computing with Python Certification**.  
It implements a `Category` class to model a budget system and a function `create_spend_chart` to visualize spending distribution across categories.  

---

## Features  

### Category Class  

Each budget category (e.g., Food, Clothing, Entertainment) is represented by a `Category` object.  
It contains a `ledger` (list) that tracks deposits, withdrawals, and transfers.  

#### Methods  
- **`deposit(amount, description="")`**  
  Adds money to the category with an optional description.  

- **`withdraw(amount, description="")`**  
  Deducts money as a negative amount in the ledger if sufficient funds exist.  
  Returns `True` if successful, `False` otherwise.  

- **`get_balance()`**  
  Returns the current balance in the category.  

- **`transfer(amount, category)`**  
  Transfers money to another category.  
  Adds withdrawal in the source and deposit in the destination with appropriate descriptions.  
  Returns `True` if successful, `False` otherwise.  

- **`check_funds(amount)`**  
  Checks if the category has enough balance.  
  Returns `True` if funds are available, `False` otherwise.  

#### String Representation  
When printed, a category displays:  
- Title centered within `*` (30 characters wide).  
- Ledger entries (23 chars of description, right-aligned amount with 2 decimals).  
- Total balance at the bottom.  

**Example:**  
```
Food
deposit 1000.00
groceries -10.15
restaurant and more fo -15.89
Transfer to Clothing -50.00
Total: 923.96
```



---

### create_spend_chart Function  

A function that generates a text-based bar chart showing the percentage spent in each category.  

- Percentages are based **only on withdrawals**.  
- Percentages are rounded down to the nearest 10.  
- The chart is vertical, with categories displayed below the bars.  

**Example:**  
```
Percentage spent by category
100|
90|
80|
70|
60| o
50| o
40| o
30| o
20| o o
10| o o o
0| o o o
----------
F C A
o l u
o o t
d t o
h
i
n
g
```


---

## Example Usage  

```python
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print(clothing)
print(create_spend_chart([food, clothing]))
```

Requirements
Python 3.x

No external libraries required



