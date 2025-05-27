# GCD: Euclidean Algorithm

A minimal implementation to find the greatest common divisor of two integers.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

Note: Assumes a >= b. This is the classic Euclidean algorithm.
