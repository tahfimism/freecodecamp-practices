# Polygon Area Calculator

This project is part of **FreeCodeCamp’s Scientific Computing with Python Certification**.  
It implements two OOP classes—`Rectangle` and `Square`—with geometry utilities and text-based shape rendering.

---

## Features

### Rectangle
Initialized with **width** and **height**.

**Methods**
- `set_width(w)` – set width  
- `set_height(h)` – set height  
- `get_area()` → `width * height`  
- `get_perimeter()` → `2 * width + 2 * height`  
- `get_diagonal()` → `(width**2 + height**2) ** 0.5`  
- `get_picture()` → returns a multi-line string of `*` with `height` lines and `width` stars per line.  
  - If `width > 50` **or** `height > 50`: returns `"Too big for picture."`  
- `get_amount_inside(shape)` → how many times `shape` (no rotation) fits inside this rectangle, as an integer count  
- `__str__()` → `"Rectangle(width=W, height=H)"`

### Square (subclass of Rectangle)
Initialized with a single **side** (stores to both width and height).

**Methods**
- Inherits all `Rectangle` methods  
- `set_side(n)` – sets both width and height to `n`  
- `set_width(n)` and `set_height(n)` – override to set **both** dimensions (to keep it a square)  
- `__str__()` → `"Square(side=S)"`

---

## Example Usage

```python
rect = Rectangle(10, 5)
print(rect.get_area())          # 50
rect.set_height(3)
print(rect.get_perimeter())     # 26
print(rect)                     # Rectangle(width=10, height=3)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())            # 81
sq.set_side(4)
print(sq.get_diagonal())        # 5.656854249492381
print(sq)                       # Square(side=4)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8
```

Expected Output

```
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```



#### Notes
- get_picture() uses plain-text (ASCII) rendering; large shapes are intentionally blocked to avoid massive output.
- get_amount_inside counts whole fits only; no partial fits and no rotation.
- Designed to pass FreeCodeCamp’s unit tests exactly (spacing, strings, and method names).