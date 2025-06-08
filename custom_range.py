def custom_range(start, end, step):
    """Generate numbers from start to end with a specified step."""
    current = start
    if step == 0:
        raise ValueError("Step must be non-zero")
    if step > 0:
        while current < end:
            yield round(current, 2)  # Round to 2 decimal places for better readability
            current += step
    else:
        while current > end:
            yield round(current, 2)
            current += step
# Example usage of custom_range function
for num in custom_range(1.0, 2.0, 0.2):
    print(num)