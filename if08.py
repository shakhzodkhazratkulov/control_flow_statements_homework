def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a > 9 and a % 2 == 1:
        x = "two-digit odd number"
    if a > 9 and a % 2 == 0:
        x = "two-digit even number"
    if a > 99 and a % 2 == 1:
        x = "three-digit odd number"
    if a > 99 and a % 2 == 0:
        x = "three-digit even number"
    
    return x
print(main(7))