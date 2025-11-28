# This Algorithm computes an approximation of the mathematical constant π using a method known as
# Monte Carlo simulation

import random

points_in_circle = 0
num_point = 50000
for i in range(num_point):
    # Generate random x and y between-1 and 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # Check if the point is inside the unit circle
    if x ** 2 + y ** 2 <= 1:
        points_in_circle += 1
# Calculate and return the result
print(4 * (points_in_circle / num_point))
