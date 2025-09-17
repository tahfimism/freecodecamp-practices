import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, n):
        if n >= len(self.contents):
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        drawn = random.sample(self.contents, n)
        for ball in drawn:
            self.contents.remove(ball)
        return drawn




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0

    for _ in range(num_experiments):
        
        trial_hat = copy.deepcopy(hat)

        drawn = trial_hat.draw(num_balls_drawn)

        counts = {}
        for c in drawn:
            counts[c] = counts.get(c, 0) + 1

        ok = all(counts.get(color, 0) >= needed
                 for color, needed in expected_balls.items())

        if ok:
            successes += 1

    return successes / num_experiments
