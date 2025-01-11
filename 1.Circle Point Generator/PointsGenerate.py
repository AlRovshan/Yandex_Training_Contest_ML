import random
import math

def generate1():
  a = random.uniform(0,1)
  b = random.uniform(0,1)
  x, y = (a * math.cos(2 * math.pi * b), a * math.sin(2 * math.pi * b))
  return [x,y]

def generate2():
  while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            return [x,y]
with open("points.txt", "w", newline='') as file:
    for cycle in range(10):
        nums = []
        rand = random.randint(1, 2)
        if rand == 1:
            for _ in range(10):
                nums.extend(generate1())
        elif rand == 2:
            for _ in range(10):
                nums.extend(generate2())
        nums_str = " ".join(map(str, nums))
        file.write(nums_str + "\n")
