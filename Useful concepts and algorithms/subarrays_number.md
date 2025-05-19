# Element Contribution to Subarrays

This note explains how to compute the number of subarrays that include a given element at index `i`, in an array of length `N`.

## Key Idea

Each element `A[i]` appears in multiple subarrays. To count how many, consider:

- You can start the subarray at any index from `0` to `i` → `(i + 1)` options  
- You can end the subarray at any index from `i` to `N - 1` → `(N - i)` options

So the total number of subarrays that include `A[i]` is:

```
(i + 1) * (N - i)
```

## Example

For array: `A = ['a', 'b', 'c', 'd', 'e']`, index `i = 2` (element `'c'`), `N = 5`:

```
(i + 1) = 3   → subarrays can start at [0, 1, 2]  
(N - i) = 3   → subarrays can end at [2, 3, 4]  
Total = 3 * 3 = 9 subarrays that include 'c'
```

## Application

This trick is useful when you want to:
- **Sum up contributions** of elements across all subarrays
- **Count how many times an element influences something** (like XOR, AND, or MOD results in subarrays)

### Example Use Case: Sum of All Subarray Elements

```python
def sum_of_all_subarrays(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        total += arr[i] * (i + 1) * (n - i)
    return total
```

---

## Note on Parity

If `i` and `N` are both even, the product `(i + 1) * (N - i)` is still non-zero.  
This may be relevant in problems that depend on parity (e.g., when considering alternating signs or parity-specific conditions).

---
