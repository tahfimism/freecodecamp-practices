# Probability Calculator  

This project is part of **FreeCodeCamp’s Scientific Computing with Python Certification**.  
It simulates drawing balls from a hat to estimate probabilities using random experiments.  

---

## Features  

### Hat Class  
- Initialize with any number of balls by color (`Hat(red=3, blue=2)` → `['red','red','red','blue','blue']`).  
- `draw(n)` → randomly removes and returns `n` balls (without replacement).  

### experiment Function  
Runs repeated random experiments to estimate probability.  

**Arguments:**  
- `hat`: a `Hat` object (copied inside function)  
- `expected_balls`: dict of balls to attempt (e.g., `{'red':2, 'green':1}`)  
- `num_balls_drawn`: number of balls per trial  
- `num_experiments`: total trials (larger = more accurate)  

**Returns:** approximate probability (`M/N`).  

---

## Example Usage  

```python
hat = Hat(black=6, red=4, green=3)
prob = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(prob)   # ~0.356
```


#### Notes:
- Randomized results differ slightly each run.
- Designed to pass FreeCodeCamp’s provided tests.