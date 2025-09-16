# Time Calculator  

This project is part of **FreeCodeCamp’s Scientific Computing with Python Certification**.  
It implements the `add_time` function, which adds a duration to a given start time and returns the correctly formatted result.  

---

## Features  

### add_time Function  

The function accepts:  
1. A **start time** in 12-hour clock format (with AM/PM).  
2. A **duration time** in hours and minutes.  
3. An **optional starting day of the week** (case insensitive).  

It returns the new time after adding the duration, properly formatted.  

#### Rules  

- **Next day / Multiple days later:**  
  - If the result crosses midnight, add `(next day)` to the output.  
  - If more than one day later, show `(n days later)`.  

- **Day of the week (optional):**  
  - If provided, the output includes the resulting day of the week.  
  - The day is shown after the time and before the “days later” text.  

- **Formatting:**  
  - Keep consistent spacing and punctuation.  
  - Handle AM/PM changes correctly.  
  - Assume valid inputs are provided.  
  - Duration minutes are always < 60, but hours can be any integer.  
  - Do not import external libraries.  

---

#### Notes:
Correctly handles AM/PM transitions.
Supports day rollover across multiple days.

## Example Usage  

```python
print(add_time("3:00 PM", "3:10"))
# 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# 12:03 PM

print(add_time("10:10 PM", "3:30"))
# 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# 7:42 AM (9 days later)
```


Requirements
Python 3.x
No external libraries required