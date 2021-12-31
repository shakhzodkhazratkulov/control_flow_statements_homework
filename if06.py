def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    positive = 0
    negative = 0
    if a > 0:
        positive += 1
    if b > 0:
        negative += 1
    if c > 0:
        positive += 1
    if a < 0:
        negative += 1
    if b < 0:
        negative += 1
    if c < 0:
        negative += 1
    if positive > negative:
        x = "there are a lot of positive numbers"
    else:
        x = "there are a lot of negative numbers"
    return x
print(main(2,3,8))
    