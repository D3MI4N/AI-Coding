import pytest
import numpy as np

"""
Gradient descent is an optimization algorithm used to minimize a function (usually a loss function) by iteratively moving towards the minimum value of the function.
"""



def gradient_descent(x, y, iterations=1000, learning_rate=0.0001, stopping_threshold=1e-6):
    """
    Performs gradient descent to fit a line to the data points in x and y.
    This method iteratively adjusts the line (defined by slope 'm' and y-intercept 'c')
    to minimize the sum of squares of the differences (cost) between predicted and actual y-values.

    Args:
    x: Array of predictor variable values.
    y: Array of dependent variable values.
    iterations: Maximum number of iterations for the gradient descent.
    learning_rate: The step size during gradient descent.
    stopping_threshold: The threshold for stopping the iterations when the change in 'm' and 'c' becomes very small.

    Returns:
    m: The slope of the fitted line.
    c: The y-intercept of the fitted line.
    """

    # Initialize the slope (m) and y-intercept (c) with zero values.
    m, c = 0, 0
    # Number of data points in the dataset.
    n = len(x)

    for _ in range(iterations):
        # Predict the y-values using the current values of m and c.
        y_pred = m * x + c

        # Compute the cost (mean squared error) between predicted and actual y-values.
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])

        # Calculate gradients for m and c to minimize the cost.
        # dm and dc represent the direction and amount by which m and c should be updated.
        dm = -(2/n) * sum(x * (y - y_pred))  # Gradient with respect to m
        dc = -(2/n) * sum(y - y_pred)        # Gradient with respect to c

        # Update m and c by moving against the gradient direction by the learning rate.
        m -= learning_rate * dm
        c -= learning_rate * dc

        # Check if the updates to m and c are smaller than the stopping threshold.
        # If yes, it means convergence has been achieved and stop further updates.
        if max(abs(learning_rate * dm), abs(learning_rate * dc)) < stopping_threshold:
            break

    return m, c

def test_gradient_descent():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])

    # Perform gradient descent to find the optimal m and c
    m, c = gradient_descent(x, y)

    # Print the slope and intercept of the fitted line
    print(f"Slope: {m}, Intercept: {c}")
